# -*- coding: utf-8 -*-
"""Rendu double : un même contenu produit un .docx (python-docx) et un .pdf (reportlab)."""
import os
import re
from datetime import date

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle, Image, PageBreak, KeepTogether, Flowable,
                                NextPageTemplate)
from PIL import Image as PILImage

# --------------------------------------------------------------------------- #
BLEU = "1F4E79"
BLEU_CLAIR = "2E75B6"
ORANGE = "C55A11"
VERT = "2E7D32"
ROUGE = "B00020"
GRIS = "595959"
GRIS_CLAIR = "F2F2F2"
FOND_BLEU = "EAF0F7"
FOND_ORANGE = "FDF1E7"
FOND_VERT = "EDF5EC"
FOND_ROUGE = "FBEAEA"

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DJ", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DJ-B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DJ", normal="DJ", bold="DJ-B", italic="DJ", boldItalic="DJ-B")

PAGE_W, PAGE_H = A4
M_L = M_R = 1.9 * cm
M_T = 2.2 * cm
M_B = 1.9 * cm
CONTENT_W = PAGE_W - M_L - M_R


def hexc(h):
    return colors.HexColor("#" + h)


# --------------------------------------------------------------------------- #
# PDF helpers
# --------------------------------------------------------------------------- #
class Band(Flowable):
    """Bandeau coloré plein avec texte optionnel (couverture)."""

    def __init__(self, height, color=BLEU, width=CONTENT_W):
        super().__init__()
        self.height, self.color, self.width = height, color, width

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        self.canv.setFillColor(hexc(self.color))
        self.canv.rect(0, 0, self.width, self.height, stroke=0, fill=1)


class HLine(Flowable):
    def __init__(self, width=CONTENT_W, color="D0D7E2", thickness=0.8, space=2):
        super().__init__()
        self.width, self.color, self.thickness, self.space = width, color, thickness, space
        self.height = thickness + space

    def draw(self):
        self.canv.setStrokeColor(hexc(self.color))
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.space, self.width, self.space)


def _esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


TOKEN_RE = re.compile(r"\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)")


def _tokens(text):
    """Découpe un texte en (fragment, gras, url) ; gère **gras**, [libellé](url) et sauts de ligne."""
    out = []
    for li, line in enumerate(str(text).split("\n")):
        if li:
            out.append(("\n", False, None))
        pos = 0
        for m in TOKEN_RE.finditer(line):
            if m.start() > pos:
                out.append((line[pos:m.start()], False, None))
            if m.group(1) is not None:
                out.append((m.group(1), True, None))
            else:
                out.append((m.group(2), False, m.group(3)))
            pos = m.end()
        if pos < len(line):
            out.append((line[pos:], False, None))
    return out


def _rich_pdf(t):
    parts = []
    for frag, bold, url in _tokens(t):
        if frag == "\n":
            parts.append("<br/>")
        elif url:
            parts.append(f'<link href="{url}"><font color="#1F4E79"><u>{_esc(frag)}</u></font></link>')
        elif bold:
            parts.append(f"<b>{_esc(frag)}</b>")
        else:
            parts.append(_esc(frag))
    return "".join(parts)


def _add_docx_hyperlink(par, url, text, size=None, bold=False, color="1F4E79"):
    part = par.part
    r_id = part.relate_to(
        url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True)
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    if bold:
        rPr.append(OxmlElement("w:b"))
    col = OxmlElement("w:color")
    col.set(qn("w:val"), color)
    rPr.append(col)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    if size:
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), str(int(size * 2)))
        rPr.append(sz)
    run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    hl.append(run)
    par._p.append(hl)


def _rich_docx(par, text):
    size = None
    for frag, bold, url in _tokens(text):
        if frag == "\n":
            par.add_run().add_break()
        elif url:
            _add_docx_hyperlink(par, url, frag, size=size, bold=bold)
        else:
            r = par.add_run(frag)
            r.bold = bold


def _img_size(path, width_pt):
    with PILImage.open(path) as im:
        w, h = im.size
    return width_pt, width_pt * h / w


# --------------------------------------------------------------------------- #
# DOCX helpers
# --------------------------------------------------------------------------- #
def _shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def _cell_margins(table, top=40, bottom=40, left=80, right=80):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)


def _no_split(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    trPr.append(el)


def _field(par, code):
    r = par.add_run()
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), code)
    t = OxmlElement("w:t")
    t.text = "1"
    rr = OxmlElement("w:r")
    rr.append(t)
    fld.append(rr)
    r._r.addnext(fld)


# --------------------------------------------------------------------------- #
class Doc:
    def __init__(self, base, title, subtitle, meta, doc_ref, footer):
        self.base = base
        self.title = title
        self.subtitle = subtitle
        self.meta = meta
        self.doc_ref = doc_ref
        self.footer = footer

        self.story = []
        self.doc = Document()
        self._setup_docx()
        self._pdf_styles()
        self.first_h1 = True
        self.w_cm = 17.1
        self._just_broke = False
        self._land = False

    # ------------------------------------------------------------------ docx
    def _setup_docx(self):
        d = self.doc
        s = d.sections[0]
        s.page_width, s.page_height = Cm(21.0), Cm(29.7)
        s.left_margin = s.right_margin = Cm(1.9)
        s.top_margin = Cm(2.0)
        s.bottom_margin = Cm(1.7)
        s.header_distance = Cm(1.0)
        s.footer_distance = Cm(0.9)

        st = d.styles["Normal"]
        st.font.name = "Calibri"
        st.font.size = Pt(10)
        st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        pf = st.paragraph_format
        pf.space_after = Pt(4)
        pf.line_spacing = 1.12

        for name, size, color, before, after in (
                ("Heading 1", 17, BLEU, 12, 8),
                ("Heading 2", 12.5, BLEU, 12, 4),
                ("Heading 3", 10.5, BLEU_CLAIR, 8, 2)):
            h = d.styles[name]
            h.font.name = "Calibri"
            h.font.size = Pt(size)
            h.font.bold = True
            h.font.color.rgb = RGBColor.from_string(color)
            h.paragraph_format.space_before = Pt(before)
            h.paragraph_format.space_after = Pt(after)
            h.paragraph_format.keep_with_next = True
            h.font.italic = False

        # en-tête / pied
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = hp.add_run(self.doc_ref)
        r.font.size = Pt(7.5)
        r.font.color.rgb = RGBColor.from_string(GRIS)
        r.font.name = "Calibri"

        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run(self.footer + "   ·   page ")
        r.font.size = Pt(7.5)
        r.font.color.rgb = RGBColor.from_string(GRIS)
        _field(fp, "PAGE")
        for run in fp.runs:
            run.font.size = Pt(7.5)
            run.font.color.rgb = RGBColor.from_string(GRIS)
            run.font.name = "Calibri"

    # ------------------------------------------------------------------- pdf
    def _pdf_styles(self):
        self.ps = {
            "body": ParagraphStyle("body", fontName="DJ", fontSize=9.3, leading=13.4,
                                   alignment=TA_JUSTIFY, spaceAfter=5, textColor=colors.HexColor("#1A1A1A")),
            "lead": ParagraphStyle("lead", fontName="DJ", fontSize=10, leading=14.8,
                                   alignment=TA_JUSTIFY, spaceAfter=8, textColor=hexc("1A1A1A")),
            "h1": ParagraphStyle("h1", fontName="DJ-B", fontSize=15.5, leading=19, textColor=hexc(BLEU),
                                 spaceBefore=2, spaceAfter=9, keepWithNext=1),
            "h2": ParagraphStyle("h2", fontName="DJ-B", fontSize=11.4, leading=14.5,
                                 textColor=hexc(BLEU), spaceBefore=11, spaceAfter=5, keepWithNext=1),
            "h3": ParagraphStyle("h3", fontName="DJ-B", fontSize=9.8, leading=12.6,
                                 textColor=hexc(BLEU_CLAIR), spaceBefore=7, spaceAfter=3, keepWithNext=1),
            "bullet": ParagraphStyle("bullet", fontName="DJ", fontSize=9.2, leading=13.0,
                                     leftIndent=11, bulletIndent=2, spaceAfter=2.5,
                                     alignment=TA_LEFT, textColor=colors.HexColor("#1A1A1A")),
            "caption": ParagraphStyle("caption", fontName="DJ", fontSize=7.6, leading=10,
                                      textColor=hexc(GRIS), spaceBefore=3, spaceAfter=8,
                                      alignment=TA_LEFT),
            "cell": ParagraphStyle("cell", fontName="DJ", fontSize=7.9, leading=10.2),
            "cellb": ParagraphStyle("cellb", fontName="DJ-B", fontSize=7.9, leading=10.2),
            "cellh": ParagraphStyle("cellh", fontName="DJ-B", fontSize=7.9, leading=10.2,
                                    textColor=colors.white),
            "co_t": ParagraphStyle("co_t", fontName="DJ-B", fontSize=9.2, leading=12, spaceAfter=2.5),
            "co_b": ParagraphStyle("co_b", fontName="DJ", fontSize=8.8, leading=12.2),
            "cover_t": ParagraphStyle("cover_t", fontName="DJ-B", fontSize=25, leading=30,
                                      textColor=hexc(BLEU), alignment=TA_LEFT),
            "cover_s": ParagraphStyle("cover_s", fontName="DJ", fontSize=12.5, leading=18,
                                      textColor=hexc(GRIS)),
            "toc": ParagraphStyle("toc", fontName="DJ", fontSize=9.2, leading=15),
        }

    # ------------------------------------------------------------------ API
    def cover(self, eyebrow, title, subtitle, meta_rows, summary=None):
        # ---------- docx
        d = self.doc
        p = d.add_paragraph()
        p.paragraph_format.space_before = Pt(110)
        r = p.add_run(eyebrow.upper())
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor.from_string(ORANGE)
        r.font.name = "Calibri"

        p = d.add_paragraph()
        r = p.add_run(title)
        r.font.size = Pt(26)
        r.font.bold = True
        r.font.color.rgb = RGBColor.from_string(BLEU)
        r.font.name = "Calibri"
        p.paragraph_format.space_after = Pt(4)

        p = d.add_paragraph()
        r = p.add_run(subtitle)
        r.font.size = Pt(12.5)
        r.font.color.rgb = RGBColor.from_string(GRIS)
        p.paragraph_format.space_after = Pt(18)

        self.table([], meta_rows, widths=[4.2, 12.8], font=9, header=False, zebra=False,
                   _append=False)
        if summary:
            d.add_paragraph()
            self.callout(*summary, _append=False)
        d.add_page_break()

        # ---------- pdf
        st = self.ps
        s = [Spacer(1, 3.2 * cm), Band(0.30 * cm, ORANGE, width=3.2 * cm), Spacer(1, 0.55 * cm)]
        s.append(Paragraph(eyebrow.upper(), ParagraphStyle(
            "eb", fontName="DJ-B", fontSize=9, leading=11, textColor=hexc(ORANGE), spaceAfter=12)))
        s.append(Paragraph(_rich_pdf(title), st["cover_t"]))
        s.append(Spacer(1, 0.35 * cm))
        s.append(Paragraph(_rich_pdf(subtitle), st["cover_s"]))
        s.append(Spacer(1, 1.2 * cm))
        s.append(HLine())
        s.append(Spacer(1, 0.45 * cm))
        s.append(self._mk_table([], meta_rows, [4.2 * cm, 12.8 * cm], header=False, zebra=False, font=9))
        if summary:
            s.append(Spacer(1, 0.9 * cm))
            s.append(self._mk_callout(*summary))
        s.append(PageBreak())
        self.story.extend(s)

    def h1(self, num, text, newpage=True):
        if not self.first_h1:
            if self._just_broke:
                self._just_broke = False
            elif newpage:
                self.doc.add_page_break()
                self.story.append(PageBreak())
            else:
                from reportlab.platypus import CondPageBreak
                self.story.append(CondPageBreak(10 * cm))
        self.first_h1 = False
        p = self.doc.add_heading(f"{num}. {text}", level=1)
        for r in p.runs:
            r.font.size = Pt(17)
            r.font.color.rgb = RGBColor.from_string(BLEU)
            r.font.name = "Calibri"
        self.story.append(Paragraph(f"{num}. {_rich_pdf(text)}", self.ps["h1"]))
        self.story.append(HLine())

    def h1_plain(self, text):
        """Section sans numéro ni saut de page (ex. sommaire)."""
        p = self.doc.add_heading(text, level=1)
        for r in p.runs:
            r.font.size = Pt(15)
            r.font.color.rgb = RGBColor.from_string(BLEU)
        self.story.append(Paragraph(f"{_rich_pdf(text)}", self.ps["h1"]))
        self.story.append(HLine())

    def h2(self, text):
        p = self.doc.add_heading(text, level=2)
        for r in p.runs:
            r.font.size = Pt(12.5)
        self.story.append(Paragraph(_rich_pdf(text), self.ps["h2"]))

    def h3(self, text):
        p = self.doc.add_heading(text, level=3)
        for r in p.runs:
            r.font.size = Pt(10.5)
        self.story.append(Paragraph(_rich_pdf(text), self.ps["h3"]))

    def p(self, text, lead=False, small=False, italic=False, center=False):
        par = self.doc.add_paragraph()
        _rich_docx(par, text)
        for r in par.runs:
            r.font.size = Pt(10.5 if lead else (8.5 if small else 10))
            r.italic = italic
            if small:
                r.font.color.rgb = RGBColor.from_string(GRIS)
        if center:
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if lead:
            par.paragraph_format.space_after = Pt(6)
        key = "lead" if lead else "body"
        st = self.ps[key] if not small else self.ps["caption"]
        if italic and not small:
            st = ParagraphStyle("it", parent=st, fontName="DJ")
        self.story.append(Paragraph(_rich_pdf(text), st))
        self.story.append(Spacer(1, 1 if small else 0))

    def ul(self, items, numbered=False):
        for i, it in enumerate(items, 1):
            par = self.doc.add_paragraph(style="List Number" if numbered else "List Bullet")
            _rich_docx(par, it)
            for r in par.runs:
                r.font.size = Pt(10)
            par.paragraph_format.space_after = Pt(2)
            par.paragraph_format.left_indent = Cm(0.6)
            par.paragraph_format.first_line_indent = Cm(-0.35)
            bullet = f"{i}." if numbered else "•"
            self.story.append(Paragraph(_rich_pdf(it), self.ps["bullet"], bulletText=bullet))

    def table(self, headers, rows, widths, font=8.4, caption=None, header=True,
              zebra=True, aligns=None, header_bg=BLEU, row_bg=None, first_col_bold=False,
              cell_fmt=None, _append=True):
        """widths : liste de largeurs relatives (cm sur 17 cm utiles)."""
        # ---------------- docx
        d = self.doc
        ncols = len(widths)
        t = d.add_table(rows=0, cols=ncols)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        _cell_margins(t)
        total = sum(widths)
        scale = self.w_cm / total
        cell_fmt = cell_fmt or {}

        if header and headers:
            cells = t.add_row().cells
            _no_split(t.rows[-1])
            for j, h in enumerate(headers):
                c = cells[j]
                c.width = Cm(widths[j] * scale)
                _shade(c, header_bg)
                par = c.paragraphs[0]
                par.paragraph_format.space_after = Pt(1)
                par.paragraph_format.space_before = Pt(1)
                r = par.add_run(h)
                r.bold = True
                r.font.size = Pt(font)
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.name = "Calibri"
                if aligns and aligns[j] == "r":
                    par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                elif aligns and aligns[j] == "c":
                    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for i, row in enumerate(rows):
            cells = t.add_row().cells
            _no_split(t.rows[-1])
            for j, val in enumerate(row):
                c = cells[j]
                c.width = Cm(widths[j] * scale)
                par = c.paragraphs[0]
                par.paragraph_format.space_after = Pt(1)
                par.paragraph_format.space_before = Pt(1)
                _rich_docx(par, str(val))
                for r in par.runs:
                    r.font.size = Pt(font)
                    r.font.name = "Calibri"
                    if j == 0 and first_col_bold:
                        r.bold = True
                if aligns and aligns[j] == "r":
                    par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                elif aligns and aligns[j] == "c":
                    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                fmt = cell_fmt.get((i, j), {})
                if fmt.get("bg"):
                    _shade(c, fmt["bg"])
                elif row_bg and i in row_bg:
                    _shade(c, row_bg[i])
                elif zebra and i % 2 == 1:
                    _shade(c, GRIS_CLAIR)
                for r in par.runs:
                    if fmt.get("color"):
                        r.font.color.rgb = RGBColor.from_string(fmt["color"])
                    if fmt.get("b"):
                        r.bold = True
                    if fmt.get("i"):
                        r.italic = True
        if caption:
            cp = d.add_paragraph()
            r = cp.add_run(caption)
            r.font.size = Pt(8)
            r.italic = True
            r.font.color.rgb = RGBColor.from_string(GRIS)
            cp.paragraph_format.space_after = Pt(8)
        else:
            d.add_paragraph().paragraph_format.space_after = Pt(4)

        # ---------------- pdf
        if not _append:
            return
        self.story.append(self._mk_table(headers, rows, [w * scale * cm for w in widths],
                                         header=header, zebra=zebra, font=font, aligns=aligns,
                                         header_bg=header_bg, row_bg=row_bg,
                                         first_col_bold=first_col_bold, cell_fmt=cell_fmt))
        if caption:
            self.story.append(Paragraph(_rich_pdf(caption), self.ps["caption"]))
        else:
            self.story.append(Spacer(1, 0.25 * cm))

    def _mk_table(self, headers, rows, widths_cm_list, header=True, zebra=True, font=8.4,
                  aligns=None, header_bg=BLEU, row_bg=None, first_col_bold=False, cell_fmt=None):
        st_cell = ParagraphStyle("c", parent=self.ps["cell"], fontSize=font, leading=font * 1.28)
        st_cellb = ParagraphStyle("cb", parent=self.ps["cellb"], fontSize=font, leading=font * 1.28)
        st_head = ParagraphStyle("ch", parent=self.ps["cellh"], fontSize=font, leading=font * 1.28)
        data = []
        if header and headers:
            data.append([Paragraph(_rich_pdf(str(h)), st_head) for h in headers])
        for i, row in enumerate(rows):
            line = []
            for j, v in enumerate(row):
                style = st_cellb if (j == 0 and first_col_bold) else st_cell
                al = ALIGN = 0
                if aligns and aligns[j] == "r":
                    al = 2
                elif aligns and aligns[j] == "c":
                    al = 1
                fmt = (cell_fmt or {}).get((i, j), {})
                s3 = ParagraphStyle(
                    f"c{j}_{i}", parent=style, alignment=al,
                    fontName="DJ-B" if fmt.get("b") else "DJ",
                    textColor=hexc(fmt["color"]) if fmt.get("color") else colors.HexColor("#1A1A1A"))
                line.append(Paragraph(_rich_pdf(str(v)), s3))
            data.append(line)
        t = Table(data, colWidths=widths_cm_list, repeatRows=1 if (header and headers) else 0)
        cmds = [
            ("GRID", (0, 0), (-1, -1), 0.4, hexc("C9D2DE")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 2.6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
            ("LEFTPADDING", (0, 0), (-1, -1), 3.4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3.4),
        ]
        if header and headers:
            cmds.append(("BACKGROUND", (0, 0), (-1, 0), hexc(header_bg)))
        if zebra:
            for i in range(1 if (header and headers) else 0, len(data)):
                if i % 2 == 0:
                    cmds.append(("BACKGROUND", (0, i), (-1, i), hexc(GRIS_CLAIR)))
        if row_bg:
            for i, bg in row_bg.items():
                idx = i + (1 if (header and headers) else 0)
                cmds.append(("BACKGROUND", (0, idx), (-1, idx), hexc(bg)))
        if cell_fmt:
            off = 1 if (header and headers) else 0
            for (i, j), fmt in cell_fmt.items():
                if fmt.get("bg"):
                    cmds.append(("BACKGROUND", (j, i + off), (j, i + off), hexc(fmt["bg"])))
        t.setStyle(TableStyle(cmds))
        return t

    def image(self, name, caption=None, width_cm=16.8):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", name)
        # docx
        self.doc.add_picture(path, width=Cm(width_cm))
        self.doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        if caption:
            cp = self.doc.add_paragraph()
            cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = cp.add_run(caption)
            r.font.size = Pt(8)
            r.italic = True
            r.font.color.rgb = RGBColor.from_string(GRIS)
            cp.paragraph_format.space_after = Pt(10)
        # pdf
        w, h = _img_size(path, width_cm * cm)
        self.story.append(Spacer(1, 0.2 * cm))
        self.story.append(Image(path, width=w, height=h))
        if caption:
            self.story.append(Paragraph(_rich_pdf(caption), ParagraphStyle(
                "capc", parent=self.ps["caption"], alignment=TA_CENTER, spaceBefore=3, spaceAfter=10)))
        else:
            self.story.append(Spacer(1, 0.3 * cm))

    def callout(self, title, body, kind="info", _append=True):
        bg = {"info": FOND_BLEU, "warn": FOND_ORANGE, "ok": FOND_VERT, "bad": FOND_ROUGE}[kind]
        bar = {"info": BLEU, "warn": ORANGE, "ok": VERT, "bad": ROUGE}[kind]
        # docx
        t = self.doc.add_table(rows=1, cols=1)
        t.autofit = False
        _cell_margins(t, top=90, bottom=90, left=140, right=140)
        c = t.rows[0].cells[0]
        c.width = Cm(17.1)
        _shade(c, bg)
        par = c.paragraphs[0]
        r = par.add_run(title)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor.from_string(bar)
        par.paragraph_format.space_after = Pt(2)
        for line in body.split("\n"):
            p2 = c.add_paragraph()
            _rich_docx(p2, line)
            for r in p2.runs:
                r.font.size = Pt(9)
            p2.paragraph_format.space_after = Pt(1)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(3)
        # pdf
        if _append:
            self.story.append(self._mk_callout(title, body, kind))

    def _mk_callout(self, title, body, kind="info"):
        bg = {"info": FOND_BLEU, "warn": FOND_ORANGE, "ok": FOND_VERT, "bad": FOND_ROUGE}[kind]
        bar = {"info": BLEU, "warn": ORANGE, "ok": VERT, "bad": ROUGE}[kind]
        inner = [Paragraph(_rich_pdf(title), ParagraphStyle(
            "cot", parent=self.ps["co_t"], textColor=hexc(bar)))]
        for line in body.split("\n"):
            inner.append(Paragraph(_rich_pdf(line), self.ps["co_b"]))
        t = Table([[""]] + [[inner]], colWidths=[CONTENT_W])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 1), (0, 1), hexc(bg)),
            ("LINEBEFORE", (0, 1), (0, 1), 2.6, hexc(bar)),
            ("LEFTPADDING", (0, 1), (0, 1), 7),
            ("RIGHTPADDING", (0, 1), (0, 1), 6),
            ("TOPPADDING", (0, 1), (0, 1), 5),
            ("BOTTOMPADDING", (0, 1), (0, 1), 5),
            ("TOPPADDING", (0, 0), (0, 0), 0),
            ("BOTTOMPADDING", (0, 0), (0, 0), 0),
            ("LEFTPADDING", (0, 0), (0, 0), 0),
            ("RIGHTPADDING", (0, 0), (0, 0), 0),
            ("SPAN", (0, 0), (0, 0)),
        ]))
        return KeepTogether([Spacer(1, 0.22 * cm), t, Spacer(1, 0.22 * cm)])

    def kpi(self, items):
        """items = [(valeur, libellé), ...] -> rangée d'indicateurs."""
        n = len(items)
        # docx
        t = self.doc.add_table(rows=2, cols=n)
        t.autofit = False
        _cell_margins(t, top=70, bottom=70, left=90, right=90)
        for j, (val, lab) in enumerate(items):
            for i in (0, 1):
                c = t.rows[i].cells[j]
                c.width = Cm(17.1 / n)
                _shade(c, FOND_BLEU)
            p0 = t.rows[0].cells[j].paragraphs[0]
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p0.add_run(val)
            r.bold = True
            r.font.size = Pt(15)
            r.font.color.rgb = RGBColor.from_string(BLEU)
            p1 = t.rows[1].cells[j].paragraphs[0]
            p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p1.add_run(lab)
            r.font.size = Pt(8)
            r.font.color.rgb = RGBColor.from_string(GRIS)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(2)
        # pdf
        data = [[Paragraph(f'<b>{_esc(v)}</b>', ParagraphStyle(
                    "kv", fontName="DJ-B", fontSize=15, leading=19, alignment=TA_CENTER,
                    textColor=hexc(BLEU))) for v, _ in items],
                [Paragraph(_esc(l), ParagraphStyle(
                    "kl", fontName="DJ", fontSize=7.4, leading=9.4, alignment=TA_CENTER,
                    textColor=hexc(GRIS))) for _, l in items]]
        t2 = Table(data, colWidths=[CONTENT_W / n] * n)
        t2.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), hexc(FOND_BLEU)),
            ("BOX", (0, 0), (-1, -1), 0.4, hexc("C9D2DE")),
            ("INNERGRID", (0, 0), (-1, -1), 0.4, hexc("FFFFFF")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, 0), 6),
            ("BOTTOMPADDING", (0, 1), (-1, 1), 6),
            ("TOPPADDING", (0, 1), (-1, 1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 1),
        ]))
        self.story.append(t2)
        self.story.append(Spacer(1, 0.28 * cm))

    def landscape(self, on=True):
        """Bascule en paysage (ou revient en portrait) : les tableaux larges y respirent."""
        if on == self._land:
            return
        self._land = on
        if on:
            sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
            sec.orientation = WD_ORIENT.LANDSCAPE
            sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
            sec.left_margin = sec.right_margin = Cm(1.9)
            sec.top_margin, sec.bottom_margin = Cm(1.9), Cm(1.6)
            self.story.append(NextPageTemplate("land"))
            self.story.append(PageBreak())
            self.w_cm = 25.9
        else:
            sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
            sec.orientation = WD_ORIENT.PORTRAIT
            sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
            sec.left_margin = sec.right_margin = Cm(1.9)
            sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(1.7)
            self.story.append(NextPageTemplate("portrait"))
            self.story.append(PageBreak())
            self.w_cm = 17.1
        self._just_broke = True

    def pagebreak(self):
        self.doc.add_page_break()
        self.story.append(PageBreak())

    def spacer(self, cm_h=0.3):
        self.doc.add_paragraph().paragraph_format.space_after = Pt(cm_h * 28 / 2)
        self.story.append(Spacer(1, cm_h * cm))

    # ------------------------------------------------------------------ save
    def save(self, outdir):
        os.makedirs(outdir, exist_ok=True)
        # DOCX
        dpath = os.path.join(outdir, self.base + ".docx")
        self.doc.save(dpath)
        # PDF
        ppath = os.path.join(outdir, self.base + ".pdf")

        def on_page(canv, doc):
            canv.saveState()
            pw, ph = canv._pagesize
            right = pw - M_R
            if doc.page > 1:
                canv.setFont("DJ", 7.2)
                canv.setFillColor(hexc(GRIS))
                canv.drawString(M_L, ph - 1.25 * cm, self.doc_ref)
                canv.drawRightString(right, ph - 1.25 * cm, self.title)
                canv.setStrokeColor(hexc("D0D7E2"))
                canv.setLineWidth(0.5)
                canv.line(M_L, ph - 1.45 * cm, right, ph - 1.45 * cm)
            canv.setFont("DJ", 7.2)
            canv.setFillColor(hexc(GRIS))
            canv.drawCentredString(pw / 2, 1.02 * cm, f"{self.footer}   ·   page {doc.page}")
            canv.setStrokeColor(hexc("D0D7E2"))
            canv.line(M_L, 1.3 * cm, right, 1.3 * cm)
            canv.restoreState()

        class _Doc(BaseDocTemplate):
            def __init__(self, *a, **k):
                BaseDocTemplate.__init__(self, *a, **k)
                self._bk = 0

            def afterFlowable(self, flowable):
                if isinstance(flowable, Paragraph) and flowable.style.name in ("h1", "h2"):
                    self._bk += 1
                    key = f"sec{self._bk}"
                    txt = flowable.getPlainText()
                    self.canv.bookmarkPage(key)
                    self.canv.addOutlineEntry(txt, key, level=0 if flowable.style.name == "h1" else 1,
                                              closed=False)

        docpdf = _Doc(ppath, pagesize=A4,
                                 leftMargin=M_L, rightMargin=M_R,
                                 topMargin=M_T, bottomMargin=M_B,
                                 title=self.title, author="GED-SERVICES",
                                 subject=self.subtitle)
        frame = Frame(M_L, M_B, CONTENT_W, PAGE_H - M_T - M_B, id="f", showBoundary=0)
        LW, LH = landscape(A4)
        frame_l = Frame(M_L, 1.6 * cm, LW - M_L - M_R, LH - 1.9 * cm - 1.6 * cm,
                        id="fl", showBoundary=0)
        docpdf.addPageTemplates([
            PageTemplate(id="portrait", frames=[frame], onPage=on_page, pagesize=A4),
            PageTemplate(id="land", frames=[frame_l], onPage=on_page, pagesize=landscape(A4)),
        ])
        docpdf.build(self.story)
        return dpath, ppath

"""Export the six interview Markdown documents and render previews for review.

Run from the repository with: .venv/Scripts/python.exe scripts/export_interview_pdfs.py
PDFs go to output/pdf; temporary QA files go to tmp/pdfs.
An open PDF is preserved and a numbered version is written instead.
"""

from pathlib import Path
import html
import json
import math
import re

import pymupdf
from markdown_it import MarkdownIt
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    LongTable,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/pdf"
PREVIEW = ROOT / "tmp/pdfs/preview"
OUT.mkdir(parents=True, exist_ok=True)
PREVIEW.mkdir(parents=True, exist_ok=True)
PW, PH = A4
WIDTH = PW - 96
BLUE, INK, MUTED, PALE, LINE = [
    colors.HexColor(c) for c in ("#175475", "#172738", "#627384", "#f0f5f9", "#d9e3eb")
]
for name, file in [
    ("Body", "arial.ttf"),
    ("Body-Bold", "arialbd.ttf"),
    ("Body-Italic", "ariali.ttf"),
    ("Body-BoldItalic", "arialbi.ttf"),
    ("Code", "consola.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, "C:/Windows/Fonts/" + file))
pdfmetrics.registerFontFamily(
    "Body", normal="Body", bold="Body-Bold", italic="Body-Italic", boldItalic="Body-BoldItalic"
)
BODY = ParagraphStyle(
    "body",
    fontName="Body",
    fontSize=9.5,
    leading=13.3,
    textColor=INK,
    spaceAfter=7,
    allowWidows=0,
    allowOrphans=0,
)
HEAD = {
    level: ParagraphStyle(
        "h" + str(level),
        parent=BODY,
        fontName="Body-Bold",
        fontSize=size,
        leading=leading,
        spaceBefore=before,
        spaceAfter=after,
        textColor=BLUE,
    )
    for level, size, leading, before, after in (
        (1, 23, 28, 0, 17),
        (2, 15, 19, 17, 9),
        (3, 11.6, 15.5, 12, 7),
        (4, 10.4, 14, 10, 6),
    )
}
QUOTE = ParagraphStyle(
    "quote",
    parent=BODY,
    leftIndent=12,
    rightIndent=8,
    backColor=PALE,
    borderColor=LINE,
    borderWidth=0.4,
    borderPadding=8,
    spaceBefore=7,
    spaceAfter=12,
)
CELL = ParagraphStyle("cell", parent=BODY, fontSize=8.5, leading=11.5, spaceAfter=0)
CELLHEAD = ParagraphStyle(
    "cellhead", parent=CELL, fontName="Body-Bold", fontSize=8.3, leading=11, textColor=colors.white
)
CODE = ParagraphStyle(
    "code",
    fontName="Code",
    fontSize=8.1,
    leading=11.1,
    textColor=INK,
    leftIndent=9,
    rightIndent=9,
    backColor=PALE,
    borderColor=LINE,
    borderWidth=0.4,
    borderPadding=9,
    spaceBefore=7,
    spaceAfter=13,
)
MD = MarkdownIt("commonmark", {"html": False}).enable("table")
FILES = [
    ("data_platform_engineer_devops_60min", "INTERVIEW GUIDE", "PLAN ROZMOWY"),
    ("zadanie_python_dla_kandydata", "PYTHON EXERCISES", "ZADANIA PYTHON"),
    ("example_answers_aws_data_platform_devops", "EXAMPLE ANSWERS", "PRZYKŁADOWE ODPOWIEDZI"),
]


def output_path(stem):
    """Select a writable path without truncating or changing an existing file."""
    version = 1
    while True:
        suffix = "" if version == 1 else f"_v{version}"
        path = OUT / f"{stem}{suffix}.pdf"
        if not path.exists():
            return path
        try:
            with path.open("r+b"):
                pass
            return path
        except PermissionError:
            version += 1


TARGETS = {
    base + suffix: output_path(base + suffix) for base, _, _ in FILES for suffix in ("", "_pl")
}


def norm(s):
    return re.sub("[\u2010-\u2014\u2212]", "-", s).replace("\xa0", " ")


class WholeParagraph(Paragraph):
    def split(self, *args, **kwargs):
        return []


class WholeCode(Preformatted):
    def split(self, *args, **kwargs):
        return []


def inline(children):
    parts = []
    for t in children or []:
        if t.type == "text":
            parts.append(html.escape(norm(t.content)))
        elif t.type == "code_inline":
            parts.append('<font name="Code">' + html.escape(norm(t.content)) + "</font>")
        elif t.type == "strong_open":
            parts.append("<b>")
        elif t.type == "strong_close":
            parts.append("</b>")
        elif t.type == "em_open":
            parts.append("<i>")
        elif t.type == "em_close":
            parts.append("</i>")
        elif t.type == "softbreak":
            parts.append(" ")
        elif t.type == "hardbreak":
            parts.append("<br/>")
        elif t.type == "link_open":
            url = t.attrGet("href")
            if url.endswith(".md"):
                stem = Path(url).stem
                url = TARGETS[stem].name if stem in TARGETS else Path(url).with_suffix(".pdf").name
            parts.append('<link href="' + html.escape(url, quote=True) + '" color="#175475">')
        elif t.type == "link_close":
            parts.append("</link>")
    return "".join(parts)


def colwidths(raw):
    n = len(raw[0])
    first = raw[0][0].lower()
    if n == 3 and first in ("minutes", "minuty"):
        return [50, 146, WIDTH - 196]
    if n == 4 and ("waga" in raw[0][1].lower() or "weight" in raw[0][1].lower()):
        return [157, 63, 67, WIDTH - 287]
    if n == 2 and first in ("rating", "ocena"):
        return [54, WIDTH - 54]
    base = 63 if n >= 3 else 90
    weights = []
    for col in zip(*raw):
        lengths = [len(s) for s in col]
        weights.append(math.sqrt(sum(lengths) / len(lengths) + 0.25 * min(max(lengths), 180)))
    return [base + (WIDTH - n * base) * w / sum(weights) for w in weights]


def build_story(source, candidate):
    tokens = MD.parse(source)
    items = []
    lists = []
    quote = 0
    at_item = False
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.type in ("bullet_list_open", "ordered_list_open"):
            lists.append([t.type, int(t.attrGet("start") or 1)])
        elif t.type in ("bullet_list_close", "ordered_list_close"):
            lists.pop()
        elif t.type == "list_item_open":
            at_item = True
        elif t.type == "blockquote_open":
            quote += 1
        elif t.type == "blockquote_close":
            quote -= 1
        elif t.type == "heading_open":
            level = int(t.tag[1:])
            content = tokens[i + 1]
            if candidate and content.content.startswith(("Exercise 2", "Zadanie 2")):
                items.append(PageBreak())
            p = WholeParagraph(inline(content.children), HEAD[min(level, 4)])
            p.heading = (level, norm(content.content))
            p.attach_next = True
            items.append(p)
            i += 2
        elif t.type == "paragraph_open":
            content = tokens[i + 1]
            style = QUOTE if quote else BODY
            bullet = None
            if lists:
                style = ParagraphStyle(
                    "list",
                    parent=style,
                    leftIndent=14 * len(lists),
                    firstLineIndent=0,
                    bulletIndent=14 * (len(lists) - 1),
                    spaceAfter=5,
                )
                if at_item:
                    bullet = "-" if lists[-1][0] == "bullet_list_open" else str(lists[-1][1]) + "."
                    if lists[-1][0] == "ordered_list_open":
                        lists[-1][1] += 1
                    at_item = False
            p = (WholeParagraph if quote else Paragraph)(
                inline(content.children), style, bulletText=bullet
            )
            children = [c for c in content.children or [] if c.type != "text" or c.content]
            fullbold = (
                children
                and children[0].type == "strong_open"
                and children[-1].type == "strong_close"
            )
            nexttype = tokens[i + 3].type if i + 3 < len(tokens) else ""
            if fullbold or nexttype == "table_open":
                p.attach_next = True
            items.append(p)
            i += 2
        elif t.type in ("fence", "code_block"):
            code = norm(t.content.rstrip("\n"))
            style = CODE
            w = max(
                (pdfmetrics.stringWidth(line, "Code", CODE.fontSize) for line in code.splitlines()),
                default=0,
            )
            if w > WIDTH - 22:
                style = ParagraphStyle(
                    "smallcode", parent=CODE, fontSize=CODE.fontSize * (WIDTH - 22) / w
                )
            items.append(WholeCode(code, style))
        elif t.type == "table_open":
            rows = []
            raw = []
            i += 1
            while tokens[i].type != "table_close":
                tt = tokens[i]
                if tt.type == "tr_open":
                    row = []
                    rawrow = []
                elif tt.type in ("th_open", "td_open"):
                    content = tokens[i + 1]
                    row.append(
                        Paragraph(
                            inline(content.children), CELLHEAD if tt.type == "th_open" else CELL
                        )
                    )
                    rawrow.append(norm(content.content))
                elif tt.type == "tr_close":
                    rows.append(row)
                    raw.append(rawrow)
                i += 1
            table = LongTable(
                rows,
                colWidths=colwidths(raw),
                repeatRows=1,
                splitInRow=1,
                hAlign="LEFT",
                spaceBefore=5,
                spaceAfter=13,
            )
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
                        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 8),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                        ("TOPPADDING", (0, 0), (-1, -1), 7),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
                    ]
                )
            )
            table.small_table = table.wrap(WIDTH, PH)[1] <= 340
            items.append(table)
        elif t.type == "hr":
            items.append(HRFlowable(width="100%", color=LINE))
        i += 1
    result = []
    i = 0
    while i < len(items):
        if getattr(items[i], "attach_next", False):
            group = [items[i]]
            while getattr(group[-1], "attach_next", False) and i + 1 < len(items):
                i += 1
                group.append(items[i])
            result.append(KeepTogether(group))
        elif getattr(items[i], "small_table", False):
            result.append(KeepTogether([items[i]]))
        else:
            result.append(items[i])
        i += 1
    return result


class Document(BaseDocTemplate):
    def afterFlowable(self, f):
        if hasattr(f, "heading"):
            level, title = f.heading
            key = "h-" + str(self.seq.nextf("heading"))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=level - 1, closed=False)


def page_template(label, footer, pl):
    def draw(c, doc):
        c.saveState()
        c.setFont("Body-Bold", 7.3)
        c.setFillColor(MUTED)
        c.drawString(48, PH - 25, label)
        c.setFont("Body", 7.3)
        c.drawRightString(PW - 48, PH - 25, "AWS DATA PLATFORM / DEVOPS" + (" · PL" if pl else ""))
        c.setStrokeColor(LINE)
        c.setLineWidth(0.5)
        c.line(48, PH - 36, PW - 48, PH - 36)
        c.line(48, 33, PW - 48, 33)
        c.drawString(48, 21, footer)
        c.drawRightString(PW - 48, 21, ("Strona " if pl else "Page ") + str(doc.page))
        c.restoreState()

    return draw


def main():
    results = []
    for base, enlabel, pllabel in FILES:
        for pl in (False, True):
            stem = base + ("_pl" if pl else "")
            source = (ROOT / "plany_rozmow" / f"{stem}.md").read_text(encoding="utf-8")
            target = TARGETS[stem]
            title = norm(MD.parse(source)[1].content)
            candidate = base == "zadanie_python_dla_kandydata"
            footer = (
                ("Arkusz kandydata" if candidate else "Materiał dla prowadzącego")
                if pl
                else ("Candidate handout" if candidate else "Interviewer reference")
            )
            doc = Document(
                str(target),
                pagesize=A4,
                leftMargin=48,
                rightMargin=48,
                topMargin=49,
                bottomMargin=43,
                title=title,
                author="Interview materials",
            )
            frame = Frame(
                48, 43, WIDTH, PH - 92, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0
            )
            doc.addPageTemplates(
                PageTemplate(
                    id="main",
                    frames=frame,
                    onPage=page_template(pllabel if pl else enlabel, footer, pl),
                )
            )
            doc.build(build_story(source, candidate))
            pdf = pymupdf.open(target)
            text = "\n".join(p.get_text() for p in pdf)
            tokens = MD.parse(source)
            flat = re.sub(r"\s+", " ", text)
            missing = [
                norm(tokens[i + 1].content)
                for i, t in enumerate(tokens)
                if t.type == "heading_open"
                and re.sub(r"\s+", " ", norm(tokens[i + 1].content)) not in flat
            ]
            visible = []
            for t in tokens:
                if t.type == "inline":
                    visible.extend(
                        c.content for c in t.children or [] if c.type in ("text", "code_inline")
                    )
                elif t.type in ("fence", "code_block"):
                    visible.append(t.content)
            words = lambda s: set(re.findall(r"[^\W\d]\w*", s.lower(), re.UNICODE))
            missingwords = sorted(words(norm(" ".join(visible))) - words(text))
            bounds = []
            badlinks = []
            for page_no, page in enumerate(pdf, 1):
                for b in page.get_text("blocks"):
                    if b[4].strip() and (
                        b[0] < 35 or b[2] > PW - 35 or b[1] < 12 or b[3] > PH - 12
                    ):
                        bounds.append([page_no, b[:4], b[4][:80]])
                for link in page.get_links():
                    uri = link.get("uri", "") or link.get("file", "")
                    planned_names = {p.name for p in TARGETS.values()}
                    if uri.endswith(".md") or (
                        uri.endswith(".pdf")
                        and Path(uri).name not in planned_names
                        and not (OUT / Path(uri).name).exists()
                    ):
                        badlinks.append(uri)
                page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(
                    PREVIEW / f"{stem}_{page_no:02}.png"
                )
            sheet = Image.new("RGB", (1050, math.ceil(len(pdf) / 3) * 500), "#e5eaf0")
            draw = ImageDraw.Draw(sheet)
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
            for idx in range(len(pdf)):
                with Image.open(PREVIEW / f"{stem}_{idx + 1:02}.png") as im:
                    im.thumbnail((330, 467))
                    x = (idx % 3) * 350 + 10
                    y = (idx // 3) * 500 + 24
                    sheet.paste(im, (x, y))
                    draw.text((x, y - 20), f"Page {idx + 1}", font=font, fill="#172738")
            sheet.save(PREVIEW / f"{stem}_contact.png")
            results.append(
                dict(
                    file=target.name,
                    pages=len(pdf),
                    bytes=target.stat().st_size,
                    missing_headings=missing,
                    missing_words=missingwords,
                    bounds_issues=bounds,
                    bad_links=badlinks,
                )
            )
            pdf.close()
    assert all(path.is_file() for path in TARGETS.values())
    (ROOT / "tmp/pdfs/qa.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(results, ensure_ascii=False, indent=2))
    assert not any(
        r["missing_headings"] or r["missing_words"] or r["bounds_issues"] or r["bad_links"]
        for r in results
    )


if __name__ == "__main__":
    main()

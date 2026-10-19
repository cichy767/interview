"""Build only the Polish interviewer handbook, with a linked table of contents."""

import html
import json
import math
import re

import pymupdf
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import CondPageBreak, Frame, PageBreak, PageTemplate, Paragraph, Spacer
from reportlab.platypus.tableofcontents import TableOfContents

import export_interview_pdfs as base


STEM = "przewodnik_dla_prowadzacego_aws_devops_pl"


class Handbook(base.Document):
    def afterFlowable(self, flowable):
        if not hasattr(flowable, "heading"):
            return
        level, title = flowable.heading
        key = "handbook-" + str(self.seq.nextf("handbook-heading"))
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(title, key, level=level - 1, closed=level > 1)
        if level == 2:
            self.notify("TOCEntry", (0, html.escape(title), self.page, key))


def heading(flowable):
    if hasattr(flowable, "heading"):
        return flowable.heading
    children = getattr(flowable, "_content", [])
    return heading(children[0]) if children else None


def main(
    stem=STEM,
    *,
    title="O co pytam na rozmowie? Przewodnik AWS DevOps dla prowadzącego",
    subject="Wyjaśnienie pojęć z Q1-Q6, zadań Python i pytań rezerwowych",
    header="PRZEWODNIK DLA PROWADZĄCEGO",
    footer="Wyjaśnienia pojęć i sensu pytań",
    expected_chapters=18,
    force_page_break_before=(),
    companion_paths=None,
):
    source = (base.ROOT / "plany_rozmow" / f"{stem}.md").read_text(encoding="utf-8")
    target = base.output_path(stem)
    # This export reads companion PDFs; it does not create their next versions.
    companion_paths = companion_paths or {}
    base.TARGETS = {
        stem: companion_paths.get(stem, base.OUT / f"{stem}.pdf") for stem in base.TARGETS
    }
    base.BODY.fontSize = 10.5
    base.BODY.leading = 14.5
    base.BODY.spaceAfter = 8
    base.QUOTE.fontSize = 10.3
    base.QUOTE.leading = 14.5
    base.CELL.fontSize = 9.1
    base.CELL.leading = 12.6
    base.CELLHEAD.fontSize = 9
    base.CELLHEAD.leading = 12
    base.HEAD[3].fontSize = 12
    base.HEAD[3].leading = 16
    base.CODE.fontSize = 8.8
    base.CODE.leading = 12.5
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "contents-entry",
            fontName="Body",
            fontSize=9.7,
            leading=12.5,
            textColor=base.INK,
            leftIndent=0,
            firstLineIndent=0,
            spaceBefore=0,
            rightIndent=25,
        )
    ]
    story = []
    contents_added = False
    for flowable in base.build_story(source, candidate=False):
        entry = heading(flowable)
        if entry and entry[0] == 2:
            if not contents_added:
                story.extend(
                    [
                        Spacer(1, 8),
                        Paragraph("Spis treści", base.HEAD[2]),
                        toc,
                    ]
                )
                contents_added = True
                story.append(PageBreak())
            else:
                story.append(
                    PageBreak()
                    if entry[1].startswith(force_page_break_before)
                    else CondPageBreak(190)
                )
        story.append(flowable)
    doc = Handbook(
        str(target),
        pagesize=base.A4,
        leftMargin=48,
        rightMargin=48,
        topMargin=49,
        bottomMargin=43,
        title=title,
        author="Materiały do przygotowania rozmowy",
        subject=subject,
    )
    frame = Frame(
        48,
        43,
        base.WIDTH,
        base.PH - 92,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates(
        PageTemplate(
            id="handbook",
            frames=frame,
            onPage=base.page_template(header, footer, True),
        )
    )
    doc.multiBuild(story)
    pdf = pymupdf.open(target)
    text = "\n".join(page.get_text() for page in pdf)
    flat = re.sub(r"\s+", " ", text)
    tokens = base.MD.parse(source)
    expected_headings = [
        base.norm(tokens[idx + 1].content)
        for idx, token in enumerate(tokens)
        if token.type == "heading_open"
    ]
    missing_headings = [h for h in expected_headings if re.sub(r"\s+", " ", h) not in flat]
    visible = []
    for token in tokens:
        if token.type == "inline":
            visible.extend(
                child.content
                for child in token.children or []
                if child.type in ("text", "code_inline")
            )
        elif token.type in ("fence", "code_block"):
            visible.append(token.content)
    words = lambda value: set(re.findall(r"[^\W\d]\w*", value.lower(), re.UNICODE))
    missing_words = sorted(words(base.norm(" ".join(visible))) - words(text))
    bounds = []
    bad_links = []
    chapter_pages = []
    image_paths = []
    for page_no, page in enumerate(pdf, 1):
        for block in page.get_text("blocks"):
            if block[4].strip() and (
                block[0] < 35 or block[2] > base.PW - 35 or block[1] < 12 or block[3] > base.PH - 12
            ):
                bounds.append([page_no, block[:4], block[4][:80]])
        for link in page.get_links():
            uri = link.get("file", "") or link.get("uri", "")
            if uri.endswith(".md"):
                bad_links.append(uri)
            elif uri.endswith(".pdf") and not (base.OUT / uri).is_file():
                bad_links.append(uri)
        image_path = base.PREVIEW / f"{stem}_{page_no:02}.png"
        page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(image_path)
        image_paths.append(image_path)
    for level, title, page_no in pdf.get_toc():
        if level == 2:
            chapter_pages.append({"title": title, "page": page_no})
    # Several sheets keep all pages legible in visual review.
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
    for start in range(0, len(pdf), 9):
        count = min(9, len(pdf) - start)
        sheet = Image.new("RGB", (1050, math.ceil(count / 3) * 500), "#e5eaf0")
        draw = ImageDraw.Draw(sheet)
        for offset in range(count):
            index = start + offset
            with Image.open(image_paths[index]) as im:
                im.thumbnail((330, 467))
                x = (offset % 3) * 350 + 10
                y = (offset // 3) * 500 + 24
                sheet.paste(im, (x, y))
                draw.text((x, y - 20), f"Strona {index + 1}", font=font, fill="#172738")
        sheet.save(base.PREVIEW / f"{stem}_contact_{start // 9 + 1:02}.png")
    result = dict(
        file=target.name,
        pages=len(pdf),
        source_words=len(source.split()),
        bytes=target.stat().st_size,
        missing_headings=missing_headings,
        missing_words=missing_words,
        bounds_issues=bounds,
        bad_links=bad_links,
        chapters=chapter_pages,
    )
    (base.ROOT / "tmp/pdfs" / f"{stem}_qa.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    assert len(chapter_pages) == expected_chapters
    assert not (missing_headings or missing_words or bounds or bad_links)
    pdf.close()


if __name__ == "__main__":
    main()

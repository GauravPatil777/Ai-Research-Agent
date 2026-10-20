
import io
import re
import html
import markdown

from html.parser import HTMLParser
from xml.sax.saxutils import escape, quoteattr

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    HRFlowable,
    KeepTogether,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.colors import HexColor


NAVY = HexColor("#172554")
PURPLE = HexColor("#4F46E5")
TEAL = HexColor("#0F766E")
TEXT = HexColor("#334155")
MUTED = HexColor("#64748B")
BORDER = HexColor("#E2E8F0")
LIGHT_BG = HexColor("#F8FAFC")

def generate_pdf(report_text, topic="AI Research Report"):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.70 * inch,
        leftMargin=0.70 * inch,
        topMargin=0.78 * inch,
        bottomMargin=0.70 * inch,
        title=topic,
        author="AI Research Agent",
        subject="AI-generated research report",
    )

    styles = getSampleStyleSheet()
    # Main cover title
    styles.add(ParagraphStyle(
        name="CoverTitle",
        fontName="Helvetica-Bold",
        fontSize=34,       # Increased from 29
        leading=42,
        alignment=TA_CENTER,
        textColor=NAVY,
        spaceAfter=20,
    ))

    # Topic on cover page
    styles.add(ParagraphStyle(
        name="CoverTopic",
        fontName="Helvetica",
        fontSize=21,       # Increased from 17
        leading=28,
        alignment=TA_CENTER,
        textColor=PURPLE,
        spaceAfter=20,
    ))

    # Main section headings
    styles.add(ParagraphStyle(
        name="SectionHeading",
        fontName="Helvetica-Bold",
        fontSize=20,       # Increased from 17
        leading=26,
        textColor=NAVY,
        spaceBefore=20,
        spaceAfter=12,
        keepWithNext=True,
    ))

    # Subsection headings
    styles.add(ParagraphStyle(
        name="SubsectionHeading",
        fontName="Helvetica-Bold",
        fontSize=15,       # Increased from 12
        leading=21,
        textColor=TEAL,
        spaceBefore=15,
        spaceAfter=8,
        keepWithNext=True,
    ))

    # Third-level headings
    styles.add(ParagraphStyle(
        name="ThirdHeading",
        fontName="Helvetica-Bold",
        fontSize=12,       # Increased from 10
        leading=17,
        textColor=PURPLE,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True,
    ))

    # Main report text
    styles.add(ParagraphStyle(
        name="ReportBody",
        fontName="Helvetica",
        fontSize=12,      # Increased from 9.5
        leading=18,       # Space between lines
        textColor=TEXT,
        alignment=TA_LEFT,
        spaceAfter=10,
        splitLongWords=1,
    ))

    # Bullet points
    styles.add(ParagraphStyle(
        name="BulletBody",
        parent=styles["ReportBody"],
        leftIndent=18,
        firstLineIndent=-12,
        spaceAfter=7,
    ))

  # Cover subtitle
    styles.add(ParagraphStyle(
        name="CoverSubtitle",
        fontName="Helvetica",
        fontSize=12,       # Increased from 10
        leading=18,
        alignment=TA_CENTER,
        textColor=MUTED,
    ))

    # Table of contents title
    styles.add(ParagraphStyle(
        name="TOCTitle",
        fontName="Helvetica-Bold",
        fontSize=26,       # Increased from 23
        leading=34,
        textColor=NAVY,
        spaceAfter=24,
    ))

    # Main table of contents entries
    styles.add(ParagraphStyle(
        name="TOCEntry",
        fontName="Helvetica",
        fontSize=12,       # Increased from 10
        leading=20,
        leftIndent=20,
        firstLineIndent=-20,
        textColor=TEXT,
        spaceBefore=7,
    ))

    # Subsection entries in the table of contents
    styles.add(ParagraphStyle(
        name="TOCSubEntry",
        fontName="Helvetica",
        fontSize=11,       # Increased from 9
        leading=17,
        leftIndent=36,
        firstLineIndent=-18,
        textColor=MUTED,
        spaceBefore=4,
    ))


    story = []

    # Cover page
    story.append(Spacer(1, 1.45 * inch))

    story.append(HRFlowable(
        width="28%",
        thickness=4,
        color=PURPLE,
        hAlign="CENTER",
        spaceAfter=25,
    ))

    story.append(Paragraph(
        "AI RESEARCH REPORT",
        styles["CoverTitle"],
    ))

    story.append(Paragraph(
        escape(topic),
        styles["CoverTopic"],
    ))

    story.append(HRFlowable(
        width="55%",
        thickness=0.8,
        color=BORDER,
        hAlign="CENTER",
        spaceBefore=8,
        spaceAfter=25,
    ))

    story.append(Paragraph(
        "Research, insights, and references",
        styles["CoverSubtitle"],
    ))

    story.append(Spacer(1, 0.3 * inch))

    story.append(Paragraph(
        "Prepared by AI Research Agent",
        styles["CoverSubtitle"],
    ))

    story.append(Spacer(1, 2.0 * inch))
    story.append(PageBreak())

    # Table of contents
    story.append(Paragraph(
        "Table of Contents",
        styles["TOCTitle"],
    ))

    toc = TableOfContents()
    toc.levelStyles = [
        styles["TOCEntry"],
        styles["TOCSubEntry"],
    ]
    toc.dotsMinLevel = 0

    story.append(toc)
    story.append(PageBreak())


    html_text = markdown.markdown(
        report_text,
        extensions=["extra", "sane_lists"],
    )

    class ReportParser(HTMLParser):

        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.inline = []
            self.active_block = None
            self.list_stack = []
            self.list_counters = []
            self.heading_counts = {}

        def start_block(self, tag, attrs):
            self.flush_block()
            self.active_block = {
                "tag": tag,
                "attrs": dict(attrs),
                "content": [],
            }

        def add_inline(self, value):
            if self.active_block is not None:
                self.active_block["content"].append(value)
            else:
                self.inline.append(value)

        def handle_starttag(self, tag, attrs):

            if tag in ("h1", "h2", "h3", "h4", "p", "li", "pre"):
                self.start_block(tag, attrs)

            elif tag in ("ul", "ol"):
                self.flush_block()
                self.list_stack.append(tag)
                self.list_counters.append(0)

            elif tag == "br":
                self.add_inline("<br/>")

            elif tag == "hr":
                self.flush_block()
                story.append(Spacer(1, 4))
                story.append(HRFlowable(
                    width="100%",
                    thickness=0.6,
                    color=BORDER,
                ))
                story.append(Spacer(1, 8))

            elif tag in ("strong", "b", "em", "i", "code"):
                self.add_inline(f"<{tag}>")

            elif tag == "a":
                href = dict(attrs).get("href", "")
                if href.startswith(("https://", "http://", "mailto:")):
                    self.add_inline(
                        f'<link href={quoteattr(href)} color="#4F46E5">'
                    )

        def handle_endtag(self, tag):

            if tag in ("strong", "b", "em", "i", "code"):
                self.add_inline(f"</{tag}>")

            elif tag == "a":
                self.add_inline("</link>")

            elif tag in ("h1", "h2", "h3", "h4", "p", "li", "pre"):
                self.flush_block()

            elif tag in ("ul", "ol"):
                self.flush_block()

                if self.list_stack:
                    self.list_stack.pop()
                    self.list_counters.pop()

        def handle_data(self, data):
            self.add_inline(escape(data))

        def flush_block(self):

            if self.active_block is None:
                return

            block = self.active_block
            self.active_block = None

            content = "".join(block["content"]).strip()
            tag = block["tag"]

            if not content:
                return

            if tag in ("h1", "h2", "h3", "h4"):

                if tag == "h1":
                    style = styles["SectionHeading"]
                    toc_level = 0

                elif tag == "h2":
                    style = styles["SubsectionHeading"]
                    toc_level = 1

                else:
                    style = styles["ThirdHeading"]
                    toc_level = None

                heading_id = (
                    block["attrs"].get("id")
                    or f"heading-{len(self.heading_counts) + 1}"
                )

                self.heading_counts[heading_id] = True

                heading = Paragraph(
                    content,
                    style,
                    bulletText=None,
                )

                heading._bookmarkName = heading_id

                if toc_level is not None:
                    heading._toc_level = toc_level

                story.append(heading)

            elif tag == "li":

                prefix = "• "

                if self.list_stack and self.list_stack[-1] == "ol":
                    self.list_counters[-1] += 1
                    prefix = f"{self.list_counters[-1]}. "

                story.append(Paragraph(
                    prefix + content,
                    styles["BulletBody"],
                ))

            elif tag == "pre":

                story.append(Paragraph(
                    content,
                    styles["ReportBody"],
                ))

            else:
                story.append(Paragraph(
                    content,
                    styles["ReportBody"],
                ))

    parser = ReportParser()
    parser.feed(html_text)
    parser.close()
    parser.flush_block()


    class ResearchDocTemplate(SimpleDocTemplate):

        def afterFlowable(self, flowable):

            level = getattr(flowable, "_toc_level", None)

            if level is None:
                return

            text = flowable.getPlainText()
            bookmark = getattr(flowable, "_bookmarkName", None)

            if bookmark:
                self.canv.bookmarkPage(bookmark)

                self.canv.addOutlineEntry(
                    text[:120],
                    bookmark,
                    level=min(level, 0),
                    closed=False,
                )

                self.notify(
                    "TOCEntry",
                    (level, text, self.page, bookmark),
                )

    # Rebuild using the document template that supports TOC entries.
    doc = ResearchDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.70 * inch,
        leftMargin=0.70 * inch,
        topMargin=0.78 * inch,
        bottomMargin=0.70 * inch,
        title=topic,
        author="AI Research Agent",
    )

    def add_page_design(canvas, doc):

        canvas.saveState()

        width, height = A4

        if doc.page > 1:

            canvas.setStrokeColor(BORDER)

            canvas.line(
                doc.leftMargin,
                height - 0.55 * inch,
                width - doc.rightMargin,
                height - 0.55 * inch,
            )

            canvas.setFont("Helvetica", 8)
            canvas.setFillColor(MUTED)

            canvas.drawString(
                doc.leftMargin,
                height - 0.42 * inch,
                "AI RESEARCH AGENT",
            )

            canvas.drawRightString(
                width - doc.rightMargin,
                0.38 * inch,
                f"Page {doc.page}",
            )

        canvas.restoreState()

    doc.multiBuild(
        story,
        onFirstPage=add_page_design,
        onLaterPages=add_page_design,
    )

    buffer.seek(0)

    return buffer.getvalue()

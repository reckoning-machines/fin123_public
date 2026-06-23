from __future__ import annotations

import html
import shutil
import zipfile
from pathlib import Path
from typing import Iterable

from PIL import Image


OUT = Path("fin123_decision_infrastructure_deck.pptx")
BUILD = Path("/private/tmp/fin123_deck_build")
MEDIA = BUILD / "ppt" / "media"

SLIDE_W = 12192000
SLIDE_H = 6858000

BG = "0B0F14"
PANEL = "0D131B"
PANEL2 = "111A24"
LINE = "283847"
MUTED = "75808C"
TEXT = "F5F7FA"
DIM = "AAB2BF"
ACCENT = "58A6FF"
AMBER = "D6A447"
RED = "E35D5B"
WHITE = "FFFFFF"


def emu(inches: float) -> int:
    return int(round(inches * 914400))


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def p_xml(text: str, size: int, color: str = TEXT, bold: bool = False, font: str = "Inter", align: str = "l") -> str:
    b = '<a:b/>' if bold else ""
    return (
        f'<a:p><a:pPr algn="{align}"/>'
        f'<a:r><a:rPr lang="en-US" sz="{size}" dirty="0">{b}'
        f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
        f'<a:latin typeface="{font}"/><a:cs typeface="{font}"/></a:rPr>'
        f"<a:t>{esc(text)}</a:t></a:r></a:p>"
    )


def shape_xml(
    sid: int,
    name: str,
    x: float,
    y: float,
    w: float,
    h: float,
    fill: str = PANEL,
    line: str = LINE,
    radius: str = "roundRect",
    alpha: int | None = None,
) -> str:
    alpha_xml = f'<a:alpha val="{alpha}"/>' if alpha is not None else ""
    return f"""
<p:sp>
  <p:nvSpPr><p:cNvPr id="{sid}" name="{esc(name)}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
  <p:spPr>
    <a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>
    <a:prstGeom prst="{radius}"><a:avLst/></a:prstGeom>
    <a:solidFill><a:srgbClr val="{fill}">{alpha_xml}</a:srgbClr></a:solidFill>
    <a:ln w="12000"><a:solidFill><a:srgbClr val="{line}"/></a:solidFill></a:ln>
  </p:spPr>
  <p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody>
</p:sp>"""


def textbox_xml(
    sid: int,
    name: str,
    x: float,
    y: float,
    w: float,
    h: float,
    paragraphs: Iterable[str],
    valign: str = "top",
    fill: str | None = None,
    line: str | None = None,
) -> str:
    anchor = {"top": "t", "mid": "ctr", "bottom": "b"}[valign]
    sppr = (
        f"""
  <p:spPr>
    <a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>
    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
    {f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else '<a:noFill/>'}
    {f'<a:ln w="10000"><a:solidFill><a:srgbClr val="{line}"/></a:solidFill></a:ln>' if line else '<a:ln><a:noFill/></a:ln>'}
  </p:spPr>"""
    )
    return f"""
<p:sp>
  <p:nvSpPr><p:cNvPr id="{sid}" name="{esc(name)}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
  {sppr}
  <p:txBody><a:bodyPr wrap="square" anchor="{anchor}"/><a:lstStyle/>{''.join(paragraphs)}</p:txBody>
</p:sp>"""


def line_xml(sid: int, x1: float, y1: float, x2: float, y2: float, color: str = LINE, arrow: bool = True, width: int = 16000) -> str:
    x, y = min(x1, x2), min(y1, y2)
    w, h = abs(x2 - x1), abs(y2 - y1)
    flip_h = ' flipH="1"' if x2 < x1 else ""
    flip_v = ' flipV="1"' if y2 < y1 else ""
    tail = '<a:tailEnd type="triangle" w="sm" len="sm"/>' if arrow else ""
    return f"""
<p:sp>
  <p:nvSpPr><p:cNvPr id="{sid}" name="Arrow {sid}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
  <p:spPr>
    <a:xfrm{flip_h}{flip_v}><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>
    <a:prstGeom prst="line"><a:avLst/></a:prstGeom>
    <a:ln w="{width}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill>{tail}</a:ln>
  </p:spPr>
  <p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody>
</p:sp>"""


def node(slide: list[str], sid: int, label: str, x: float, y: float, w: float = 1.55, h: float = 0.56, fill: str = PANEL2, color: str = TEXT) -> int:
    slide.append(shape_xml(sid, label, x, y, w, h, fill=fill, line=LINE, radius="roundRect"))
    slide.append(textbox_xml(sid + 1, f"{label} text", x + 0.08, y + 0.11, w - 0.16, h - 0.16, [p_xml(label, 1280, color, bold=True, align="ctr")], valign="mid"))
    return sid + 2


def title(slide: list[str], sid: int, text: str, eyebrow: str | None = None) -> int:
    if eyebrow:
        slide.append(textbox_xml(sid, "Eyebrow", 0.55, 0.32, 4.5, 0.28, [p_xml(eyebrow.upper(), 760, ACCENT, bold=True, font="Aptos Mono")]))
        sid += 1
    slide.append(textbox_xml(sid, "Title", 0.55, 0.58, 8.8, 0.55, [p_xml(text, 2050, TEXT, bold=True)]))
    sid += 1
    slide.append(line_xml(sid, 0.55, 1.18, 12.75, 1.18, LINE, arrow=False, width=9000))
    return sid + 1


def footer(slide: list[str], sid: int, n: int) -> int:
    slide.append(textbox_xml(sid, "Footer left", 0.55, 7.14, 2.4, 0.22, [p_xml("$fin123", 620, MUTED, bold=True, font="Aptos Mono")]))
    slide.append(textbox_xml(sid + 1, "Footer right", 12.0, 7.14, 0.75, 0.22, [p_xml(f"{n:02d}", 620, MUTED, font="Aptos Mono", align="r")]))
    return sid + 2


def add_picture(slide: list[str], sid: int, rel_id: str, name: str, x: float, y: float, w: float, h: float) -> int:
    slide.append(f"""
<p:pic>
  <p:nvPicPr><p:cNvPr id="{sid}" name="{esc(name)}"/><p:cNvPicPr/><p:nvPr/></p:nvPicPr>
  <p:blipFill><a:blip r:embed="{rel_id}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
  <p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:ln w="12000"><a:solidFill><a:srgbClr val="{LINE}"/></a:solidFill></a:ln></p:spPr>
</p:pic>""")
    return sid + 1


def image_fit(path: Path, x: float, y: float, box_w: float, box_h: float) -> tuple[float, float, float, float]:
    iw, ih = Image.open(path).size
    scale = min(box_w / iw, box_h / ih)
    w, h = iw * scale, ih * scale
    return x + (box_w - w) / 2, y + (box_h - h) / 2, w, h


class Deck:
    def __init__(self) -> None:
        self.slides: list[list[str]] = []
        self.slide_rels: list[list[tuple[str, str]]] = []
        self.media: dict[str, str] = {}

    def pic_rel(self, slide_idx: int, src: str) -> str:
        src_path = Path(src)
        if src not in self.media:
            ext = src_path.suffix.lower()
            media_name = f"image{len(self.media)+1}{ext}"
            self.media[src] = media_name
        while len(self.slide_rels) <= slide_idx:
            self.slide_rels.append([])
        rid = f"rId{len(self.slide_rels[slide_idx]) + 1}"
        self.slide_rels[slide_idx].append((rid, f"../media/{self.media[src]}"))
        return rid

    def add_slide(self, body: list[str]) -> None:
        self.slides.append(body)
        while len(self.slide_rels) < len(self.slides):
            self.slide_rels.append([])


def slide_xml(body: list[str]) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="{BG}"/></a:solidFill></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      {''.join(body)}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''


def add_chip_row(slide: list[str], sid: int, labels: list[str], x: float, y: float, colors: list[str] | None = None) -> int:
    for i, label in enumerate(labels):
        c = colors[i] if colors else PANEL2
        sid = node(slide, sid, label, x + i * 2.22, y, 1.75, 0.66, fill=c)
    return sid


def build_slides(deck: Deck) -> None:
    # 1
    s, sid = [], 10
    s.append(textbox_xml(sid, "Brand", 0.62, 0.64, 4.4, 0.74, [p_xml("$fin123", 2800, TEXT, bold=True, font="Inter")]))
    sid += 1
    s.append(textbox_xml(sid, "Subtitle", 0.66, 1.33, 7.0, 0.42, [p_xml("Decision Infrastructure for Investment Research", 1220, DIM, bold=True)]))
    sid += 1
    s.append(textbox_xml(sid, "Tagline", 0.66, 6.23, 7.2, 0.38, [p_xml("Investment decisions became production workflows.", 1160, TEXT, bold=True)]))
    sid += 1
    cols = [
        ("Data Infrastructure", ["Bloomberg", "FactSet", "Visible Alpha"], 0.85, PANEL2),
        ("Execution Infrastructure", ["OMS", "EMS", "Risk", "Compliance"], 4.65, PANEL2),
        ("Decision Infrastructure", ["$fin123"], 8.85, "12314A"),
    ]
    for heading, labels, x, fill in cols:
        s.append(shape_xml(sid, heading, x, 2.2, 3.0, 2.92, fill="0D131B", line=LINE, radius="rect"))
        sid += 1
        s.append(textbox_xml(sid, f"{heading} heading", x + 0.18, 2.42, 2.64, 0.42, [p_xml(heading, 930, TEXT, bold=True, align="ctr")]))
        sid += 1
        for j, label in enumerate(labels):
            sid = node(s, sid, label, x + 0.42, 3.1 + j * 0.56, 2.16, 0.38, fill=fill, color=ACCENT if label == "$fin123" else DIM)
    s.append(textbox_xml(sid, "Plus1", 3.85, 3.48, 0.35, 0.3, [p_xml("+", 1500, MUTED, bold=True, align="ctr")]))
    s.append(textbox_xml(sid + 1, "Plus2", 8.15, 3.48, 0.35, 0.3, [p_xml("+", 1500, MUTED, bold=True, align="ctr")]))
    sid += 2
    sid = footer(s, sid, 1)
    deck.add_slide(s)

    # 2
    s, sid = [], 10
    sid = title(s, sid, "The Industry Built Infrastructure Around Data")
    labels = ["Bloomberg", "FactSet", "Visible Alpha", "Snowflake", "Databases"]
    xs = [0.8, 3.18, 5.56, 7.94, 10.32]
    for x, label in zip(xs, labels):
        sid = node(s, sid, label, x, 3.18, 1.78, 0.75, fill=PANEL2)
    for x in xs:
        s.append(line_xml(sid, x + 0.89, 2.25, x + 0.89, 3.18, LINE))
        sid += 1
    sid = node(s, sid, "Market + Fundamental Data Layer", 4.15, 1.74, 5.05, 0.62, fill="102033", color=ACCENT)
    s.append(textbox_xml(sid, "Minimal", 4.55, 5.1, 4.2, 0.32, [p_xml("Centralized. Structured. Queried. Governed.", 1050, DIM, bold=True, align="ctr")]))
    sid += 1
    sid = footer(s, sid, 2)
    deck.add_slide(s)

    # 3
    s, sid = [], 10
    sid = title(s, sid, "The Industry Built Infrastructure Around Execution")
    sid = node(s, sid, "Order Lifecycle", 4.75, 1.75, 3.65, 0.62, fill="102033", color=ACCENT)
    exec_labels = ["OMS", "EMS", "Risk", "Compliance"]
    for i, label in enumerate(exec_labels):
        x = 1.25 + i * 3.0
        sid = node(s, sid, label, x, 3.45, 1.7, 0.75, fill=PANEL2)
        s.append(line_xml(sid, 6.58, 2.37, x + 0.85, 3.45, LINE))
        sid += 1
    s.append(textbox_xml(sid, "Minimal", 4.15, 5.25, 5.0, 0.32, [p_xml("Routed. Monitored. Controlled. Recorded.", 1050, DIM, bold=True, align="ctr")]))
    sid += 1
    sid = footer(s, sid, 3)
    deck.add_slide(s)

    # 4
    s, sid = [], 10
    sid = title(s, sid, "Research Still Lives In Files")
    labels = ["Excel", "Word", "PDF", "Email", "Chat"]
    for i, label in enumerate(labels):
        sid = node(s, sid, label, 0.95 + i * 2.35, 2.1, 1.55, 0.62, fill=PANEL2)
    s.append(shape_xml(sid, "Callout", 3.95, 3.72, 5.45, 1.55, fill="17110D", line=AMBER, radius="rect"))
    sid += 1
    s.append(textbox_xml(sid, "Forecast", 4.25, 4.0, 4.85, 0.42, [p_xml("Forecast Changed", 1650, TEXT, bold=True, align="ctr")]))
    sid += 1
    s.append(textbox_xml(sid, "Why", 4.25, 4.62, 4.85, 0.35, [p_xml("Why?", 1320, AMBER, bold=True, align="ctr")]))
    sid += 1
    sid = footer(s, sid, 4)
    deck.add_slide(s)

    # 5
    s, sid = [], 10
    sid = title(s, sid, "Investment Decisions Are Workflows", "Core Thesis")
    labels = ["Observation", "Research", "Discussion", "Forecast", "Decision", "Position", "Outcome"]
    x0, y = 0.55, 3.22
    for i, label in enumerate(labels):
        sid = node(s, sid, label, x0 + i * 1.78, y, 1.35, 0.62, fill="0F1821", color=TEXT if i != 4 else ACCENT)
        if i < len(labels) - 1:
            s.append(line_xml(sid, x0 + i * 1.78 + 1.35, y + 0.31, x0 + (i + 1) * 1.78, y + 0.31, LINE))
            sid += 1
    s.append(textbox_xml(sid, "Thesis", 2.45, 5.0, 8.5, 0.35, [p_xml("The decision process is now a production system.", 1250, DIM, bold=True, align="ctr")]))
    sid += 1
    sid = footer(s, sid, 5)
    deck.add_slide(s)

    # 6
    s, sid = [], 10
    sid = title(s, sid, "One Workflow. Five Stakeholders.")
    sid = node(s, sid, "Decision Model", 5.15, 3.22, 3.05, 0.78, fill="12314A", color=TEXT)
    stakeholders = [("Analyst", 1.2, 1.8), ("PM", 9.95, 1.8), ("Head of Research", 0.95, 5.05), ("Trading Desk", 9.65, 5.05), ("Compliance", 5.2, 5.75)]
    for label, x, y in stakeholders:
        s.append(line_xml(sid, 6.68, 3.61, x + 0.85, y + 0.31, LINE, arrow=False))
        sid += 1
        sid = node(s, sid, label, x, y, 1.9, 0.62, fill=PANEL2)
    sid = footer(s, sid, 6)
    deck.add_slide(s)

    # 7
    s, sid = [], 10
    sid = title(s, sid, "Analyst")
    s.append(textbox_xml(sid, "Question", 0.62, 1.42, 4.2, 0.35, [p_xml("How do I build it?", 1250, ACCENT, bold=True)]))
    sid += 1
    rid = deck.pic_rel(len(deck.slides), "system.png")
    px, py, pw, ph = image_fit(Path("system.png"), 6.45, 1.55, 5.85, 4.2)
    sid = add_picture(s, sid, rid, "fin123 dark system screenshot", px, py, pw, ph)
    sid = node(s, sid, "Decision Model", 1.35, 3.15, 2.7, 0.72, fill="12314A")
    for label, x, y in [("Data", 0.8, 2.0), ("AI", 4.1, 2.0), ("Versions", 0.8, 4.65), ("Scenarios", 4.1, 4.65), ("Runs", 2.45, 5.35)]:
        s.append(line_xml(sid, 2.7, 3.51, x + 0.75, y + 0.3, LINE, arrow=False))
        sid += 1
        sid = node(s, sid, label, x, y, 1.5, 0.58, fill=PANEL2)
    sid = footer(s, sid, 7)
    deck.add_slide(s)

    # 8
    s, sid = [], 10
    sid = title(s, sid, "Portfolio Manager")
    s.append(textbox_xml(sid, "Question", 0.62, 1.42, 5.8, 0.35, [p_xml("Why did the estimate change?", 1250, ACCENT, bold=True)]))
    sid += 1
    sid = node(s, sid, "Estimate", 5.2, 3.25, 2.6, 0.72, fill="12314A")
    for label, x, y in [("Data", 1.0, 2.0), ("Evidence", 3.0, 1.75), ("Memory", 5.25, 1.55), ("AI", 7.65, 1.75), ("Methodology", 9.5, 2.0)]:
        s.append(line_xml(sid, x + 0.8, y + 0.58, 6.5, 3.25, LINE))
        sid += 1
        sid = node(s, sid, label, x, y, 1.65, 0.58, fill=PANEL2)
    rid = deck.pic_rel(len(deck.slides), "yap.png")
    px, py, pw, ph = image_fit(Path("yap.png"), 1.1, 4.65, 11.05, 1.45)
    sid = add_picture(s, sid, rid, "YAP provenance screenshot", px, py, pw, ph)
    sid = footer(s, sid, 8)
    deck.add_slide(s)

    # 9
    s, sid = [], 10
    sid = title(s, sid, "Head of Research")
    s.append(textbox_xml(sid, "Question", 0.62, 1.42, 5.8, 0.35, [p_xml("How do I scale methodology?", 1250, ACCENT, bold=True)]))
    sid += 1
    labels = ["House View", "Coverage Universe", "100 Companies", "100 Results"]
    for i, label in enumerate(labels):
        sid = node(s, sid, label, 4.65, 1.9 + i * 1.08, 4.0, 0.66, fill="12314A" if i == 0 else PANEL2)
        if i < len(labels) - 1:
            s.append(line_xml(sid, 6.65, 2.56 + i * 1.08, 6.65, 2.98 + i * 1.08, LINE))
            sid += 1
    s.append(textbox_xml(sid, "Caption", 3.35, 6.1, 6.65, 0.3, [p_xml("Methodology becomes a reusable operating asset.", 1050, DIM, bold=True, align="ctr")]))
    sid += 1
    sid = footer(s, sid, 9)
    deck.add_slide(s)

    # 10
    s, sid = [], 10
    sid = title(s, sid, "Trading Desk")
    s.append(textbox_xml(sid, "Question", 0.62, 1.42, 9.5, 0.35, [p_xml("How do I fold real-time knowledge into the decision process?", 1150, ACCENT, bold=True)]))
    sid += 1
    s.append(textbox_xml(sid, "Current", 0.9, 2.05, 2.5, 0.28, [p_xml("Current state", 820, MUTED, bold=True, font="Aptos Mono")]))
    sid += 1
    cur = ["Trader", "Chat", "Phone Call", "Lost"]
    for i, label in enumerate(cur):
        sid = node(s, sid, label, 0.9 + i * 2.35, 2.62, 1.55, 0.6, fill=PANEL2 if label != "Lost" else "311A1C", color=RED if label == "Lost" else TEXT)
        if i < len(cur) - 1:
            s.append(line_xml(sid, 2.45 + i * 2.35, 2.92, 3.25 + i * 2.35, 2.92, LINE))
            sid += 1
    s.append(textbox_xml(sid, "Future", 0.9, 4.35, 2.5, 0.28, [p_xml("Future state", 820, MUTED, bold=True, font="Aptos Mono")]))
    sid += 1
    fut = ["Trader", "YAP", "Approved Memory", "Forecast", "Decision"]
    for i, label in enumerate(fut):
        sid = node(s, sid, label, 0.9 + i * 2.18, 4.92, 1.62, 0.6, fill="12314A" if label == "YAP" else PANEL2, color=ACCENT if label == "Decision" else TEXT)
        if i < len(fut) - 1:
            s.append(line_xml(sid, 2.52 + i * 2.18, 5.22, 3.08 + i * 2.18, 5.22, LINE))
            sid += 1
    sid = footer(s, sid, 10)
    deck.add_slide(s)

    # 11
    s, sid = [], 10
    sid = title(s, sid, "Market Knowledge Should Compound")
    labels = ["Observation", "Discussion", "Review", "Approved Memory", "Future Decisions"]
    for i, label in enumerate(labels):
        sid = node(s, sid, label, 4.75, 1.55 + i * 0.88, 3.8, 0.56, fill="12314A" if label == "Approved Memory" else PANEL2)
        if i < len(labels) - 1:
            s.append(line_xml(sid, 6.65, 2.11 + i * 0.88, 6.65, 2.43 + i * 0.88, LINE))
            sid += 1
    for i, t in enumerate(["Research compounds.", "Data compounds.", "Market knowledge should compound too."]):
        s.append(textbox_xml(sid, "Message", 1.0, 5.65 + i * 0.34, 11.5, 0.28, [p_xml(t, 980, TEXT if i == 2 else DIM, bold=True, align="ctr")]))
        sid += 1
    sid = footer(s, sid, 11)
    deck.add_slide(s)

    # 12
    s, sid = [], 10
    sid = title(s, sid, "Compliance")
    s.append(textbox_xml(sid, "Question", 0.62, 1.42, 5.8, 0.35, [p_xml("Can I reconstruct the decision?", 1250, ACCENT, bold=True)]))
    sid += 1
    labels = ["Data", "Evidence", "Decision", "Replay", "Audit"]
    for i, label in enumerate(labels):
        sid = node(s, sid, label, 5.1, 1.8 + i * 0.9, 3.2, 0.58, fill="12314A" if label in ["Decision", "Audit"] else PANEL2)
        if i < len(labels) - 1:
            s.append(line_xml(sid, 6.7, 2.38 + i * 0.9, 6.7, 2.7 + i * 0.9, LINE))
            sid += 1
    sid = footer(s, sid, 12)
    deck.add_slide(s)

    # 13
    s, sid = [], 10
    sid = title(s, sid, "The Decision Model", "Ontology")
    labels = ["Decision Model", "Version", "Scenario", "Run", "Result", "Replay", "Audit"]
    for i, label in enumerate(labels):
        sid = node(s, sid, label, 4.8, 1.42 + i * 0.72, 3.7, 0.48, fill="12314A" if i == 0 else PANEL2, color=ACCENT if i == len(labels) - 1 else TEXT)
        if i < len(labels) - 1:
            s.append(line_xml(sid, 6.65, 1.9 + i * 0.72, 6.65, 2.14 + i * 0.72, LINE, width=12000))
            sid += 1
    sid = footer(s, sid, 13)
    deck.add_slide(s)

    # 14
    s, sid = [], 10
    sid = title(s, sid, "Workbook")
    sid = node(s, sid, "Workbook", 5.0, 2.05, 3.35, 0.7, fill="12314A")
    sid = node(s, sid, "Spreadsheet", 3.15, 3.68, 2.45, 0.62, fill=PANEL2)
    sid = node(s, sid, "Document", 7.75, 3.68, 2.45, 0.62, fill=PANEL2)
    s.append(line_xml(sid, 6.68, 2.75, 4.38, 3.68, LINE, arrow=False))
    sid += 1
    s.append(line_xml(sid, 6.68, 2.75, 8.98, 3.68, LINE, arrow=False))
    sid += 1
    s.append(textbox_xml(sid, "Caption", 3.2, 5.35, 7.0, 0.5, [p_xml("Different surfaces.", 1180, DIM, bold=True, align="ctr"), p_xml("Same governed substrate.", 1180, TEXT, bold=True, align="ctr")]))
    sid += 1
    sid = footer(s, sid, 14)
    deck.add_slide(s)

    # 15
    s, sid = [], 10
    sid = title(s, sid, "Why Firms Adopt $fin123")
    items = ["Better Forecasts", "Faster Research", "Institutional Memory", "Replayable Decisions", "Governed AI", "Decision Infrastructure"]
    for i, label in enumerate(items):
        col, row = i % 3, i // 3
        sid = node(s, sid, label, 1.0 + col * 4.05, 1.8 + row * 1.22, 3.2, 0.72, fill="12314A" if i == 5 else PANEL2, color=ACCENT if i == 5 else TEXT)
    final = [
        "The industry built infrastructure around data.",
        "The industry built infrastructure around execution.",
        "$fin123 brings infrastructure to the decision process itself.",
    ]
    for i, t in enumerate(final):
        s.append(textbox_xml(sid, "Final", 1.2, 5.05 + i * 0.38, 11.0, 0.32, [p_xml(t, 1020, TEXT if i == 2 else DIM, bold=True, align="ctr")]))
        sid += 1
    sid = footer(s, sid, 15)
    deck.add_slide(s)


def write_deck(deck: Deck) -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    (BUILD / "_rels").mkdir(parents=True)
    (BUILD / "ppt" / "_rels").mkdir(parents=True)
    (BUILD / "ppt" / "slides" / "_rels").mkdir(parents=True)
    MEDIA.mkdir(parents=True)
    (BUILD / "docProps").mkdir(parents=True)

    for src, media_name in deck.media.items():
        shutil.copyfile(src, MEDIA / media_name)

    slide_overrides = "\n".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, len(deck.slides) + 1)
    )
    (BUILD / "[Content_Types].xml").write_text(f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Default Extension="png" ContentType="image/png"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  {slide_overrides}
</Types>''')

    (BUILD / "_rels" / ".rels").write_text('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>''')

    ids = "\n".join(f'<p:sldId id="{255+i}" r:id="rId{i}"/>' for i in range(1, len(deck.slides) + 1))
    (BUILD / "ppt" / "presentation.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldIdLst>{ids}</p:sldIdLst>
  <p:sldSz cx="{SLIDE_W}" cy="{SLIDE_H}" type="screen16x9"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>''')

    pres_rels = "\n".join(
        f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
        for i in range(1, len(deck.slides) + 1)
    )
    (BUILD / "ppt" / "_rels" / "presentation.xml.rels").write_text(f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{pres_rels}</Relationships>''')

    for i, body in enumerate(deck.slides, 1):
        (BUILD / "ppt" / "slides" / f"slide{i}.xml").write_text(slide_xml(body))
        rels = "\n".join(
            f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{target}"/>'
            for rid, target in deck.slide_rels[i - 1]
        )
        (BUILD / "ppt" / "slides" / "_rels" / f"slide{i}.xml.rels").write_text(f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{rels}</Relationships>''')

    (BUILD / "docProps" / "core.xml").write_text('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>fin123 Decision Infrastructure for Investment Research</dc:title>
  <dc:creator>fin123</dc:creator>
  <cp:lastModifiedBy>fin123</cp:lastModifiedBy>
</cp:coreProperties>''')
    (BUILD / "docProps" / "app.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>fin123 deck generator</Application><PresentationFormat>On-screen Show (16:9)</PresentationFormat><Slides>{len(deck.slides)}</Slides>
</Properties>''')

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for p in BUILD.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(BUILD))


def main() -> None:
    deck = Deck()
    build_slides(deck)
    write_deck(deck)
    print(f"Wrote {OUT} with {len(deck.slides)} slides")


if __name__ == "__main__":
    main()

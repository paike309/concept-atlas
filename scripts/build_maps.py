#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从概念卡片自动生成地图 (Mermaid)。

读取 concepts/{ai,agent,software}/*.md 的属性表（前置 / 相关），
生成 maps/{overview,ai,agent,software}.md 里的 Mermaid 代码块。

设计取舍：
- 只把「前置」画成实线（学习顺序），「相关」不进图——相关关系已在卡片
  「边界：它不是什么」一节用相对链接表达，图里再画只会过密、且和正文重复。
- overview 只画跨领域衔接（前置指向别的领域），块内顺序在各领域地图里看。
- 只替换每个 maps 文件里的 ```mermaid … ``` 代码块，其余散文原样保留。

用法：
  python scripts/build_maps.py            # 重新生成并写回 maps/*.md
  python scripts/build_maps.py --check    # CI 漂移闸门：重生成后与已提交内容比对，不一致则失败

为什么存在：地图是卡片依赖关系的投影，手写一定会在改卡时忘记同步。
脚本只做投影，不判断内容对错。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"
MAPS = ROOT / "maps"
DOMAINS = ("ai", "agent", "software")
DOMAIN_LABEL = {"ai": "AI / 模型", "agent": "Agent / 控制流", "software": "软件工程"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)\n```", re.S)


def parse_cards():
    """返回 {slug: {domain,title,node,prereq[],related[]}}。"""
    cards = {}
    for domain in DOMAINS:
        d = CONCEPTS / domain
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            m = re.search(r"^#\s+(.+)$", text, re.M)
            title = m.group(1).strip() if m else path.stem
            zh = title.split("·")[0].strip()
            node = "n_" + re.sub(r"[^\w]", "_", path.stem)
            entry = {"slug": path.stem, "domain": domain, "title": zh,
                     "node": node, "prereq": [], "related": []}
            for fld in ("前置", "相关"):
                fm = re.search(r"^\|\s*%s\s*\|\s*(.+?)\s*\|\s*$" % re.escape(fld), text, re.M)
                if not fm:
                    continue
                val = fm.group(1).strip()
                if val in ("无", "—", "-", ""):
                    continue
                for tgt in LINK_RE.finditer(val):
                    rel = tgt.group(1).split("#")[0].strip()
                    slug = Path(rel).stem
                    entry["prereq" if fld == "前置" else "related"].append(slug)
            cards[path.stem] = entry
    return cards


def node_def(card):
    return '    %s["%s"]' % (card["node"], card["title"])


def build_domain_mermaid(cards, domain):
    """返回 mermaid 块内部内容（不含 ```mermaid 包裹）。"""
    lines = ["flowchart TD"]
    lines.append('    subgraph %s["%s"]' % ("G_" + domain, DOMAIN_LABEL[domain]))
    for slug in sorted(cards):
        c = cards[slug]
        if c["domain"] == domain:
            lines.append(node_def(c))
    lines.append("    end")
    for slug in sorted(cards):
        c = cards[slug]
        if c["domain"] != domain:
            continue
        for pre in c["prereq"]:
            p = cards.get(pre)
            if p and p["domain"] == domain:
                lines.append("    %s --> %s" % (p["node"], c["node"]))
    return "\n".join(lines)


def build_overview_mermaid(cards):
    """返回 mermaid 块内部内容（不含 ```mermaid 包裹）。"""
    lines = ["flowchart TD"]
    for domain in DOMAINS:
        lines.append('    subgraph %s["%s"]' % ("G_" + domain, DOMAIN_LABEL[domain]))
        for slug in sorted(cards):
            c = cards[slug]
            if c["domain"] == domain:
                lines.append(node_def(c))
        lines.append("    end")
    for slug in sorted(cards):
        c = cards[slug]
        for pre in c["prereq"]:
            p = cards.get(pre)
            if p and p["domain"] != c["domain"]:
                lines.append("    %s --> %s" % (p["node"], c["node"]))
    return "\n".join(lines)


def render_map_file(path, inner):
    block = "```mermaid\n" + inner.strip() + "\n```"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if MERMAID_RE.search(text):
        text = MERMAID_RE.sub(block, text, count=1)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    # 显式写 LF：文本模式在 Windows 上会把 \n 变成 \r\n，同一脚本在不同平台
    # 就会产出不同字节（diff 全是行尾变化）。Path.write_text 的 newline 参数
    # 要 Python 3.10+，所以这里用 open。
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def generate():
    cards = parse_cards()
    render_map_file(MAPS / "overview.md", build_overview_mermaid(cards))
    for domain in DOMAINS:
        render_map_file(MAPS / (domain + ".md"), build_domain_mermaid(cards, domain))
    return cards


def check():
    cards = parse_cards()
    targets = {
        "overview.md": build_overview_mermaid(cards),
        "ai.md": build_domain_mermaid(cards, "ai"),
        "agent.md": build_domain_mermaid(cards, "agent"),
        "software.md": build_domain_mermaid(cards, "software"),
    }
    bad = []
    for name, expected in targets.items():
        p = MAPS / name
        if not p.exists():
            bad.append("%s 不存在" % name)
            continue
        cur = MERMAID_RE.search(p.read_text(encoding="utf-8"))
        if not cur:
            bad.append("%s 无 mermaid 块" % name)
        elif cur.group(1).strip() != expected.strip():
            bad.append("%s 的 mermaid 与卡片不一致（请重跑 scripts/build_maps.py）" % name)
    if bad:
        print("地图漂移：")
        for b in bad:
            print("  [FAIL] " + b)
        return 1
    print("地图与卡片一致。")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只检查不写入（CI 漂移闸门）")
    args = ap.parse_args()
    if args.check:
        return check()
    cards = generate()
    print("已重新生成 maps/*.md 的 mermaid 块（基于 %d 张卡片）。" % len(cards))
    return 0


if __name__ == "__main__":
    sys.exit(main())

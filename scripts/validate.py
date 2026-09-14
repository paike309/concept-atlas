#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验仓库结构是否符合 docs/schema.md。

在 PR 上由 GitHub Actions 运行。只检查**机器能判定**的部分——结构、字段、
链接。文风、论证质量、来源是否真的支撑正文，这些检查不了，也不该由脚本假装检查。

用法：
  python scripts/validate.py
退出码 0 = 通过，1 = 有错误。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_LINK_PREFIX = ("http://", "https://", "mailto:", "#")

REQUIRED_FIELDS = ("英文", "领域", "层级", "前置", "状态", "信源等级", "最近核对")
REQUIRED_SECTIONS = (
    "## 一句话定义",
    "## 我的理解",
    "## 核心机制",
    "## 边界：它不是什么",
    "## 常见误解",
    "## 应用场景",
    "## 自测",
    "## 来源对应",
)
VALID_VERIFIED = {"unverified", "link-checked", "machine-confirmed", "human-reviewed"}
VALID_STATUS = {"stub", "stable", "stale"}

errors: list[str] = []
warnings: list[str] = []


def field_value(text: str, name: str):
    m = re.search(r"^\|\s*%s\s*\|\s*(.+?)\s*\|\s*$" % re.escape(name), text, re.M)
    return m.group(1).strip() if m else None


def check_card(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")

    def err(msg):
        errors.append("%s: %s" % (rel, msg))

    # ① 文件名
    if not SLUG_RE.match(path.stem):
        err("文件名不是小写英文短名")

    # ② H1
    if not re.search(r"^#\s+\S", text, re.M):
        err("缺少 H1 标题")

    # ③ 属性表字段
    for name in REQUIRED_FIELDS:
        value = field_value(text, name)
        if value is None:
            err("属性表缺少「%s」" % name)
        elif not value:
            err("属性表「%s」为空" % name)

    verified = field_value(text, "信源等级")
    if verified:
        code = verified.strip("`").split("`")[0].split()[0]
        if code not in VALID_VERIFIED:
            err("信源等级取值非法：%s（应为 %s）" % (code, " / ".join(sorted(VALID_VERIFIED))))

    status = field_value(text, "状态")
    if status:
        code = status.strip("`").split("`")[0].split()[0]
        if code not in VALID_STATUS:
            err("状态取值非法：%s（应为 %s）" % (code, " / ".join(sorted(VALID_STATUS))))

    # ④ 参考来源
    if "**参考来源**" not in text:
        err("缺少「参考来源」区块")
    else:
        block = text.split("**参考来源**", 1)[1].split("\n---", 1)[0]
        if not re.search(r"https?://", block):
            err("参考来源里没有任何 URL")

    # ⑤ 正文章节齐全且顺序正确
    positions = []
    for section in REQUIRED_SECTIONS:
        idx = text.find(section)
        if idx < 0:
            err("缺少章节「%s」" % section)
        else:
            positions.append((idx, section))
    if len(positions) == len(REQUIRED_SECTIONS):
        if positions != sorted(positions):
            err("正文章节顺序与 schema 不一致")

    # ⑥ 来源对应非空
    if "## 来源对应" in text:
        tail = text.split("## 来源对应", 1)[1].strip()
        if len(tail) < 20:
            err("「来源对应」章节内容过少")

    # ⑦ 前置字段必须有值（可以是"无"）
    prereq = field_value(text, "前置")
    if prereq is not None and not prereq.strip():
        err("「前置」为空——没有前置也要写「无」")


def check_links() -> None:
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        rel = md.relative_to(ROOT).as_posix()
        in_fence = False
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = re.sub(r"`[^`]*`", "", line)  # 行内代码是示例，不算链接
            for m in LINK_RE.finditer(line):
                target = m.group(1).split("#")[0].strip()
                if not target or target.startswith(SKIP_LINK_PREFIX):
                    continue
                if not (md.parent / target).resolve().exists():
                    errors.append("%s:%d: 相对链接失效 -> %s" % (rel, lineno, target))


def main() -> int:
    cards = sorted(CONCEPTS.rglob("*.md")) if CONCEPTS.is_dir() else []
    for card in cards:
        check_card(card)
    check_links()

    print("检查卡片 %d 张" % len(cards))
    for w in warnings:
        print("  [warn] %s" % w)
    if errors:
        print("\n发现 %d 个错误：" % len(errors))
        for e in errors:
            print("  [FAIL] %s" % e)
        return 1
    print("结构校验通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())

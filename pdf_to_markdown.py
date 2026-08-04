#!/usr/bin/env python3
"""Batch-convert text-based PDFs in a directory to Markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def markdown_filename(pdf_path: Path) -> str:
    """Return a filesystem-safe Markdown filename for a PDF."""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", pdf_path.stem).strip()
    return f"{name or 'document'}.md"


def convert_pdf(pdf_path: Path, output_path: Path) -> int:
    """Extract PDF text page by page and write it as Markdown."""
    import fitz  # PyMuPDF

    document = fitz.open(pdf_path)
    try:
        parts = [f"# {pdf_path.stem}\n"]
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()
            parts.append(f"## 第 {page_number} 页\n")
            parts.append(f"{text}\n" if text else "*此页没有可提取的文本（可能是扫描件）。*\n")
    finally:
        document.close()

    output_path.write_text("\n".join(parts), encoding="utf-8")
    return len(parts) // 2


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert every PDF in a directory to a Markdown file."
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        type=Path,
        default=Path("pdf"),
        help="directory containing PDFs (default: pdf)",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        type=Path,
        default=Path("markdown"),
        help="directory for Markdown files (default: markdown)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="also process PDFs in subdirectories",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()
    if not args.input_dir.is_dir():
        print(f"输入目录不存在或不是目录：{args.input_dir}", file=sys.stderr)
        return 1

    pdf_paths = sorted(
        path for path in (args.input_dir.rglob("*") if args.recursive else args.input_dir.glob("*"))
        if path.is_file() and path.suffix.lower() == ".pdf"
    )
    if not pdf_paths:
        print(f"未在 {args.input_dir} 找到 PDF 文件。")
        return 0

    args.output_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for pdf_path in pdf_paths:
        output_path = args.output_dir / markdown_filename(pdf_path)
        try:
            page_count = convert_pdf(pdf_path, output_path)
            print(f"已转换：{pdf_path} -> {output_path}（{page_count} 页）")
        except Exception as error:
            failures += 1
            print(f"转换失败：{pdf_path}：{error}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

# PDF 转 Markdown

先安装依赖：

```bash
python3 -m pip install PyMuPDF
```

在项目根目录运行：

```bash
python3 pdf_to_markdown.py
```

这会将 `pdf/` 中的每个 PDF 转换为 `markdown/` 中同名的 `.md` 文件。可指定其他输入、输出目录：

```bash
python3 pdf_to_markdown.py 输入PDF目录 输出Markdown目录
```

若 PDF 位于多层子目录中，加入 `--recursive`。该脚本提取可选择、可复制的文本；扫描型 PDF 需要先进行 OCR 才能获得文字内容。

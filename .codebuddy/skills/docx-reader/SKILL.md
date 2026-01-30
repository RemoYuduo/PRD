---
name: docx-reader
description: This skill should be used when the user needs to read, write, extract, or analyze content from Microsoft Word (.docx) files. It provides Python scripts to convert docx files to plain text or Markdown format, and create new Word documents from JSON or Markdown content.
---

# DOCX Reader & Writer Skill

读取、解析和创建 Microsoft Word (.docx) 文档的技能。

## 使用场景

- 需要读取 .docx 文件内容时
- 需要将 Word 文档转换为 Markdown 格式时
- 需要分析 Word 文档结构时
- **需要创建新的 Word 文档时**
- **需要从 JSON 或 Markdown 生成 Word 文档时**

## 依赖安装

首次使用前需安装 python-docx 库：

```bash
pip install python-docx
```

---

## 一、读取文档

### 基本用法

使用 `scripts/read_docx.py` 脚本读取 docx 文件：

```bash
# 输出为 Markdown 格式（默认）
python scripts/read_docx.py <docx文件路径>

# 输出为纯文本格式
python scripts/read_docx.py <docx文件路径> --format text
```

### 输出格式

- **markdown**: 将文档转换为 Markdown 格式，保留标题层级和表格结构
- **text**: 输出纯文本，适合简单文本提取

---

## 二、创建文档

### 基本用法

使用 `scripts/write_docx.py` 脚本创建 docx 文件：

```bash
# 从 Markdown 文件创建 Word 文档
python scripts/write_docx.py output.docx --content input.md

# 从 JSON 文件创建 Word 文档
python scripts/write_docx.py output.docx --content input.json

# 使用模板创建文档
python scripts/write_docx.py output.docx --content input.md --template template.docx
```

### JSON 内容格式

JSON 文件应包含 `elements` 数组，支持以下元素类型：

```json
{
    "elements": [
        {"type": "title", "text": "文档标题", "level": 0},
        {"type": "heading", "text": "章节标题", "level": 1},
        {"type": "paragraph", "text": "段落内容", "bold": false, "italic": false, "alignment": "left"},
        {"type": "table", "headers": ["列1", "列2"], "rows": [["数据1", "数据2"]], "header_color": "4472C4"},
        {"type": "key_value_table", "data": [{"key": "标签", "value": "值"}]},
        {"type": "list", "items": ["项目1", "项目2"], "ordered": false},
        {"type": "page_break"},
        {"type": "empty_lines", "count": 2}
    ]
}
```

### 元素类型说明

| 类型 | 说明 | 参数 |
| --- | --- | --- |
| `title` | 标题 | `text`, `level`(0=主标题, 1-6=章节) |
| `heading` | 章节标题 | `text`, `level` |
| `paragraph` | 段落 | `text`, `bold`, `italic`, `alignment`, `font_size`, `color` |
| `table` | 表格 | `headers`, `rows`, `header_color` |
| `key_value_table` | 键值对表格 | `data`([{key, value}]) |
| `list` | 列表 | `items`, `ordered` |
| `page_break` | 分页符 | 无 |
| `empty_lines` | 空行 | `count` |

### Markdown 内容格式

支持的 Markdown 语法：

- `#` 到 `######` 标题
- 普通段落
- `-` 或 `*` 无序列表
- `1.` 有序列表
- `| 表格 |` Markdown 表格

### Python API 用法

```python
from write_docx import DocxWriter

# 创建文档
writer = DocxWriter()

# 添加标题
writer.add_title("文档标题", level=0)  # 主标题
writer.add_title("第一章", level=1)    # 一级标题

# 添加段落
writer.add_paragraph("这是一个段落。", bold=True)
writer.add_paragraph("居中文本", alignment="center")

# 添加表格
writer.add_table(
    headers=["姓名", "年龄", "职位"],
    rows=[
        ["张三", "28", "工程师"],
        ["李四", "32", "经理"]
    ]
)

# 添加键值对表格（文档信息表）
writer.add_key_value_table([
    {"key": "作者", "value": "张三"},
    {"key": "日期", "value": "2026-01-30"},
    {"key": "版本", "value": "V1.0.0"},
    {"key": "状态", "value": "草稿"}
])

# 添加列表
writer.add_list(["项目1", "项目2", "项目3"], ordered=False)

# 分页
writer.add_page_break()

# 保存
writer.save("output.docx")
```

---

## 功能特性

### 读取功能
1. **标题识别**: 自动识别 Word 文档中的标题样式（Heading 1-6），转换为对应的 Markdown 标题
2. **表格支持**: 将 Word 表格转换为 Markdown 表格格式
3. **列表识别**: 识别列表样式并转换为 Markdown 列表
4. **编码兼容**: 支持中文及其他 Unicode 字符

### 写入功能
1. **多种标题级别**: 支持主标题和1-6级章节标题
2. **丰富的段落格式**: 支持加粗、斜体、对齐、字体大小、颜色等
3. **专业表格**: 支持带彩色表头的表格和键值对表格
4. **列表支持**: 支持有序和无序列表
5. **分页控制**: 支持添加分页符
6. **模板支持**: 可基于现有模板创建新文档
7. **中文支持**: 默认使用微软雅黑字体

---

## 注意事项

- 仅支持 .docx 格式（Office 2007+），不支持旧版 .doc 格式
- 复杂格式（如嵌入图片、特殊样式）可能不会完全保留
- 大型文档处理可能需要较长时间
- 写入时建议使用 JSON 格式以获得更精确的格式控制

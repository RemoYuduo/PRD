#!/usr/bin/env python3
"""
读取 Word (.docx) 文件内容并输出为纯文本或Markdown格式

依赖: pip install python-docx
用法: python read_docx.py <docx_file_path> [--format text|markdown]
"""

import sys
import argparse
from pathlib import Path

try:
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph
except ImportError:
    print("错误: 请先安装 python-docx 库")
    print("运行: pip install python-docx")
    sys.exit(1)


def read_docx_as_text(file_path: str) -> str:
    """读取docx文件，返回纯文本内容"""
    doc = Document(file_path)
    content = []
    
    for element in doc.element.body:
        if element.tag.endswith('p'):
            # 段落
            para = Paragraph(element, doc)
            text = para.text.strip()
            if text:
                content.append(text)
        elif element.tag.endswith('tbl'):
            # 表格
            table = Table(element, doc)
            content.append(format_table_text(table))
    
    return '\n\n'.join(content)


def read_docx_as_markdown(file_path: str) -> str:
    """读取docx文件，返回Markdown格式内容"""
    doc = Document(file_path)
    content = []
    
    for element in doc.element.body:
        if element.tag.endswith('p'):
            para = Paragraph(element, doc)
            text = para.text.strip()
            if text:
                # 检测标题样式
                style_name = para.style.name if para.style else ''
                if 'Heading 1' in style_name or style_name == '标题 1':
                    content.append(f'# {text}')
                elif 'Heading 2' in style_name or style_name == '标题 2':
                    content.append(f'## {text}')
                elif 'Heading 3' in style_name or style_name == '标题 3':
                    content.append(f'### {text}')
                elif 'Heading 4' in style_name or style_name == '标题 4':
                    content.append(f'#### {text}')
                elif 'Heading 5' in style_name or style_name == '标题 5':
                    content.append(f'##### {text}')
                elif 'Heading 6' in style_name or style_name == '标题 6':
                    content.append(f'###### {text}')
                elif 'List' in style_name or '列表' in style_name:
                    content.append(f'- {text}')
                else:
                    content.append(text)
        elif element.tag.endswith('tbl'):
            table = Table(element, doc)
            content.append(format_table_markdown(table))
    
    return '\n\n'.join(content)


def format_table_text(table: Table) -> str:
    """将表格格式化为纯文本"""
    rows = []
    for row in table.rows:
        cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
        rows.append(' | '.join(cells))
    return '\n'.join(rows)


def format_table_markdown(table: Table) -> str:
    """将表格格式化为Markdown表格"""
    if not table.rows:
        return ''
    
    rows = []
    for i, row in enumerate(table.rows):
        cells = [cell.text.strip().replace('\n', ' ').replace('|', '\\|') for cell in row.cells]
        rows.append('| ' + ' | '.join(cells) + ' |')
        if i == 0:
            # 添加分隔行
            separator = '| ' + ' | '.join(['---'] * len(cells)) + ' |'
            rows.append(separator)
    
    return '\n'.join(rows)


def main():
    parser = argparse.ArgumentParser(description='读取Word文档(.docx)内容')
    parser.add_argument('file', help='docx文件路径')
    parser.add_argument('--format', '-f', choices=['text', 'markdown', 'md'], 
                        default='markdown', help='输出格式 (默认: markdown)')
    
    args = parser.parse_args()
    
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"错误: 文件不存在: {file_path}")
        sys.exit(1)
    
    if not file_path.suffix.lower() == '.docx':
        print(f"警告: 文件可能不是docx格式: {file_path}")
    
    try:
        if args.format in ['markdown', 'md']:
            result = read_docx_as_markdown(str(file_path))
        else:
            result = read_docx_as_text(str(file_path))
        
        print(result)
    except Exception as e:
        print(f"错误: 读取文件失败: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

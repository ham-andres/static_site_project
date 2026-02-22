from enum import Enum
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

# def markdown_to_blocks(markdown):
#     result = []
#     markdown_text = markdown.split("\n\n")
#     for block in markdown_text:
#         stripped = block.strip()
#         if stripped != "":
#            result.append(stripped)
#     return result

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH
    


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


# def text_to_children(text):
#     html_node = []
#     text_node = text_to_textnodes(text)
#     for node in text_node:
#         html_node.append(text_node_to_html_node(node))
#     return html_node



# def markdown_to_html_node(markdown):
#     markdown_html = []
#     blocks = markdown_to_blocks(markdown)
#     for block in blocks:
#         type_of_block = block_to_block_type(block)
        
#         if type_of_block == BlockType.HEADING:
#             splitted_block = block.split(" ",1)
#             level = splitted_block[0].count("#")
#             text = splitted_block[1]
#             block_html = text_to_children(text)
#             markdown_html.append(ParentNode(f"h{level}", block_html))
#         elif type_of_block == BlockType.CODE:

#             raw_string = block.split("\n")
#             raw_code = ""
#             for i in range(1,len(raw_string)-1):
#                 raw_code += raw_string[i] + "\n"
#             text_node = TextNode(raw_code, TextType.TEXT)
#             child = text_node_to_html_node(text_node)
#             code_node = ParentNode("code", [child])
#             pre_node = ParentNode("pre", [code_node])
#             markdown_html.append(pre_node)
#         elif type_of_block == BlockType.QUOTE:
#             raw_text_list = block.split("\n")
#             stripped_quote = ""
#             temp = []
#             for quote in raw_text_list:
#                 temp.append(quote.strip("> "))
#             stripped_quote = " ".join(temp)
#             quote_html = text_to_children(stripped_quote)
#             markdown_html.append(ParentNode("blockquote", quote_html))
#         elif type_of_block == BlockType.ORDEREDLIST:
#             raw_text_list = block.split("\n")
#             ol_list = []
#             for line in raw_text_list:
#                 content = line.split(". ",1)[1]
#                 children = text_to_children(content)
#                 ol_list.append(ParentNode("li", children))
#             markdown_html.append(ParentNode("ol",ol_list))
#         elif type_of_block == BlockType.UNORDEREDLIST:
#             raw_text_ulist = block.split("\n")
#             ul = []
#             for line in raw_text_ulist:
#                 content = line.split("- ", 1)[1]
#                 children = text_to_children(content)
#                 ul.append(ParentNode("li", children))
#             markdown_html.append(ParentNode("ul", ul))
#         else:
#             paragraph = " ".join(block.split("\n"))
#             block_html = text_to_children(paragraph)
#             markdown_html.append(ParentNode("p", block_html))

#     return ParentNode("div", markdown_html)
        

            

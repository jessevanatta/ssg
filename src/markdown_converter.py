import re
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode, LeafNode
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered list"
    O_LIST = "ordered list"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Unmatched delimiter {delimiter} in:\n{node.text}")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)
            for n in range(len(split_node)):
                text = split_node[n]
                if text != "":
                    if n % 2 != 0:
                        new_nodes.append(TextNode(text, text_type))
                    else:
                        new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def extract_markdown_images_or_links(text):
    texts = re.findall(r"(?<=\[)(.*?)(?=\])", text)
    urls = re.findall(r"(?<=\()(.*?)(?=\))", text)
    matches = []
    for i in range(len(texts)):
        matches.append((texts[i], urls[i]))
    return matches

def split_nodes_images_or_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            extraction = extract_markdown_images_or_links(remaining_text)
            if extraction == []:
                new_nodes.append(node)
            else:
                for text, url in extraction:
                    parts = remaining_text.split(f"[{text}]({url})", 1)
                    if "![" in node.text:
                        content = TextType.IMAGE
                    else:
                        content = TextType.LINK
                    if len(parts[0]) != 0:
                        new_nodes.append(TextNode(parts[0].rstrip("!"), TextType.TEXT))
                    new_nodes.append(TextNode(text, content, url))
                    remaining_text = parts[1] if len(parts) > 1 else ""
                if len(remaining_text) != 0:
                    new_nodes.append(TextNode(remaining_text.rstrip("!"), TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    init_node = TextNode(text, TextType.TEXT)
    split_bold = split_nodes_delimiter([init_node], "**", TextType.BOLD)
    split_ital = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)
    split_code = split_nodes_delimiter(split_ital, "`", TextType.CODE)
    return split_nodes_images_or_links(split_code)

def markdown_to_blocks(markdown):
    blocks = []
    stripped_md = markdown.strip()
    split_md = stripped_md.split("\n\n")
    for split in split_md:
        if split != "":
            blocks.append(split)
    return blocks

def block_to_block_type(block):
    first_char = block[0]
    _type = BlockType.PARAGRAPH
    match (first_char):
        case "#":
            for char in range(len(block)):
                last = block[char - 1]
                current = block[char]
                _next = block[char + 1]
                # MD only supports 6 heading layers
                if char > 6:
                    raise ValueError("Headings have a maximum depth of 6.")
                # Continue if this is a subheading
                if current == "#":
                    continue
                # Reached end of subheadings
                if last == "#" and current == " ":
                    break
                # Spaces must follow last hash
                if current == "#" and _next != " " and _next != "#":
                    raise ValueError("Headings must have a space following their last #.")
            _type = BlockType.HEADING

        case "`":
            # Inline code
            if block[1] != "`":
                if block[-1] != "`":
                    raise ValueError("Unmatched markdown block.")
            else:            
                # Code block
                if block[:3] != "```":
                    raise ValueError("Code blocks must start with three backticks.")
                elif block[-3:] != "```":
                    raise ValueError("Unmatched markdown block.")
            _type = BlockType.CODE

        case ">":
            split = block.split("\n")
            for s in split:
                if s[0] != ">":
                    raise ValueError("All lines of quotes must begin with >")
            _type = BlockType.QUOTE

        case "-":
            if block[1] != " ":
                raise ValueError("Missing space after dash at top of list.")
            else:
                split = block.split("\n")
                for s in split:
                    if block[1] != " ":
                        raise ValueError(f"Missing space after dash in list item: {s}")
            _type = BlockType.U_LIST

        case "1":
            if block[1] != ".":
                raise ValueError("Missing period after 1 at top of list.")
            else:
                split = block.split("\n")
                for s in range(len(split)):
                    current = split[s]
                    last = split[-1]
                    if current != last:
                        _next = split[s + 1]
                    else:
                        _next = "0"
                    if current[1] != ".":
                        raise ValueError(f"Missing period after number for list item: {split[s]}")
                    if current[0] != last[0] and int(_next[0]) != s + 2:
                        raise ValueError("Ordered lists must increment by 1.")
            _type = BlockType.O_LIST

        case _:
            _type = BlockType.PARAGRAPH

    return _type

def inline_to_children(text):
    nodes = text_to_textnodes(text)
    new_nodes = []
    for node in nodes:
        new_node = text_node_to_html_node(node)
        new_nodes.append(new_node)
    return ParentNode("p", new_nodes)

def text_to_heading(text):
    hash_count = 1
    for i in range(len(text)):
        if text[i + 1] == " ":
            break
        else:
            hash_count += 1
    content = text.replace("#", "").replace("\n", "").strip()
    nodes = text_to_textnodes(content)
    subchildren = []
    for node in nodes:
        subchildren.append(text_node_to_html_node(node))
    return ParentNode(f"h{hash_count}", subchildren)

def list_to_children(text, _type):
    if _type == BlockType.U_LIST:
        tag = "ul"
        start = 2
    else:
        tag = "ol"
        start = 3
    children = []
    split = text.split("\n")
    for s in split:
        # If list item is a link
        s_text = s[start:]
        if s_text[0] == "[":
            extraction = extract_markdown_images_or_links(s_text)
            this_node = ParentNode("li", [LeafNode("a", extraction[0][0], {"href": f"{extraction[0][1]}"})])
        else:
            # Format list item
            nodes = text_to_textnodes(s_text)
            subchildren = []
            for node in nodes:
                subchildren.append(text_node_to_html_node(node))
            this_node = ParentNode("li", subchildren)
        children.append(this_node)
    return ParentNode(tag, children)

def block_to_html_node(block, _type):
    node = -1
    match (_type):
        case BlockType.PARAGRAPH:
            content = block.replace("\n", " ")
            node = inline_to_children(content)

        case BlockType.HEADING:
            node = text_to_heading(block)

        case BlockType.CODE:
            content = block.strip("```").lstrip("\n")
            text_node = TextNode(content, TextType.CODE)
            child = text_node_to_html_node(text_node)
            node = ParentNode("pre", [child])

        case BlockType.QUOTE:
            content = block.replace(">", "").replace("\n", " ").strip()
            node = LeafNode("blockquote", content)

        case BlockType.U_LIST | BlockType.O_LIST:
            node = list_to_children(block, _type)
        
        case _:
            raise ValueError("Not a valid BlockType.")

    return node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block, block_type)
        children.append(html_node)
    return ParentNode("div", children)

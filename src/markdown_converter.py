import re
from textnode import TextNode, TextType
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
                    if "!" in parts[0]:
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
            _type = BlockType.HEADING
        case "```":
            if block[:-3] != "```":
                raise ValueError("Unmatched markdown block.")
            _type = BlockType.CODE
        case ">":
            split = block.split("\n")
            for s in split:
                if s[0] != ">":
                    raise ValueError("All lines of quotes must begin with >")
            _type = BlockType.QUOTE
        case "-":
            split = block.split("\n")
from textnode import TextNode, TextType

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
                if split_node[n] != "":
                    text = split_node[n]
                    if n % 2 != 0:
                        new_nodes.append(TextNode(text, text_type))
                    else:
                        new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

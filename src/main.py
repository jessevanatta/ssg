from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():    
    new_node = TextNode("blah", TextType.LINK, "https://google.com")
    print(new_node)

main()
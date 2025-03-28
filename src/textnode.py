from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, text_node):
        return self.__init__ == text_node.__init__

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        if self.props != None:
            for key in self.props:
                result += f' {key}="{self.props[key]}"'
        return result

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
    def to_html(self):
        result = ""
        if self.tag == None:
            raise ValueError("Parent nodes require a tag.")
        if self.children == None:
            raise ValueError("Parent nodes require children.")
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes require a value.")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
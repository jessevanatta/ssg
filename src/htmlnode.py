
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

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        for key in props:
            result += f" {key}={props[key]}"
        return result

    def __repr__(self):
        print(self)

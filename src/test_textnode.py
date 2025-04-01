import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_type_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_type_noteq(self):
        node = TextNode("blah", TextType.TEXT)
        node2 = TextNode("blah", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_urleq(self):
        node = TextNode("blah", TextType.LINK, "google.com")
        node2 = TextNode("blah", TextType.LINK, "google.com")
        self.assertEqual(node, node2)

    def test_urlnone(self):
        node = TextNode("blah", TextType.LINK)
        node2 = TextNode("blah", TextType.LINK)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
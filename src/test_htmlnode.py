import unittest

from htmlnode import HTMLNode

# class TestHTMLNode(unittest.TestCase):
#     def test_node_eq(self):
#         node = HTMLNode("a", "link", None, {"href": "https://google.com"})
#         node2 = HTMLNode("a", "link", None, {"href": "https://google.com"})
#         self.assertEqual(node, node2)

#     def test_node_validtag(self):
#         valid_tags = ["a", "p", "h1"]
#         node = HTMLNode("p", "p text")
#         self.assertIn(node.tag, valid_tags)

#     def test_node_haschildren(self):
#         node = HTMLNode("p", None, [HTMLNode("a", "link", None, {"href": "https://google.com"})])
#         self.assertTrue(node.children != None and len(node.children) > 0)

#     def test_node_hasprops(self):
#         node = HTMLNode("a", "link", None, {"href": "https://google.com"})
#         self.assertTrue(node.props != None)
    
#     def test_node_noprops(self):
#         node = HTMLNode("p", "just a p", [HTMLNode("a", "link", None, {"href": "https://google.com"})])
#         self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()
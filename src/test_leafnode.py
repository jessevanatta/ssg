import unittest

from htmlnode import HTMLNode, LeafNode

# class TestLeafNode(unittest.TestCase):
#     def test_leaf_to_html_p(self):
#         node = LeafNode("p", "Hello, world!")
#         expected = "<p>Hello, world!</p>"
#         self.assertEqual(node.to_html(), expected)
    
#     def test_leaf_to_html_a(self):
#         node = LeafNode("a", "this a link", {"href": "https://google.com"})
#         expected = '<a href="https://google.com">this a link</a>'
#         self.assertEqual(node.to_html(), expected)
    
#     def test_leaf_noval(self):
#         node = LeafNode("p", None)
#         self.assertRaises(ValueError)

#     def test_leaf_multi_attr(self):
#         node = LeafNode("img", "bear!", {
#             "src": "https://bears.com/cool_bear.jpg", 
#             "alt": "a cool bear", 
#             "width": "1920", 
#             "height": "1080"
#             })
#         expected = '<img src="https://bears.com/cool_bear.jpg" alt="a cool bear" width="1920" height="1080">bear!</img>'
#         self.assertEqual(node.to_html(), expected)
    
#     def test_leaf_notag(self):
#         node = LeafNode(None, "value runs free")
#         expected = "value runs free"
#         self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
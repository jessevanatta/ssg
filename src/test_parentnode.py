import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

# class TestParentNode(unittest.TestCase):
#     def test_to_html_with_children(self):
#         child_node = LeafNode("span", "child")
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

#     def test_to_html_with_grandchildren(self):
#         grandchild_node = LeafNode("b", "grandchild")
#         child_node = ParentNode("span", [grandchild_node])
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<div><span><b>grandchild</b></span></div>",
#         )

#     def test_multi_grandkids(self):
#         grandkids = [
#             LeafNode("p", "Hello, world!"), 
#             LeafNode("a", "this a link", {"href": "https://google.com"}), 
#             LeafNode(None, "value runs free")
#             ]
#         child = ParentNode("body", grandkids)
#         parent = ParentNode("html", [child])
#         expected = '<html><body><p>Hello, world!</p><a href="https://google.com">this a link</a>value runs free</body></html>'
#         self.assertEqual(parent.to_html(), expected)

#     def test_parents_only(self):
#         father = ParentNode("i", None)
#         mother = ParentNode("b", [father])
#         marriage = ParentNode("m", [mother])
#         self.assertRaises(ValueError)
    
#     def test_orphanage(self):
#         child = LeafNode(None, "just a boy")
#         adult_a = ParentNode("p", [child])
#         adult_b = ParentNode("h2", [adult_a])
#         adult_c = ParentNode("h1", [adult_b])
#         adult_d = ParentNode("body", [adult_c])
#         adult_e = ParentNode("html", [adult_d])
#         expected = "<html><body><h1><h2><p>just a boy</p></h2></h1></body></html>"
#         self.assertEqual(adult_e.to_html(), expected)
        

if __name__ == "__main__":
    unittest.main()
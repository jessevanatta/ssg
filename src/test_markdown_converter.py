import unittest

from textnode import TextNode, TextType
from markdown_converter import split_nodes_delimiter, extract_markdown_images_or_links, split_nodes_images_or_links, markdown_to_blocks

class TestMarkdownConverter(unittest.TestCase):
    # def test_bold_wrap(self):
    #     node = TextNode("**bold at start** and **bold at end**", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #     self.assertEqual(new_nodes, [
    #         TextNode("bold at start", TextType.BOLD),
    #         TextNode(" and ", TextType.TEXT),
    #         TextNode("bold at end", TextType.BOLD),
    #     ])
    
    # def test_ital_wrap(self):
    #     node = TextNode("_ital at start_ and _ital at end_", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    #     self.assertEqual(new_nodes, [
    #         TextNode("ital at start", TextType.ITALIC),
    #         TextNode(" and ", TextType.TEXT),
    #         TextNode("ital at end", TextType.ITALIC),
    #     ])

    # def test_code_inline(self):
    #     node = TextNode("here is some `inline code` for you", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    #     self.assertEqual(new_nodes, [
    #         TextNode("here is some ", TextType.TEXT),
    #         TextNode("inline code", TextType.CODE),
    #         TextNode(" for you", TextType.TEXT),
    #     ])

    # def test_code_block(self):
    #     node = TextNode("here is my code:\n```def your_mom(joke):\n    return 'is bad'\n``` how is that?", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "```", TextType.CODE)
    #     self.assertEqual(new_nodes, [
    #         TextNode("here is my code:\n", TextType.TEXT),
    #         TextNode("def your_mom(joke):\n    return 'is bad'\n", TextType.CODE),
    #         TextNode(" how is that?", TextType.TEXT),
    #     ])
    
    # def test_extract_image(self):
    #     matches = extract_markdown_images_or_links("here is an ![image test](https://image.gov) you butt")
    #     self.assertEqual(matches, [("image test", "https://image.gov")])

    # def test_extract_images(self):
    #     matches = extract_markdown_images_or_links("![here](https://ggl.com) ![are](https://goog.com) ![several](https://google.com) ![image tests](https://image.gov) ![you butt](https://boot.dev)")
    #     self.assertEqual(matches, [
    #         ("here", "https://ggl.com"),
    #         ("are", "https://goog.com"),
    #         ("several", "https://google.com"),
    #         ("image tests", "https://image.gov"),
    #         ("you butt", "https://boot.dev")
    #         ])

    # def test_split_image_link_nodes(self):
    #     old_nodes = [
    #         TextNode("Here is an ![image test](https://image.net) first", TextType.TEXT),
    #         TextNode("Followed by a [link test](https://link.net) second", TextType.TEXT),
    #         TextNode("Continuing with another ![image tester](https://imager.net)", TextType.TEXT),
    #         TextNode("And finally, a [big link test](https://biiiiiiigimage.net) last", TextType.TEXT),
    #     ]
    #     nodes = split_nodes_images_or_links(old_nodes)
    #     expected = [
    #         TextNode("Here is an ", TextType.TEXT),
    #         TextNode("image test", TextType.IMAGE, "https://image.net"),
    #         TextNode(" first", TextType.TEXT),
    #         TextNode("Followed by a ", TextType.TEXT),
    #         TextNode("link test", TextType.LINK, "https://link.net"),
    #         TextNode(" second", TextType.TEXT),
    #         TextNode("Continuing with another ", TextType.TEXT),
    #         TextNode("image tester", TextType.IMAGE, "https://imager.net"),
    #         TextNode("And finally, a ", TextType.TEXT),
    #         TextNode("big link test", TextType.LINK, "https://biiiiiiigimage.net"),
    #         TextNode(" last", TextType.TEXT)
    #     ]
    #     self.assertEqual(expected, nodes)

    # def test_split_mixed_nodes(self):
    #     old_nodes = [
    #         TextNode("Here is an ![image test](https://image.net) with a [link test](https://link.net)", TextType.TEXT),
    #         TextNode("Continuing with another ![image tester](https://imager.net) coupled with a [big link test](https://biiiiiiigimage.net)", TextType.TEXT),
    #     ]
    #     nodes = split_nodes_images_or_links(old_nodes)
    #     expected = [
    #         TextNode("Here is an ", TextType.TEXT),
    #         TextNode("image test", TextType.IMAGE, "https://image.net"),
    #         TextNode(" with a ", TextType.TEXT),
    #         TextNode("link test", TextType.LINK, "https://link.net"),
    #         TextNode("Continuing with another ", TextType.TEXT),
    #         TextNode("image tester", TextType.IMAGE, "https://imager.net"),
    #         TextNode(" coupled with a ", TextType.TEXT),
    #         TextNode("big link test", TextType.LINK, "https://biiiiiiigimage.net")
    #     ]
    #     self.assertEqual(expected, nodes)

    def test_markdown_to_blocks(self):
        md = """
This is **bloded**

Another with _ital_ and `code`
Same para new game

- list
- items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bloded**", "Another with _ital_ and `code`\nSame para new game", "- list\n- items"
            ],
        )

if __name__ == "__main__":
    unittest.main()

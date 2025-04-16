import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from markdown_converter import split_nodes_delimiter, extract_markdown_images_or_links, split_nodes_images_or_links, markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node

class TestMarkdownConverter(unittest.TestCase):
    # def test_bold_wrap(self):
    #     node = TextNode("**bold at start** and **bold at end**", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #     self.assertEqual(new_nodes, [
    #         TextNode("bold at start", TextType.BOLD),
    #         TextNode(" and ", TextType.TEXT),
    #         TextNode("bold at end", TextType.BOLD),
    #     ])
    
    def test_ital_wrap(self):
        node = TextNode("_ital at start_ and _ital at end_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        html = text_node_to_html_node(new_nodes[0])
        print(html)
        self.assertEqual(new_nodes, [
            TextNode("ital at start", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("ital at end", TextType.ITALIC),
        ])

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

#     def test_markdown_to_blocks(self):
#         md = """
# This is **bloded**

# Another with _ital_ and `code`
# Same para new game

# - list
# - items
# """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "This is **bloded**", "Another with _ital_ and `code`\nSame para new game", "- list\n- items"
#             ],
#         )

#     def test_block_type_multi(self):
#         types = []
#         md = """
# # The Thing About Geese

# Geese are really wild. Like, seriously crazy. Don't go near them, especially if you're carrying grain.

# ## Not Your Average Bird

# The typical winged creature will flee rapidly once they're disturbed by a human or other predator. Geese, however, are far more stubborn. President Obama once said:

# >In these difficult times, it's important to remember that geese are extremely dangerous creatures to be around. Yes we can, but not if these horrific monsters are given the opportunity to rip your esophagus out.

# ## Coming To Our Senses

# Thanks to our friends at StackOverflow, we're knee-deep in development of an application that notifies you when geese are nearby. This allows you to act accordingly at a moment's notice so you and your family can stay safe. Here's a snippet of the code that makes the magic happen:

# ```
# def goose_detector(x, y, dist):
#     position = (x, y)
#     for i in range(dist):
#         if Geese.GOOSE in position:
#             send_notification("THERE IS A GOOSE NEARBY")
#     return ""
# ```

# ## Things to do

# Below is a list of what actions to take when you spot a goose (or geese).

# 1. Stay calm and maintain eye contact with the creature(s).
# 2. Do NOT approach the creature(s).
# 3. Grab hold of any other humans in your immediate vicinity.
# 4. Slowly back away from the creature(s), ensuring you do not break eye contact. They can smell fear.

# ## Conclusion

# Be aware. Stay safe. Avoid geese whenever possible. 
# """
#         blocks = markdown_to_blocks(md)
#         for block in blocks:
#             types.append(block_to_block_type(block))
#         expected = [
#             BlockType.HEADING,
#             BlockType.PARAGRAPH,
#             BlockType.HEADING,
#             BlockType.PARAGRAPH,
#             BlockType.QUOTE,
#             BlockType.HEADING,
#             BlockType.PARAGRAPH,
#             BlockType.CODE,
#             BlockType.HEADING,
#             BlockType.PARAGRAPH,
#             BlockType.O_LIST,
#             BlockType.HEADING,
#             BlockType.PARAGRAPH
#         ]
#         self.assertEqual(types, expected)

#     def test_paragraphs(self):
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#         )

#     def test_codeblock(self):
#         md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
#         )

#     def test_headings(self):
#         md = """
# # head1

# ## head2

# ### head3

# #### head4

# ##### head5

# ###### head6
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><h1>head1</h1><h2>head2</h2><h3>head3</h3><h4>head4</h4><h5>head5</h5><h6>head6</h6></div>"
#         )

#     def test_aio(self):
#         md = """
# # Here, a Big Test

# Hey! [Here is a link.](https://google.com)

# ## Second heading

# Some `inline code` and **bolded text.** Wow, _power._ Wise words:

# >This quote is dank.
# >It has a second line.

# ### Third heading

# An ![alt texted image.](https://itch.io) What do you think about the order of this list?

# 1. First
# 2. Second
# 3. Third

# Can you handle it without order?

# - Boom
# - Bap
# - Bong

# Finally, a little code block:

# ```
# Booty
# bounce
# ```
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.maxDiff = None
#         self.assertEqual(
#             html,
#              "<div><h1>Here, a Big Test</h1><p>Hey! <a href=\"https://google.com\">Here is a link.</a></p><h2>Second heading</h2><p>Some <code>inline code</code> and <b>bolded text.</b> Wow, <i>power.</i> Wise words:</p><blockquote><p>This quote is dank. It has a second line.</p></blockquote><h3>Third heading</h3><p>An <img src=\"https://itch.io\" alt=\"alt texted image.\"></img> What do you think about the order of this list?</p><ol><li>First</li><li>Second</li><li>Third</li></ol><p>Can you handle it without order?</p><ul><li>Boom</li><li>Bap</li><li>Bong</li></ul><p>Finally, a little code block:</p><pre><code>Booty\nbounce\n</code></pre></div>"
#              )

if __name__ == "__main__":
    unittest.main()


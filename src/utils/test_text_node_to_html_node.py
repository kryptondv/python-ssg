import unittest
from text_node_to_html_node import text_node_to_html_node\

from textnode import TextNode, TextType

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<p>Hello, world!</p>")

    def test_bold_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Hello, world!</b>")

    def test_italic_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Hello, world!</i>")

    def test_code_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Hello, world!</code>")

    def test_link_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<a href='https://www.example.com'>Hello, world!</a>")

    def test_image_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.IMAGE, "https://www.example.com/image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<img src='https://www.example.com/image.jpg' alt='Hello, world!'>")

    def test_invalid_text_type(self):
        text_node = TextNode("Hello, world!", "invalid")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()

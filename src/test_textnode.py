import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Link", "link", "https://example.com")
        node2 = TextNode("Link", "link", "https://example.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Text", "bold", "https://example.com")
        expected = "TextNode(Text, bold, https://example.com)"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
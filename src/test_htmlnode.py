import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HtmlNode(tag="div", value="Hello", children=["world"], props={"class": "container"})
        expected = "HtmlNode(div, Hello, ['world'], {'class': 'container'})"
        self.assertEqual(repr(node), expected)

    def test_props_to_html(self):
        node = HtmlNode(tag="div", value="Hello", children=["world"], props={"class": "container"})
        expected = "class='container'"
        self.assertEqual(node.props_to_html(), expected)

    def test_to_html(self):
        try:
            node = HtmlNode(tag="div", value="Hello", children=["world"], props={"class": "container"})
            with self.assertRaises(NotImplementedError):
                node.to_html()
        except NotImplementedError:
            pass

if __name__ == "__main__":
    unittest.main()
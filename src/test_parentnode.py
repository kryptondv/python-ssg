import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_mixed_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_none_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)

    def test_to_html_with_none_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, []).to_html()

    def test_to_html_with_empty_children(self):
        node = ParentNode("p", [])
        expected = "<p></p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props(self):
        node = ParentNode("p", [], {"class": "container"})
        expected = "<p class='container'></p>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_parent_nodes(self):
        inner_node = ParentNode("div", [LeafNode("span", "Inner text")])
        outer_node = ParentNode("section", [inner_node, LeafNode("p", "Outer text")])
        expected = "<section><div><span>Inner text</span></div><p>Outer text</p></section>"
        self.assertEqual(outer_node.to_html(), expected)

    def test_parent_node_with_multiple_props(self):
        node = ParentNode("div", [LeafNode("p", "Text")], {"id": "main", "class": "container"})
        expected = "<div id='main' class='container'><p>Text</p></div>"
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
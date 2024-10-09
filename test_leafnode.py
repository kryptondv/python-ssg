import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("div", "Hello")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, {})

    def test_init_with_none_value(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None)

    def test_to_html(self):
        node = LeafNode("div", "Hello")
        self.assertEqual(node.to_html(), "<div>Hello</div>")

    def test_to_html_with_props(self):
        node = LeafNode("div", "Hello", {"class": "container"})
        self.assertEqual(node.to_html(), "<div class='container'>Hello</div>")

if __name__ == "__main__":
    unittest.main()

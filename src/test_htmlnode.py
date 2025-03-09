import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple_attrs(self):
        node = HTMLNode(
            props={"href": "https://google.com", "target": "_blank"}
        )
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_single_attr(self):
        node = HTMLNode(props={"class": "main-title"})
        expected = ' class="main-title"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_no_attrs(self):
        node = HTMLNode()
        expected = ''
        self.assertEqual(node.props_to_html(), expected)

    def test_repr_method(self):
        node = HTMLNode("p", "Hello World", None, {"class": "text"})
        expected = "HTMLNode(tag=p, value=Hello World, children=None, props={'class': 'text'})"
        self.assertEqual(repr(node), expected)

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_leaf_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_empty_props(self):
        node = LeafNode("span", "Simple text")
        self.assertEqual(node.to_html(), "<span>Simple text</span>")

if __name__ == "__main__":
    unittest.main()

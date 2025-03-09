import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
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

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
                LeafNode("span", "Just a span"),
            ],
            props={"class": "container"}
        )
        expected = '<div class="container"><p><b>Bold text</b><i>italic text</i></p><span>Just a span</span></div>'
        self.assertEqual(node.to_html(), expected)

    def test_missing_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "content")])

    def test_missing_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_empty_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

if __name__ == "__main__":
    unittest.main()

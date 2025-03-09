import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()

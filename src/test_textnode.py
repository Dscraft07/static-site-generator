import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text_differs(self):
        node = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type_differs(self):
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url_differs(self):
        node = TextNode("Link", TextType.LINK, "https://google.com")
        node2 = TextNode("Link", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_with_none_url(self):
        node = TextNode("Simple text", TextType.TEXT)
        node2 = TextNode("Simple text", TextType.TEXT, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

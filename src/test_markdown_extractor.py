import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(expected, extract_markdown_images(text))

    def test_extract_markdown_links(self):
        text = ("This is text with a link [to boot dev](https://www.boot.dev) "
                "and [to youtube](https://www.youtube.com/@bootdotdev)")
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(expected, extract_markdown_links(text))

    def test_extract_multiple_images_and_links(self):
        text = ("Here is an image ![alt1](https://example.com/img1.png) and a link "
                "[link1](https://example.com) and another image ![alt2](https://example.com/img2.png)")
        expected_images = [
            ("alt1", "https://example.com/img1.png"),
            ("alt2", "https://example.com/img2.png")
        ]
        expected_links = [
            ("link1", "https://example.com")
        ]
        self.assertListEqual(expected_images, extract_markdown_images(text))
        self.assertListEqual(expected_links, extract_markdown_links(text))

if __name__ == "__main__":
    unittest.main()

import unittest
from block_types import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "###### Heading level 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code(self):
        block = "```\nprint('Hello World')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = "> This is a quote\n> that spans multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- First item\n- Second item\n- Third item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_non_incrementing(self):
        block = "1. First item\n3. Second item\n4. Third item"
        # Čísla neklesají o 1, mělo by to být paragraph.
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is just a normal paragraph. It does not match any other type."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()

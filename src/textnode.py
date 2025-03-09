from enum import Enum

# Enum definující typy inline textu
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# Třída reprezentující inline textový prvek
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text                # textový obsah
        self.text_type = text_type      # typ z TextType enumu
        self.url = url                  # URL (pouze pro LINK a IMAGE)

    def __eq__(self, other):
        # Porovnání dvou TextNode objektů (potřebné pro testy)
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        # Čitelná reprezentace objektu (pro debugging)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

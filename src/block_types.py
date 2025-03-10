from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    """
    Určí typ bloku podle Markdown syntaxe.
    Předpokládá se, že block již byl .strip() (bez vedoucích a závěrečných mezer).
    """
    # Code block: začíná a končí třemi backticks.
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Heading: začíná 1 až 6 znaky '#' následovanými mezerou.
    if re.match(r"^#{1,6}\s", block):
        return BlockType.HEADING

    # Quote: každá řádka musí začínat znakem '>'.
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines if line.strip() != ""):
        return BlockType.QUOTE

    # Unordered list: každá řádka musí začínat "- " (spojeno s mezerou).
    if all(line.startswith("- ") for line in lines if line.strip() != ""):
        return BlockType.UNORDERED_LIST

    # Ordered list: každá řádka musí začínat číslem, tečkou a mezerou,
    # a čísla musí začínat 1 a zvyšovat se po řádcích.
    ordered = True
    expected = 1
    for line in lines:
        if not line.strip():
            continue
        match = re.match(r"^(\d+)\.\s", line)
        if match:
            number = int(match.group(1))
            if number != expected:
                ordered = False
                break
            expected += 1
        else:
            ordered = False
            break
    if ordered and expected > 1:
        return BlockType.ORDERED_LIST

    # Pokud nic z výše uvedeného neplatí, jde o odstavec.
    return BlockType.PARAGRAPH

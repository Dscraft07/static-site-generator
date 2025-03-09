import re
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    """
    Rozdělí TextNode objekty podle Markdown syntaxe obrázků.
    Každý výskyt ![alt](url) rozdělí původní textový uzel na tři části:
    - text před obrázkem (TextType.TEXT)
    - samotný obrázek jako TextNode s typem TextType.IMAGE a URL v 'url'
    - text za obrázkem (TextType.TEXT)
    Pokud žádný obrázek nenajde, vrátí původní uzel.
    """
    new_nodes = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        last_end = 0
        matches = list(re.finditer(pattern, text))
        if not matches:
            new_nodes.append(node)
            continue
        for match in matches:
            start, end = match.span()
            # Text před obrázkem
            before = text[last_end:start]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            # Zachycený obrázek
            alt = match.group(1)
            url = match.group(2)
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            last_end = end
        # Zbytek textu za poslední shodou
        after = text[last_end:]
        if after:
            new_nodes.append(TextNode(after, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Rozdělí TextNode objekty podle Markdown syntaxe odkazů.
    Každý výskyt [anchor](url) rozdělí původní textový uzel na:
    - text před odkazem (TextType.TEXT)
    - samotný odkaz jako TextNode s typem TextType.LINK a URL v 'url'
    - text za odkazem (TextType.TEXT)
    Pokud žádný odkaz nenajde, vrátí původní uzel.
    Poznámka: Používáme negative lookbehind (?<!!) k zajištění, že se nejedná o obrázek.
    """
    new_nodes = []
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        last_end = 0
        matches = list(re.finditer(pattern, text))
        if not matches:
            new_nodes.append(node)
            continue
        for match in matches:
            start, end = match.span()
            # Text před odkazem
            before = text[last_end:start]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            # Zachycený odkaz
            anchor = match.group(1)
            url = match.group(2)
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            last_end = end
        # Text za poslední shodou
        after = text[last_end:]
        if after:
            new_nodes.append(TextNode(after, TextType.TEXT))
    return new_nodes

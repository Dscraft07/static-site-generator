import re

def extract_markdown_images(text):
    """
    Vyhledá v textu Markdown obrázky a vrátí seznam dvojic (alt text, URL).
    Používá regex: r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Vyhledá v textu Markdown odkazy a vrátí seznam dvojic (anchor text, URL).
    Používá regex: r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    Poznámka: (?<!!) zajišťuje, že nejde o obrázek.
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter  # Funkce pro bold, italic, code
from markdown_splitter import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    """
    Převede surový Markdown text na seznam TextNode objektů.
    
    Postup:
      1. Začneme s jediným TextNode obsahujícím celý text.
      2. Postupně aplikujeme funkce pro rozdělení podle:
         - Bold: delimiter "**" → TextType.BOLD
         - Italic: delimiter "_" → TextType.ITALIC
         - Code: delimiter "`" → TextType.CODE
         - Obrázky: pomocí split_nodes_image (TextType.IMAGE)
         - Odkazy: pomocí split_nodes_link (TextType.LINK)
    """
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

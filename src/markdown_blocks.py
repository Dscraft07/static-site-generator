def markdown_to_blocks(markdown):
    """
    Rozdělí surový Markdown text na bloky, přičemž každý blok představuje
    oddělenou sekci dokumentu (např. nadpis, odstavec, seznam).
    
    Postup:
      1. Rozdělíme text podle dvojitého nového řádku "\n\n".
      2. Každý blok ořízneme (strip) od přebytečných mezer a nových řádků.
      3. Odstraníme prázdné bloky.
    
    Vrací seznam bloků jako řetězců.
    """
    # Rozdělení textu na části podle "\n\n"
    raw_blocks = markdown.split("\n\n")
    # Oříznutí každého bloku a odstranění prázdných bloků
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    return blocks

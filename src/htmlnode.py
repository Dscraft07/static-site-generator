class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag            # Název HTML tagu (např. 'p', 'a', 'h1')
        self.value = value        # Textový obsah (např. "Hello World")
        self.children = children  # Seznam potomků typu HTMLNode
        self.props = props        # Slovník HTML atributů (např. {"href": "..."})

    def to_html(self):
        raise NotImplementedError("This method should be implemented in subclasses.")

    def props_to_html(self):
        if not self.props:
            return ""
        html_attrs = ""
        for prop, val in self.props.items():
            html_attrs += f' {prop}="{val}"'
        return html_attrs

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag}, value={self.value}, "
                f"children={self.children}, props={self.props})")

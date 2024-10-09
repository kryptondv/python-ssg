from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("Value cannot be None for LeafNode")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None for LeafNode")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        props_string = f" {props_html}" if props_html else ""
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        if children is None:
            raise ValueError("Children cannot be None for ParentNode")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        
        children_html = "".join([child.to_html() for child in self.children])
        props_html = self.props_to_html()
        props_string = f" {props_html}" if props_html else ""
        return f"<{self.tag}{props_string}>{children_html}</{self.tag}>"

class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    NotImplementedError

  def props_to_html(self):
    if(not self.props):
      return ""
    return " ".join(f'{key}="{value}"' for key, value in self.props.items())

  def __repr__(self):
    return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
  
  def __eq__(self, other):
    return (
      self.tag == other.tag
      and self.value == other.value
      and self.children == other.children
      and self.props == other.props
    )
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if(not self.value):
      raise ValueError("All leaf nodes must have a value")
    if(not self.tag):
      return self.value
    if(not self.props):
      return f"<{self.tag}>{self.value}</{self.tag}>"
    return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
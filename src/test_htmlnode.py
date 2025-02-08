import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    htmlnode = HTMLNode("a", "linkhere", None, {
        "href": "https://www.google.com",
        "target": "_blank",
    })
    self.assertEqual(htmlnode.props_to_html(), 'href="https://www.google.com" target="_blank"')

  def test_html_constructor(self):
    htmlnode = HTMLNode("p", "testing", None, None)
    htmlnode2 = HTMLNode("p", "testing", None, None)
    self.assertEqual(htmlnode, htmlnode2)

  def test_not_eq(self):
    htmlnode = HTMLNode("p", "testing", None, None)
    htmlnode2 = HTMLNode("h1", "testing", None, None)
    self.assertNotEqual(htmlnode, htmlnode2)

  def test_repr(self):
    node = HTMLNode(
      "p",
      "What a strange world",
      None,
      {"class": "primary"},
    )
    self.assertEqual(
      node.__repr__(),
      "HTMLNode(tag=p, value=What a strange world, children=None, props={'class': 'primary'})",
    )

  def test_to_html_no_children(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_to_html_no_tag(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")

  def test_to_html(self):
    p_tag_node = LeafNode("p", "This is a paragraph of text.")
    a_tag_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(p_tag_node.to_html(), '<p>This is a paragraph of text.</p>')
    self.assertEqual(a_tag_node.to_html(), '<a href="https://www.google.com">Click me!</a>')

  def test_to_html_no_tag(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")

  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

  def test_to_html_many_children(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(
        node.to_html(),
        "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
    )

  def test_headings(self):
    node = ParentNode(
      "h2",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(
      node.to_html(),
      "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
    )

if __name__ == "__main__":
  unittest.main()
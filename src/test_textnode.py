import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
  
  def test_not_eq(self):
    node = TextNode("This is a text node", TextType.NORMAL)
    node2 = TextNode("This is a text node2", TextType.NORMAL)
    self.assertNotEqual(node, node2)

  def test_url_None(self):
    node = TextNode("This is a text node", TextType.ITALIC, None)
    node2 = TextNode("This is a text node2", TextType.ITALIC)
    self.assertNotEqual(node, node2)

class TextHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    htmlnode = HTMLNode("a", "linkhere", None, {
        "href": "https://www.google.com",
        "target": "_blank",
    })
    self.assertEqual(htmlnode.props_to_html(), 'href="https://www.google.com" target="_blank"')
if __name__ == "__main__":
  unittest.main()

class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text(self):
    node = TextNode("This is a text node", TextType.NORMAL)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_image(self):
    node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(
      html_node.props,
      {"src": "https://www.boot.dev", "alt": "This is an image"},
    )

  def test_bold(self):
    node = TextNode("This is bold", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is bold")
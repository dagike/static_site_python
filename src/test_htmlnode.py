import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
  unittest.main()
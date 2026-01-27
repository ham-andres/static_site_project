import unittest

from htmlnode import HTMLNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        hnode1 = HTMLNode(tag="a", value="Click me", props={"href": "https://www.google.com", "target": "_blank"})
        
        self.assertEqual(hnode1.props_to_html(), ' href="https://www.google.com" target="_blank"')
        hnode2 = HTMLNode(props={"class": "button"})
        self.assertEqual(hnode2.props_to_html(), ' class="button"')

        hnode3 = HTMLNode()
        self.assertEqual(hnode3.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        lnode1 = LeafNode("p", "Hello, world!")
        self.assertEqual(lnode1.to_html(),"<p>Hello, world!</p>")
        lnode2 = LeafNode(None, "raw text")
        self.assertEqual(lnode2.to_html(), "raw text")
        lnode3 = LeafNode(tag="a", value="Click me!", props={"href": "https://example.com"})
        self.assertEqual(lnode3.to_html(), "<a href='https://example.com'>Click me!</a>")
        lnode4 = LeafNode("p", None)
        with self.assertRaises(ValueError):
            lnode4.to_html()
            
if __name__ == "__main__":
    unittest.main()
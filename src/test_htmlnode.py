import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        hnode1 = HTMLNode(tag="a", value="Click me", props={"href": "https://www.google.com", "target": "_blank"})
        
        self.assertEqual(hnode1.props_to_html(), ' href="https://www.google.com" target="_blank"')
        hnode2 = HTMLNode(props={"class": "button"})
        self.assertEqual(hnode2.props_to_html(), ' class="button"')

        hnode3 = HTMLNode()
        self.assertEqual(hnode3.props_to_html(), "")




if __name__ == "__main__":
    unittest.main()
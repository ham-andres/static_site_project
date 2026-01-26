import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("this is awesome", TextType.TEXT)
        node4 = TextNode("this is not awesome", TextType.TEXT)
        self.assertNotEqual(node3,node4)
        node5 = TextNode("this is awesome", TextType.LINK,"www.awesome.m")
        node6 = TextNode("this is awesome", TextType.LINK,"www.awesome.m")
        self.assertEqual(node5,node6)
        node7 = TextNode("this is awesome", TextType.BOLD,"www.awesome.m")
        node8 = TextNode("this is awesome", TextType.BOLD)
        self.assertNotEqual(node7,node8)
        node9 = TextNode("this is awesome", TextType.IMAGE,"www.awesome.m")
        node10 = TextNode("this is awesome", TextType.LINK,"www.awesome.m")
        self.assertNotEqual(node9,node10)
        


if __name__ == "__main__":
    unittest.main()
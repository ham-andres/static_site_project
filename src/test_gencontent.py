import unittest
from gencontent import extract_title

class Testgencontent(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# hello")
        self.assertEqual(title,"hello")

        title2 = extract_title("hello")
        self.assertEqual(title2,"No header found")

        


if __name__=='__main__':
    unittest.main()
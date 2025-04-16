import unittest
from main import extract_title

# class TestExtractTitle(unittest.TestCase):
#     def test_valid(self):
#         md = "# Valid MD Header"
#         expected = "Valid MD Header"
#         self.assertEqual(extract_title(md), expected)

#     def test_invalid(self):
#         md = "Not Valid MD Header"
#         self.assertRaises(Exception)


if __name__ == "__main__":
    unittest.main()
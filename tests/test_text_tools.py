import unittest
from page_object import text_tools

class GetPriceTests(unittest.TestCase):

    def test(self):
        examples = [
            # 0                                 1
            ["$110.00 $122.00\nEx Tax: $90.00", "110.00"],
            ["$122.00\nEx Tax: $100.00", "122.00"],
            ["$1,202.00\nEx Tax: $1,000.00", "1202.00"],
            ["$1,202.00\nEx Tax: $1,000.00", "1202.00"],
            ["", ""],
            ["$", ""],
        ]

        for example in examples:
            self.assertEqual(example[1], text_tools.extract_price(example[0]))

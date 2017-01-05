import unittest

from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_integer_values(self):
        self.assertEqual(format_price(1), '1')
        self.assertEqual(format_price(1234), '1 234')
        self.assertEqual(format_price(1234567890), '1 234 567 890')

    def test_float_values(self):
        self.assertEqual(format_price(1.2), '1.20')
        self.assertEqual(format_price(1234.100200), '1 234.10')
        self.assertEqual(format_price(1234567890.50), '1 234 567 890.50')

    def test_string_values(self):
        self.assertEqual(format_price('1'), '1')
        self.assertEqual(format_price('1234'), '1 234')
        self.assertEqual(format_price('1234567890'), '1 234 567 890')

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            format_price('abc')
        with self.assertRaises(ValueError):
                format_price('')
        with self.assertRaises(ValueError):
            format_price('123 456')
        with self.assertRaises(ValueError):
            format_price('123.456.50')
        with self.assertRaises(TypeError):
            format_price([1])


if __name__ == '__main__':
    unittest.main()

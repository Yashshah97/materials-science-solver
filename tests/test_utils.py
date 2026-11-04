import unittest
from materials_science_solver import utils

class TestUtils(unittest.TestCase):
    def test_parse_int_list(self):
        self.assertEqual(utils.parse_int_list('1,2,3'), [1, 2, 3])

    def test_parse_float_list(self):
        self.assertAlmostEqual(utils.parse_float_list('1.0,2.0,3.0'), [1.0, 2.0, 3.0])

    def test_parse_tuple(self):
        self.assertEqual(utils.parse_tuple('1,2,3'), (1, 2, 3))

    def test_parse_float_tuple(self):
        self.assertAlmostEqual(utils.parse_float_tuple('1.0,2.0,3.0'), (1.0, 2.0, 3.0))

    def test_setup_logging(self):
        utils.setup_logging()
        self.assertEqual(logging.root.level, logging.INFO)

if __name__ == '__main__':
    unittest.main()

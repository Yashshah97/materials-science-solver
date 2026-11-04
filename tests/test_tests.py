import unittest
from materials_science_solver import tests

class TestTestModule(unittest.TestCase):

    def test_test_module_init(self):
        """Test that the test module initializes correctly."""
        self.assertIsNotNone(tests)

    def test_test_module_classes_exist(self):
        """Test that the required classes exist in the test module."""
        self.assertTrue(hasattr(tests, 'TestSolver'))
        self.assertTrue(hasattr(tests, 'TestStrategy'))

if __name__ == '__main__':
    unittest.main()

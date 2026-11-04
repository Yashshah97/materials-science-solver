"""Smoke tests for strategies."""
import unittest

from materials_science_solver import strategies


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(strategies, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(strategies) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()

"""Smoke tests for solver."""
import unittest

from materials_science_solver import solver


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(solver, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(solver) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()

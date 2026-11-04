import unittest
from materials_science_solver import benchmarks

class TestBenchmarkFunctions(unittest.TestCase):

    def test_timer_decorator(self):
        @benchmarks.timer_decorator
        def example_function():
            return None
        result = example_function()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_run_benchmark(self):
        strategy = lambda: None
        result = benchmarks.run_benchmark(strategy)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_generate_random_lattice(self):
        size = 5
        lattice = benchmarks.generate_random_lattice(size)
        self.assertEqual(len(lattice), size)
        for row in lattice:
            self.assertEqual(len(row), size)

if __name__ == '__main__':
    unittest.main()

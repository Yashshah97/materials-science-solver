import unittest
from materials_science_solver import strategies

class TestStrategies(unittest.TestCase):
    def test_greedy_strategy(self):
        constraints = [{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}]
        strategy = strategies.GreedyStrategy()
        solutions = list(strategy.solve(constraints))
        self.assertEqual(len(solutions), 1)
        self.assertIn('a', solutions[0])
        self.assertIn('b', solutions[0])

    def test_exhaustive_strategy(self):
        constraints = [{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}]
        strategy = strategies.ExhaustiveStrategy()
        solutions = list(strategy.solve(constraints))
        self.assertEqual(len(solutions), 4)
        for solution in solutions:
            self.assertIn('a', solution)
            self.assertIn('b', solution)

    def test_random_strategy(self):
        constraints = [{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}]
        strategy = strategies.RandomStrategy()
        solutions = list(strategy.solve(constraints))
        self.assertGreaterEqual(len(solutions), 1)
        for solution in solutions:
            self.assertIn('a', solution)
            self.assertIn('b', solution)

if __name__ == '__main__':
    unittest.main()

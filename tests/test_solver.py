import unittest
from materials_science_solver import solver

class TestConstraintSolver(unittest.TestCase):
    def test_add_constraint(self):
        solver = solver.ConstraintSolver()
        constraint = {'a': 1, 'b': 2}
        solver.add_constraint(constraint)
        self.assertEqual(solver.constraints[0], constraint)

    def test_set_strategy(self):
        solver = solver.ConstraintSolver()
        strategy = lambda x: x
        solver.set_strategy(strategy)
        self.assertEqual(solver.strategy, strategy)

    def test_solve_with_strategy(self):
        solver = solver.ConstraintSolver()
        strategy = lambda x: x[0]
        solver.set_strategy(strategy)
        constraint = {'a': 1, 'b': 2}
        solver.add_constraint(constraint)
        solution = solver.solve()
        self.assertEqual(solution, constraint)

    def test_solve_without_strategy(self):
        solver = solver.ConstraintSolver()
        with self.assertRaises(ValueError):
            solver.solve()

class TestStrategy(unittest.TestCase):
    def test_identity_strategy(self):
        strategy = solver.identity_strategy([{'a': 1, 'b': 2}])
        solution = strategy
        self.assertEqual(solution, {'a': 1, 'b': 2})

if __name__ == '__main__':
    unittest.main()

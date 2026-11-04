"""
Module containing various solving strategies that can be plugged into the solver.

Each strategy is a class with a `solve` method. The solve method should take in a list of constraints and return a solution.
"""

class GreedyStrategy:
    """
    A greedy strategy that selects the first possible solution it finds.
    """
    def solve(self, constraints):
        """
        Solve the given constraints.

        Args:
            constraints (list): A list of constraints. Each constraint is a dictionary with 'name' and 'value' keys.

        Returns:
            dict: The first possible solution found.
        """
        for i in range(1 << len(constraints)):
            solution = {}
            for j, constraint in enumerate(constraints):
                if (i >> j) & 1:
                    solution[constraint['name']] = constraint['value']
            yield solution


class ExhaustiveStrategy:
    """
    An exhaustive strategy that tries all possible solutions.
    """
    def solve(self, constraints):
        """
        Solve the given constraints.

        Args:
            constraints (list): A list of constraints. Each constraint is a dictionary with 'name' and 'value' keys.

        Yields:
            dict: Each possible solution found.
        """
        for i in range(1 << len(constraints)):
            solution = {}
            for j, constraint in enumerate(constraints):
                if (i >> j) & 1:
                    solution[constraint['name']] = constraint['value']
            yield solution


class RandomStrategy:
    """
    A random strategy that selects a solution at random.
    """
    def solve(self, constraints):
        """
        Solve the given constraints.

        Args:
            constraints (list): A list of constraints. Each constraint is a dictionary with 'name' and 'value' keys.

        Yields:
            dict: A random possible solution found.
        """
        import random
        for _ in range(1000):  # Try 1000 times to find a solution
            i = random.randint(1, (1 << len(constraints)) - 1)
            solution = {}
            for j, constraint in enumerate(constraints):
                if (i >> j) & 1:
                    solution[constraint['name']] = constraint['value']
            yield solution

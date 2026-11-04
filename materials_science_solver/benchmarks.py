"""
Module containing functions to run benchmarks on the solver's performance.

This module provides a set of benchmarking functions that can be used to test and compare different strategies for solving crystal lattice and alloy properties.
"""

import time
from functools import wraps
import random

def timer_decorator(func):
    """
    Decorator function to measure execution time of a given function.

    Args:
        func (function): The function whose execution time is to be measured.

    Returns:
        A wrapper function that measures the execution time and returns it.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return (end_time - start_time), result
    return wrapper

def run_benchmark(strategy, num_iterations=10):
    """
    Runs a benchmark on the given strategy.

    Args:
        strategy (function): The strategy to be benchmarked.
        num_iterations (int, optional): Number of iterations for the benchmark. Defaults to 10.

    Returns:
        tuple: A tuple containing the average execution time and the results of the last iteration.
    """
    total_time = 0
    results = []
    for _ in range(num_iterations):
        result = strategy()
        execution_time, result_value = timer_decorator(strategy)()
        total_time += execution_time
        results.append(result_value)
    avg_execution_time = total_time / num_iterations
    return avg_execution_time, results

def generate_random_lattice(size=10):
    """
    Generates a random crystal lattice of the given size.

    Args:
        size (int, optional): Size of the lattice. Defaults to 10.

    Returns:
        list: A 2D list representing the crystal lattice.
    """
    return [[random.choice([-1, 1]) for _ in range(size)] for _ in range(size)]

def run_lattice_benchmark(strategy):
    """
    Runs a benchmark on the given strategy for generating random lattices.

    Args:
        strategy (function): The strategy to be benchmarked.

    Returns:
        tuple: A tuple containing the average execution time and the results of the last iteration.
    """
    return run_benchmark(strategy, num_iterations=10)

def run_alloy_benchmark(strategy):
    """
    Runs a benchmark on the given strategy for generating random alloys.

    Args:
        strategy (function): The strategy to be benchmarked.

    Returns:
        tuple: A tuple containing the average execution time and the results of the last iteration.
    """
    return run_benchmark(strategy, num_iterations=10)

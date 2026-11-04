"""
Miscellaneous utility functions for the materials science constraint solver.

This module provides various utility functions used throughout the project,
including logging and parsing functionality.
"""

import argparse
import logging
import re
from typing import List, Tuple

def parse_int_list(s: str) -> List[int]:
    """
    Parse a comma-separated string of integers into a list.

    Args:
        s (str): A comma-separated string of integers.

    Returns:
        List[int]: A list of parsed integers.
    """
    return [int(i) for i in re.split(r'[^\d]+', s)]

def parse_float_list(s: str) -> List[float]:
    """
    Parse a comma-separated string of floats into a list.

    Args:
        s (str): A comma-separated string of floats.

    Returns:
        List[float]: A list of parsed floats.
    """
    return [float(i) for i in re.split(r'[^\d\.]+', s)]

def parse_tuple(s: str, sep: str = ',') -> Tuple[int]:
    """
    Parse a comma-separated string into an integer tuple.

    Args:
        s (str): A comma-separated string of integers.
        sep (str): The separator to use for parsing. Defaults to ','.

    Returns:
        Tuple[int]: An integer tuple parsed from the input string.
    """
    return tuple(int(i) for i in re.split(sep, s))

def parse_float_tuple(s: str, sep: str = ',') -> Tuple[float]:
    """
    Parse a comma-separated string into a float tuple.

    Args:
        s (str): A comma-separated string of floats.
        sep (str): The separator to use for parsing. Defaults to ','.

    Returns:
        Tuple[float]: An integer tuple parsed from the input string.
    """
    return tuple(float(i) for i in re.split(sep, s))

def setup_logging(log_level: int = logging.INFO):
    """
    Set up basic logging configuration.

    Args:
        log_level (int): The minimum logging level to display. Defaults to INFO.
    """
    logging.basicConfig(level=log_level)

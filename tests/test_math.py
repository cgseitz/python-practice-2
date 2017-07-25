"""
testing for the math.py module
"""

import python_practice_2 as pp2
import pytest

def test_add():
    assert pp2.math.add(5, 2) == 7
    assert pp2.math.add(2, 5) == 7

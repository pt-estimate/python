import numpy as np
import pytest
import sys
sys.path.append('../')
from binomial_proportions import difference


def test_difference():
    """python -m pytest test_binomial_proportions.py"""
    n1, n2 = 10, 10
    s1 = np.random.binomial(n1, p=0.5, size=1)[0]
    s2 = np.random.binomial(n2, p=0.5, size=1)[0]
    lb, ub = difference(n1, n2, s1, s2)
    in_ci_count = 0
    for i in range(100):
        s1 = np.random.binomial(n1, p=0.5, size=1)[0]
        s2 = np.random.binomial(n2, p=0.5, size=1)[0]
        if lb <= s1/n1 - s2/n2 <= ub:
            in_ci_count+=1
    assert(in_ci_count >= 95)
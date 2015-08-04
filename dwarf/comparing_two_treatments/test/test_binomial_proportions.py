import numpy as np
import pytest
import sys
sys.path.append('../')
from binomial_proportions import normal_interval 


def test_normal_interval():
    """python -m pytest test_binomial_proportions.py"""
    n1, n2 = 10, 10
    s1 = np.random.binomial(n1, p=0.5, size=1)[0]
    s2 = np.random.binomial(n2, p=0.5, size=1)[0]
    lb, ub = normal_interval(n1, n2, s1, s2, 0.05)
    in_ci_count = 0
    for i in range(100):
        s1 = np.random.binomial(n1, p=0.5, size=1)[0]
        s2 = np.random.binomial(n2, p=0.5, size=1)[0]
        if lb <= s1/n1 - s2/n2 <= ub:
            in_ci_count+=1
    assert(in_ci_count >= 95)
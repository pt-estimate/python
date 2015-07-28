"""Script to test difference in binomial proportions for two populations"""
from __future__ import division

import math
import numpy as np
import sys


def difference(n1, n2, s1, s2):
    """Compares two binomial proportions."""
    p1_hat = s1/n1
    p2_hat = s2/n2
    est_std = math.sqrt(p1_hat*(1-p1_hat)/n1 + p2_hat*(1-p2_hat)/n2)
    return (p1_hat - p2_hat)-1.96*est_std, (p1_hat - p2_hat)+1.96*est_std

def main():
    """Main entry point for the script."""
    n1, n2 = 10, 10
    s1 = np.random.binomial(n1, p=0.3, size=1)
    s2 = np.random.binomial(n2, p=0.6, size=1)
    lb, ub = difference(n1, n2, s1, s2)
    print "\nWe are 95%% confident the difference in probabilities p1-p2 lies in the interval %f to %f" % (lb[0], ub[0])


if __name__ == '__main__':
    sys.exit(main())
"""Script to test difference in binomial proportions for two populations"""
from __future__ import division

import numpy as np
from scipy import stats


def normal_interval(n1, n2, s1, s2, alpha):
    """Compares two binomial proportions under the following assumptions:
       - p1_hat and p2_hat are independent
       - n1 and n2 are both large
       - relies on central limit theorem"""
    p1_hat = s1/n1
    p2_hat = s2/n2
    est_std = np.sqrt(p1_hat*(1-p1_hat)/n1 + p2_hat*(1-p2_hat)/n2)
    cv_of_z = stats.norm.isf(alpha / 2)
    return (p1_hat - p2_hat)-cv_of_z*est_std, (p1_hat - p2_hat)+cv_of_z*est_std
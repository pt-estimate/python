from __future__ import division
import numpy as np
from scipy import stats
import sys

def wilson_score_interval(success_count, total_count, alpha):
    """Computes a 100(1-alpha)% wilson score confidence interval for the parameter"""
    cv_of_z = stats.norm.isf(alpha / 2)
    p_hat = success_count / total_count
    lower_bound = p_hat + cv_of_z**2/(2*total_count) - cv_of_z * \
            np.sqrt((p_hat*(1-p_hat) + cv_of_z**2/(4*total_count))/total_count)/ (1 + cv_of_z**2/total_count)
    upper_bound = p_hat + cv_of_z**2/(2*total_count) + cv_of_z * \
            np.sqrt((p_hat*(1-p_hat) + cv_of_z**2/(4*total_count))/total_count)/ (1 + cv_of_z**2/total_count)
    return lower_bound, upper_bound

def frequentist_interval(sample, alpha):
    """Computes a 100(1-alpha)% confidence interval for the parameter"""
    x_bar = np.mean(sample)
    s = np.std(sample)
    n = len(sample)
    cv_of_z = stats.norm.isf(alpha / 2)
    lower_bound = x_bar - cv_of_z*(s/np.sqrt(n))
    upper_bound = x_bar + cv_of_z*(s/np.sqrt(n))
    return lower_bound, upper_bound
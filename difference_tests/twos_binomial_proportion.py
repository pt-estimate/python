"""Script to test difference in binomial proportions for two populations"""
from __future__ import division

import csv
import itertools
import math
import numpy as np
import sys


def csv_extract_binomial_parameters(csv_file):
    csv_file_object = csv.reader(open('/Users/chriswright/notebooks/notebook_data/phys_training.csv', 'rb'))
    header = csv_file_object.next()
    data=[]

    for row in csv_file_object:
        data.append(row[0:])
    data = np.array(data)
    n1, n2 = len(data[0::,0]), len(data[0::,1])
    s1, s2 = np.sum(data[0::,0].astype(np.int)), np.sum(data[::,1].astype(np.int))
    return n1, n2, s1, s2

def difference(n1, n2, s1, s2):
    """Compares two binomial proportions under the following assumptions:
       - p1_hat and p2_hat are independent
       - n1 and n2 are both large"""
    p1_hat = s1/n1
    p2_hat = s2/n2
    est_std = math.sqrt(p1_hat*(1-p1_hat)/n1 + p2_hat*(1-p2_hat)/n2)
    return (p1_hat - p2_hat)-1.96*est_std, (p1_hat - p2_hat)+1.96*est_std

def main():
    """Main entry point for the script."""
    csv_file = sys.argv[1] if len(sys.argv) >= 2 else None
    if csv_file:
        n1, n2, s1, s2 = csv_extract_binomial_parameters(csv_file)
    else:
        print "\nNo input file given, generating random binomial data for test."
        n1, n2 = 10, 10
        s1 = np.random.binomial(n1, p=0.3, size=1)
        s2 = np.random.binomial(n2, p=0.6, size=1)
    lb, ub = list(itertools.chain(*(difference(n1, n2, s1, s2))))
    print "\nWe are 95%% confident the difference in probabilities p1-p2 lies in the interval %f to %f.\nApproximately 95%% of the intervals calculated in this manner will contain the true difference." % (lb, ub)


if __name__ == '__main__':
    sys.exit(main())
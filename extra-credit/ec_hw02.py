
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# Homework 2: see hw/hw02/hw02.ipynb for question prompt
# ---------------------------------------------------------------------

def approx_median(fh, col, N, k):
    """
    Returns the approximate median of the
    col in a csv file object fh.

    :param fh: file handle with csv object
    :param col: column of csv to compute median
    :param N: chunksize
    :param k: median buffer size
    :returns: approximate median

    :Example:
    """

    return ...


def run_flight_experiments(fh, num_exper, N, k):
    """
    Runs ARRIVAL_DELAY approx_median experiment
    num_exper times for values N, k.
    :param fh: a file handle object of `flights.csv`
    :param num_exper: number of times to run experiment
    :param N: chunksize
    :param k: buffer size for median list
    :returns: 95% confidence interval of medians.

    :Example:
    """

    return ...


def approx_median_example():
    """

    returns a dataframe df with one column `col` 
    with the following property: 
    - the true median of df[col] is the max value df[col], 
    - the approximate median (N=100 and k=3) is the min value of df[col]
    :param:
    :returns: dataframe that has behavior described

    :Example:
    """

    return ...

# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q01': ['approx_median', 'run_flight_experiments', 'approx_median_example']
}


def check_for_graded_elements():
    """
    >>> check_for_graded_elements()
    True
    """
    
    for q, elts in GRADED_FUNCTIONS.items():
        for elt in elts:
            if elt not in globals():
                stmt = "YOU CHANGED A QUESTION THAT SHOULDN'T CHANGE! \
                In %s, part %s is missing" %(q, elt)
                raise Exception(stmt)

    return True


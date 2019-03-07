
import pandas as pd
import numpy as np
import os

# ---------------------------------------------------------------------
# Homework 6: see hw/hw02/hw02.ipynb for question prompt
# ---------------------------------------------------------------------


def descendants(comments):
    """
    
    :Example:
    >>> fp = os.path.join('data', 'hw06', 'comments.csv')
    >>> comments = pd.read_csv(fp, sep='|')
    >>> (descendants(comments) == np.array([4, 0, 2, 1, 0, 1, 0, 0])).all()
    True
    """

    return ...


def distinct_descendants(comments):
    """
    
    :Example:
    >>> fp = os.path.join('data', 'hw06', 'comments.csv')
    >>> comments = pd.read_csv(fp, sep='|')
    >>> (distinct_descendants(comments) == np.array([3, 0, 2, 1, 0, 1, 0, 0])).all()
    True
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
    'q01': ['descendants', 'distinct_descendants']
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


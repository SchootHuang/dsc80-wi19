
import pandas as pd
import numpy as np
import os

# ---------------------------------------------------------------------
# Homework 4: see hw/hw02/hw02.ipynb for question prompt
# ---------------------------------------------------------------------


def join_purch_visit(purch, webvisits):
    """
    approximately joins the purchases and webvisits data according
    to the condition specified in the HW.

    :Example:
    >>> fpurch = os.path.join('data', 'hw04', 'purch.csv')
    >>> fweb = os.path.join('data', 'hw04', 'webvisits.csv')
    >>> purch, webvisits = pd.read_csv(fpurch), pd.read_csv(fweb)
    >>> joined = join_purch_visit(purch, webvisits)
    >>> joined['email'].nunique() == len(joined)
    True
    """
    return ...


def revenue_by_url(joined):
    """
    Returns the revenue of each ad-campaign (web visit)

    :Example:
    >>> fpurch = os.path.join('data', 'hw04', 'purch.csv')
    >>> fweb = os.path.join('data', 'hw04', 'webvisits.csv')
    >>> purch, webvisits = pd.read_csv(fpurch), pd.read_csv(fweb)
    >>> joined = join_purch_visit(purch, webvisits)
    >>> out = revenue_by_url(joined)
    >>> isinstance(out, pd.Series)
    True
    >>> isinstance(out.iloc[0], float)
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
    'q01': ['join_purch_visit', 'revenue_by_url']
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


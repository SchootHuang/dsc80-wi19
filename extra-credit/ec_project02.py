
import pandas as pd
import numpy as np
import os

# ---------------------------------------------------------------------
# project 2: see projects/project02/project02.ipynb for question prompt
# ---------------------------------------------------------------------


def impute(college):
    """
    returns 101 columns: GRAD_DEBT_MDN_SUPP, and 100
    imputed C150_4_POOLED_SUPP columns.

    :Example:
    >>> fp = os.path.join('data', 'project02', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(fp).dropna(subset=['GRAD_DEBT_MDN_SUPP'])
    >>> out = impute(college)
    >>> len(out.columns) == 101
    True
    >>> out.isnull().any().any() == False
    True
    """

    return ...


def correlation_bootstrap(imputed):
    """
    returns the 95% confidence interval for correlations coefficients
    between the imputed C150_4_POOLED_SUPP and the GRAD_DEBT_MDN_SUPP.

    `imputed` should contain 101 columns: GRAD_DEBT_MDN_SUPP, and 100 
    imputed C150_4_POOLED_SUPP columns.

    :Example:
    >>> fp = os.path.join('data', 'project02', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(fp).dropna(subset=['GRAD_DEBT_MDN_SUPP'])
    >>> imputed = impute(college)
    >>> l, r = correlation_bootstrap(imputed)
    >>> l <= r
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
    'q01': ['impute', 'correlation_bootstrap']
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


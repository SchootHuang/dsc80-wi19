
import pandas as pd
import os



# ---------------------------------------------------------------------
# Homework 1: see hw/hw01/hw01.ipynb for Question # 10 prompt
# ---------------------------------------------------------------------

def cancel_cnt_airport(fh):
    """
    returns the number of cancelled flights for 
    each airport using out-of-memory techniques 
    (chunking; chunk-size=1000).

    :param fh: an open file object of a csv-file like `flights.csv`.
    :returns: a pd.Series, indexed by airport, of the 
    number of cancelled flights for each airport.

    :Example:
    >>> fp = os.path.join('data', 'hw01', 'flights.csv')
    >>> cancels = cancel_cnt_airport(open(fp))
    >>> isinstance(cancels, pd.Series)
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
    'q01': ['cancel_cnt_airport']
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


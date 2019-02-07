
import pandas as pd
import numpy as np
import matplotlib.path as mpltPath
from scipy.stats import linregress
import os
import json

# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------


def best_transformation():
    """

    :Example:
    >>> best_transformation() in [1,2,3,4]
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------


def prediction(population):
    """

    :Example:
    >>> d = {}
    >>> d["Time_in_Days"] = [0, 40, 70, 110, 140, 171, 181]
    >>> d["Population"] = [10, 20, 60, 160, 325, 890, 1112]
    >>> df = pd.DataFrame(d)
    >>> pred, choice = prediction(df)
    >>> pred > 0
    True
    >>> choice in [1,2,3]
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------


def latlong2geojson(route):
    """

    :Example:
    >>> path = os.path.join('data', 'aarons-day.txt')
    >>> data = pd.read_csv(path, sep='\\t')
    >>> gj = latlong2geojson(data)
    >>> types = set([x['geometry']['type'] for x in gj['features']])
    >>> types == set(['MultiLineString', 'Point'])
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------


def trajectory_distance(filepath):
    """
    
    :Example:
    >>> path = os.path.join('data', '20081023025304.plt')
    >>> dist = trajectory_distance(path)
    >>> 0 <= dist
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


def point_in_state(coord, state, geojson):
    """
    
    :Example:
    >>> path = os.path.join('data', 'states.geojson')
    >>> geojson = json.load(open(path))
    >>> coord = [32.881, -117.237]
    >>> point_in_state(coord, 'CA', geojson)
    True
    >>>
    """

    return ...


def label_state(coord, geojson):
    """

    :Example:
    >>> path = os.path.join('data', 'states.geojson')
    >>> geojson = json.load(open(path))
    >>> coord = [32.881, -117.237]
    >>> label_state(coord, geojson)
    'CA'
    """

    return 



# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q01': ['best_transformation'],
    'q02': ['prediction'],
    'q03': ['latlong2geojson'],
    'q04': ['trajectory_distance'],
    'q05': ['point_in_state', 'label_state'],
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

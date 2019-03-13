import os
import pandas as pd
import numpy as np
import requests
import json
import re

from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

def question1():
    """

    :return:
    """

    return ...


# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------


def order_classifiers():
    """

    :Example:
    >>> len(order_classifiers()) == 3
    True
    """
    return ...


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def null_hypoth():
    """
    :Example:
    >>> isinstance(null_hypoth(), list)
    True
    >>> set(null_hypoth()).issubset({1,2,3,4})
    True
    """

    return ...


def simulate_null():
    """
    :Example:
    >>> pd.Series(simulate_null()).isin([0,1]).all()
    True
    """

    return ...


def estimate_p_val(N):
    """
    >>> 0 < estimate_p_val(1000) < 0.1
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------



def simulate_searches(stops):
    """
    :Example:
    >>> fp = os.path.join('data', 'vehicle_stops_datasd.csv')
    >>> stops = pd.read_csv(fp)
    >>> sim = simulate_searches(stops)
    >>> set(stops.service_area.dropna().unique()) == set(sim().index)
    True
    >>> np.isclose(sim().sum(), 1.0)
    True
    """
    
    return ...


def tvd_sampling_distr(stops, N=1000):
    """
    :Example:
    >>> fp = os.path.join('data', 'vehicle_stops_datasd.csv')
    >>> stops = pd.read_csv(fp)
    >>> tvd = tvd_sampling_distr(stops, N=1)[0]
    >>> tvd <= 0.05
    True
    """

    return ...


def search_results():
    """
    :Example:
    >>> obs, reject = search_results()
    >>> obs <= 0.5
    True
    >>> isinstance(reject, bool)
    True
    """
    return ...

# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


def perm_test(stops, col='service_area'):
    """
    :Example:
    >>> fp = os.path.join('data', 'vehicle_stops_datasd.csv')
    >>> stops = pd.read_csv(fp)
    >>> out = perm_test(stops)
    >>> 0.005 < out < 0.025
    True
    """

    return ...


def obs_perm_stat(stops, col='service_area'):
    """
    :Example:
    >>> fp = os.path.join('data', 'vehicle_stops_datasd.csv')
    >>> stops = pd.read_csv(fp)
    >>> out = obs_perm_stat(stops)
    >>> 0.20 < out < 0.30
    True
    """

    return ...


def sd_res_missing_dependent(stops, N, col='service_area'):
    """
    :Example:
    >>> fp = os.path.join('data', 'vehicle_stops_datasd.csv')
    >>> stops = pd.read_csv(fp)
    >>> out = sd_res_missing_dependent(stops, 10)
    >>> out <= 0.01
    True
    """

    return ...


def sd_res_missing_cols():
    """
    :Example:
    >>> cols = sd_res_missing_cols()
    >>> 'service_area' in cols
    True
    >>> 'stop_cause' not in cols
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
    'q01': ['question1'],
    'q02': ['order_classifiers'],
    'q03': ['null_hypoth', 'simulate_null', 'estimate_p_val'],
    'q04': ['simulate_searches', 'tvd_sampling_distr', 'search_results'],
    'q05': ['perm_test', 'obs_perm_stat', 'sd_res_missing_dependent', 'sd_res_missing_cols']
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
                In %s, part %s is missing" % (q, elt)
                raise Exception(stmt)

    return True

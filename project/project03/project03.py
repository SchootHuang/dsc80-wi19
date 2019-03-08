
import os
import io
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, ClassifierMixin

from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------


def create_cat_feats():
    """
    :Example:
    >>> pl = create_cat_feats()
    >>> isinstance(pl, Pipeline)
    True
    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp)[['subject_sex']]
    >>> pl.fit(stops) # doctest:+ELLIPSIS
    Pipeline(...)
    >>> pl.transform(stops.iloc[0:1]).toarray().tolist()[0] == [0, 1, 0]
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------


def create_age_feats():
    """
    :Example:
    >>> pl = create_age_feats()
    >>> isinstance(pl, Pipeline)
    True
    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp)[['subject_age']]
    >>> pl.fit(stops) # doctest:+ELLIPSIS
    Pipeline(...)
    >>> pl.transform(stops.iloc[0:1])[0][0] == 20
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------


def baseline_model():
    """
    :Example:
    >>> pl = baseline_model()
    >>> isinstance(pl, Pipeline)
    True
    >>> isinstance(pl.steps[-1][-1], LogisticRegression)
    True
    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp).drop('searched', axis=1)
    >>> searched_fp = os.path.join('data', 'sample_imp_search.csv')
    >>> searched = pd.read_csv(searched_fp, names=['searched'], squeeze=True)
    >>> pl.fit(stops.iloc[:500], searched.iloc[:500]) # doctest:+ELLIPSIS
    Pipeline(...)
    >>> out = pl.predict(stops)
    >>> pd.Series(out).isin([0,1]).all()
    True
    """

    return ...


def train_test_acc(pl, stops, searched):
    """
    :Example:
    >>> pl = baseline_model()
    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp)
    >>> searched_fp = os.path.join('data', 'sample_imp_search.csv')
    >>> searched = pd.read_csv(searched_fp, names=['searched'], squeeze=True)
    >>> out = train_test_acc(pl, stops, searched)
    >>> np.isclose(out, 0.90, 0.1).all()
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------

def constant_model_acc(searched):
    """
    :Example:
    >>> searched_fp = os.path.join('data', 'sample_imp_search.csv')
    >>> searched = pd.read_csv(searched_fp, names=['searched'], squeeze=True)
    >>> 0.8 <= constant_model_acc(searched) <= 1.0
    True
    """
    return ...


def model_outcomes(predictions, target):
    """
    :Example:
    >>> out = model_outcomes(pd.Series([1,0,1,0]), pd.Series([0,1,1,0]))
    >>> (np.diag(out) == 1).all()
    True
    >>> set(out.columns) == {'FN', 'FP', 'TN', 'TP'}
    True
    """

    return ...


def metrics(predictions, target):
    """
    :Example:
    >>> out = metrics(pd.Series([1,0,1,0]), pd.Series([0,1,1,0]))
    >>> set(out.index) == {'acc', 'f1', 'fdr', 'fnr', 'fpr', 'precision', 'recall', 'specificity'}
    True
    >>> (out == 0.5).all()
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


class AdditiveSmoother(BaseEstimator, ClassifierMixin):
    """
    :Example:

    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp)
    >>> searched_fp = os.path.join('data', 'sample_imp_search.csv')
    >>> searched = pd.read_csv(searched_fp, names=['searched'], squeeze=True)
    >>> asm = AdditiveSmoother()
    >>> asm.fit(stops[['subject_sex']], searched)
    AdditiveSmoother(alpha=100)
    >>> np.isclose(asm.srate, 0.054)
    True
    >>> internal = asm.smdists['subject_sex']['M']
    >>> out = asm.transform(stops[['subject_sex']].iloc[[0]])[0][0]
    >>> np.isclose(internal, out)
    True
    """

    def __init__(self, alpha=100):
        self.alpha = alpha

    def fit(self, X, y, **kwargs):
        """
        Calculates the smoothed condition empirical 
        distributions of the columns of X dependent on y.
        In this case, y is searches in the stops data.
        """

        # calculate the search rate

        self.srate = ...

        smdists = {}
        ...
        ...
        # loop through the columns of X
        for c in ...:
            # create a smoothed empirical distribution for each column in X
            ...
            smoothed = ...
            smdists[c] = smoothed

        # smoothed empirical search rates in smdists
        self.smdists = smdists
        
        return self

    def transform(self, X):
        """
        Transforms the categorical values in the columns of X to
        the smoothed search rates of those values.
        """
        ...
        # loop through columns of X (categorical values)
        for c in ...:
            # create a column of smoothed search rates
            ...

        # return the array of smoothed search rates.
        return ...

    def get_params(self, deep=False):
        """
        Gets the parameters of the transformer;
        Allows Gridsearch to be used with class.
        """
        return {'alpha': self.alpha}


# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------


def final_model():
    """
    :Example:
    >>> pl = final_model()
    >>> isinstance(pl, Pipeline)
    True
    >>> isinstance(pl.steps[-1][-1], BaseEstimator)
    True
    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp).drop('searched', axis=1)
    >>> searched_fp = os.path.join('data', 'sample_imp_search.csv')
    >>> searched = pd.read_csv(searched_fp, names=['searched'], squeeze=True)
    >>> pl.fit(stops.iloc[:500], searched.iloc[:500]) # doctest:+ELLIPSIS
    Pipeline(...)
    >>> out = pl.predict(stops)
    >>> pd.Series(out).isin([0,1]).all()
    True

    """


    return ...


# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------

def compare_search_rate(stops, predictions, col):
    """
    :Example:
    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp)
    >>> randpred = np.random.choice([0,1], size=len(stops))
    >>> out = compare_search_rate(stops, randpred, 'hour')
    >>> set(out.columns) == {'searched', 'predicted'}
    True
    >>> (out.index == range(24)).all()
    True
    """
    
    return ...


def compare_metrics(stops, predictions, col):
    """
    :Example:
    >>> fp = os.path.join('data', 'sample_stops.csv')
    >>> stops = pd.read_csv(fp)
    >>> randpred = np.random.choice([0,1], size=len(stops))
    >>> out = compare_metrics(stops, randpred, 'hour')
    >>> 'precision' in out.columns
    True
    >>> (out.index == range(24)).all()
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
    'q01': ['create_cat_feats'],
    'q02': ['create_age_feats'],
    'q03': ['baseline_model','train_test_acc'],
    'q04': ['constant_model_acc', 'model_outcomes', 'metrics'],
    'q05': ['AdditiveSmoother'],
    'q06': ['final_model'],
    'q07': ['compare_search_rate', 'compare_metrics']
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

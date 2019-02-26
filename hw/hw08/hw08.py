import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score


# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------



def most_relevant(query, corpus):
    """
    :Example
    >>> fp = os.path.join('data', 'corpus.txt')
    >>> corpus = pd.read_csv(fp, header=None, squeeze=True)
    >>> query = ["relevance", "text relevance", "text relevance document", "text relevance document search"]
    >>> result = most_relevant(query, corpus)
    >>> type(result)
    <class 'pandas.core.series.Series'>
    >>> len(result)
    4
    >>> type(result[0])
    <class 'numpy.int64'>
    """

    return ...


# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------

def question2():
    """
    :Example
    >>> ans = question2()
    >>> isinstance(ans, list)
    True
    >>> len(ans)
    5
    >>> s = sum(ans)
    >>> isinstance(s, int)
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def pct_rare_or_common(corpus):
    """
    :Example:
    >>> fp = os.path.join('data', 'phone_reviews.text.txt')
    >>> reviews = [line.strip() for line in open(fp, encoding='utf8')]
    >>> out = pct_rare_or_common(reviews)
    >>> 0.50 < out < 0.70
    True
    """
    return ...

# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------

###### this will be given ####

def true_distribution(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(0)

sample_count = 50
noise_level = 0.1

random_noise = np.random.randn(sample_count) * noise_level    # creating noise
X = np.random.rand(sample_count)                              # creating random sample
y = true_distribution(X) + random_noise                       # adding noise
X_true = np.linspace(0, 1, 100)                               # uniform distribution from 0-1.

###############################

def degrees_and_mse():
    """
    :Example
    >>> result = degrees_and_mse()
    >>> isinstance(result, dict)
    True
    >>> len(result)
    3
    """
    degrees = []
    mse_errors = []
    plt.figure(figsize=(14, 5))
    for i in range(len(degrees)):
        ax = plt.subplot(1, len(degrees), i + 1)

        # Setting up the Pipeline

        # TODO


        # Evaluate the models using cross-validation

        # TODO


        # Train the model on the samples

        # TODO


        # Plotting

        # TODO

    return ...

# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


def tree_reg_perf(galton):
    """

    :Example:
    >>> galton_fp = os.path.join('data', 'galton.csv')
    >>> galton = pd.read_csv(galton_fp)
    >>> out = tree_reg_perf(galton)
    >>> out.columns.tolist() == ['train_err', 'test_err']
    True
    >>> out['train_err'].iloc[-1] < out['test_err'].iloc[-1]
    True
    """
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.model_selection import train_test_split

    return


def knn_reg_perf(galton):
    """
    :Example:
    >>> galton_fp = os.path.join('data', 'galton.csv')
    >>> galton = pd.read_csv(galton_fp)
    >>> out = knn_reg_perf(galton)
    >>> out.columns.tolist() == ['train_err', 'test_err']
    True
    """
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.model_selection import train_test_split

    return ...

# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------


def titanic_model(titanic):
    """
    :Example:
    >>> fp = os.path.join('data', 'titanic.csv')
    >>> data = pd.read_csv(fp)
    >>> pl = titanic_model(data)
    >>> isinstance(pl, Pipeline)
    True
    >>> from sklearn.base import BaseEstimator
    >>> isinstance(pl.steps[-1][-1], BaseEstimator)
    True
    >>> preds = pl.predict(data.drop('Survived', axis=1))
    >>> ((preds == 0)|(preds == 1)).all()
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------

def json_reader(file, iterations):
    """
    :Example
    >>> fp = os.path.join('data', 'reviews.json')
    >>> reviews, labels = json_reader(fp, 5000)
    >>> isinstance(reviews, list)
    True
    >>> isinstance(labels, list)
    True
    >>> len(labels) == len(reviews)
    True
    """
    return ...


def create_classifier_multi(X, y):
    """
    :Example
    >>> fp = os.path.join('data', 'reviews.json')
    >>> reviews, labels = json_reader(fp, 5000)
    >>> trial = create_classifier_multi(reviews, labels)
    >>> isinstance(trial, Pipeline)
    True

    """

    X_train, X_test, y_train, y_test = # TODO
    classifier = Pipeline(# TODO)


     # TODO

    return ...



def to_binary(labels):
    """
    :Example
    >>> lst = [1, 2, 3, 4, 5]
    >>> to_binary(lst)
    >>> print(lst)
    [0, 0, 0, 1, 1]
    """
    ...


def create_classifier_binary(X, y):
    """
    :Example
    >>> fp = os.path.join('data', 'reviews.json')
    >>> reviews, labels = json_reader(fp, 5000)
    >>> to_binary(labels)
    >>> trial = create_classifier_multi(reviews, labels)
    >>> isinstance(trial, Pipeline)
    True

    """

    return ...

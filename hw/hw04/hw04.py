
import pandas as pd
import numpy as np
import re
import os

# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

def earliest_login(login):
    """Calculates the earliest login time for each user
    :param login: a dataframe with login information
    :return: a dataframe with earliest login time for each user indexed by "Login Id"
    >>> login = pd.read_csv("data/login_table.csv")
    >>> result = earliest_login(login)
    >>> len(result)
    433
    >>> result.loc[381, "Time"].hour > 12
    False
    """
    return ...



# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------

def smallest_ellapsed(login):
    """
    Calculates the the smallest time elapsed for each user.
    :param login: a dataframe with login information but without unique IDs
    :return: a dataframe, indexed by Login ID, containing the smallest time elapsed for each user.
    >>> login = pd.read_csv("data/login_table.csv")
    >>> result = smallest_ellapsed(login)
    >>> len(result)
    238
    >>> 18 < result.loc[1233, "Time"].days < 23
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def day_of_the_week(login):
    """
    Calculates the most common day of login for each user. Then calculates the busiest day over
    all users.
    :param login: a dataframe with login information
    :return: a tuple with a series, indexed by Login ID, containing the busiest day for each user.
    Represent day as a string; and the most popular day overall, as a string.
    >>> login = pd.read_csv("data/login_table.csv")
    >>> result = day_of_the_week(login)
    >>> result[1]!= "Sunday"
    True
    >>> type(result[0])
    <class 'pandas.core.series.Series'>
    >>> len(result[0].loc[472]) == 2
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------

def day_time(login):
    """
    Calculates time of the day for each user based on the hour only.
    :param login: a dataframe with login information
    :return: returns a copy of the given dataframe plus additional column that
    indicates whether a given time belongs to the "Night", "Morning",
    "Afternoon", or "Evening" category.
    >>> login = pd.read_csv("data/login_table.csv")
    >>> result = day_time(login)
    >>> len(result)
    3003
    >>> result["timeOfDay"].value_counts()["Night"]
    24
    """

    return ...


# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


def snippet_occurence(snip_list, text):
    """
    Finds the empirical and smoothed probabilities that
    a snippet occurs in a given text.

    :param snip_list: list of snippets that contain only two words.
    :return: a data frame, where each row is index by the snippet
    and the columns represents the empirical and smoothed probabilities
    for each snippet.
    >>> text = open('data/tomsawyer.txt').read()
    >>> result  = snippet_occurence(["in this", "that is", "likes me", "likes you"], text)
    >>> num = result.loc["in this", "Empirical"]
    >>> 0.02 < num < 0.025
    True
    >>> num = result.Smoothed.sum()
    >>> 0.0040 < num < 0.0045
    True
    """

    return ...



# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------

def payments_missingness():
    """
    Returns a list of integers of corresponding
    to correct responses to the `payments` dataset.

    >>> L = payments_missingness()
    >>> isinstance(L, list)
    True
    >>> 1 <= len(L) <= 4
    True
    >>> all(map(lambda x:type(x) == int, L))
    True
    """
    
    return ...


def car_missingness():
    """
    Returns a list of integers of corresponding
    to correct responses to the `payments` dataset.

    >>> L = car_missingness()
    >>> isinstance(L, list)
    True
    >>> 1 <= len(L) <= 4
    True
    >>> all(map(lambda x:type(x) == int, L))
    True

    """

    return ...


# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------

def mins_after_hour(stops):
    """
    mins_after_hour takes in a dataframe `stops` and outputs a series, 
    indexed by minutes after the hour, that gives the percentage of 
    stops that occurred that many minutes after the hour.

    :Example:
    >>> stops = pd.read_csv(os.path.join('data', 'stops.test.csv'))
    >>> out = mins_after_hour(stops)
    >>> out.sum()
    1.0
    >>> 0 in out.index[:5]
    True
    """

    return ...


def avg_age_per_hour(stops):
    """
    avg_age_per_hour takes in the stops data, 
    computes the average age of stops over a 
    3 hour rolling window, and returns the average 
    age of a driver for each hour of the day as a Series.

    :Example:
    >>> stops = pd.read_csv(os.path.join('data', 'stops.test.csv'))
    >>> out = avg_age_per_hour(stops)
    >>> isinstance(out, pd.Series)
    True
    >>> set(out.index) == set(range(24))
    True
    >>> (30 <= out).values.all() and (out < 42).values.all()
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------


def plot_search(stops):
    """
    plot_search that takes in a dataframe like stops 
    and returns an array of two matplotlib.axes subplots 
    that depicts two vertically stacked plots:
    - the top displaying a bar chart of the number of traffic 
    stops per subject_race, and
    - the bottom displaying a bar chart of search rates by subject_race.

    :Example:
    >>> stops = pd.read_csv(os.path.join('data', 'stops.test.csv'))
    >>> ax = plot_search(stops)
    >>> len(ax)
    2
    >>> ax[0].get_title() == 'number of stops'
    True
    >>> list(ax[1].get_xticklabels())[0].get_text()
    'A'
    """

    return ...


def smoothed_search_rates(stops, alpha):
    """
    smoothed_search_rates takes in stops data 
    and a parameter alpha and returns a Series 
    indexed by subject_race of the smoothed 
    search rates for each value of subject_race.
    
    :Example:
    >>> stops = pd.read_csv(os.path.join('data', 'stops.test.csv'))
    >>> out = smoothed_search_rates(stops, 100)
    >>> isinstance(out, pd.Series)
    True
    >>> 'A' in set(out.index)
    True
    >>> 0.01 <= out['A'] < 0.05
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 9
# ---------------------------------------------------------------------


def sd_res_missingness(stops, col):
    """
    sd_res_missingness that takes in the stops dataset 
    and a column col, and returns the Total Variational Distance 
    between the following two distributions:
    - the empirical distribution of col conditional on 
    sd_resident being null, and
    - the empirical distribution of col conditional on 
    sd_resident being non-null.

    :Example:
    >>> stops = pd.read_csv(os.path.join('data', 'stops.test.csv'))
    >>> out = sd_res_missingness(stops, 'service_area')
    >>> 0.4 >= out >= 0.2
    True
    """

    return ...



def fill_sd_res_mcar(stops):
    """
    `fill_sd_res_mcar` that takes in the stops data and 
    outputs a column (the 'imputed `sd_resident`') that 
    satisfies the following conditions:
    - The output column of `fill_sd_res_mcar` is either 0 or 1,
    - non-null entries of `sd_resident` remain unchanged,
    - the output has *almost* the same mean as the unimputed `sd_resident` column.

    :Example:
    >>> stops = pd.read_csv(os.path.join('data', 'stops.test.csv'))
    >>> out = fill_sd_res_mcar(stops)
    >>> len(out) == 1000
    True
    >>> (out.unique() == np.array([0,1])).all()
    True
    """


    return ...


def fill_sd_res_mar(stops):
    """
    `fill_sd_res_mar` that takes in a row of the stops data 
    and outputs a value (the 'imputed `sd_resident`') that 
    satisfies the following conditions:
    - The output column of `fill_sd_res_mar` is either 0 or 1,
    - non-null entries of `sd_resident` remain unchanged,
    - the output has *almost* the same mean as the unimputed `sd_resident` column.
    - The condition above remains true when grouping by `service_area`.

    :Example:
    >>> stops = pd.read_csv(os.path.join('data', 'stops.test.csv'))
    >>> out = fill_sd_res_mar(stops)
    >>> len(out) == 1000
    True
    >>> (out.unique() == np.array([0,1])).all()
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
    'q01': ['earliest_login'],
    'q02': ['smallest_ellapsed'],
    'q03': ['day_of_the_week'],
    'q04': ['day_time'],
    'q05': ['snippet_occurence'],
    'q06': ['payments_missingness', 'car_missingness'],
    'q07': ['mins_after_hour', 'avg_age_per_hour'],
    'q08': ['plot_search', 'smoothed_search_rates'],
    'q09': ['sd_res_missingness', 'fill_sd_res_mcar', 'fill_sd_res_mar']
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


import pandas as pd
import numpy as np



# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

def non_quant_numeric():
    """
    Returns non-quantitative, numeric variables.

    :returns: a list of column names, that are numeric by notnull
    quantitative.

    :Example:
    >>> isinstance(non_quant_numeric(), list)
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------

def depart_arrive_stats(flights):
    """

    depart_arrive_stats calculates the following 
    quantities in a list (in the given order):
    - The proportion of flights from/to SAN that 
    leave late, but arrive early or on-time.
    - The proportion of flights from/to SAN that 
    leaves early, or on-time, but arrives late.
    The proportion of flights from/to SAN that both 
    left late and arrived late.
    :param flights: a dataframe similar to `flights`.
    :returns: a list as described above.

    :Example:
    >>> stats = depart_arrive_stats(pd.read_csv('flights.csv', nrows=100))
    >>> isinstance(stats, list)
    True
    >>> (np.array(stats) <= 1).all().all()
    True
    >>> (np.array(stats) >= 0).all().all()
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def trip_breakdown(flights):
    """

    trip_breakdown returns a dataframe with columns named 
    TIME_AT_AIRPORT, TAXI_OUT, AIR_TIME, TAXI_IN, ARRIVAL_DELAY.
    - The first four columns should contain the proportion of the 
    trip spent in each of the four activities.
    - The last column should contain the proportion of the trip 
    that's attributable to delay-related reasons.

    :param flights: a dataframe similar to `flights`.
    :returns: a dataframe as described above.

    :Example:
    >>> out = trip_breakdown(pd.read_csv('flights.csv', nrows=100))
    >>> 'TIME_AT_AIRPORT' in out.columns
    True
    >>> (out.dropna() <= 1).all().all() and (out.drop('ARRIVAL_DELAY', axis=1).dropna() >= 0).all().all()
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------

def prop_non_null(flights):
    """

    prop_non_null a series whose values are the proportion 
    of each field of flights which are non-null.

    :param flights: a dataframe similar to `flights`
    :returns: a series as described above.

    :Example:
    >>> out = prop_non_null(pd.read_csv('flights.csv', nrows=100))
    >>> isinstance(out, pd.Series)
    True
    >>> (out <= 1).all().all() and (out >= 0).all().all()
    True
    """

    return ...


def missing_types():
    """

    missing_types returns a Series, 
    - indexed by the following columns of flights: 
    CANCELLED, AIRLINE_DELAY, CANCELLATION_REASON, TAIL_NUMBER.
    - The values contain the most-likely missingness type of each column.
    - The unique values of this Series should be MD, MCAR, MAR, MNAR, NaN.

    :param:
    :returns: A series with index and values as described above.

    :Example:
    >>> out = missing_types()
    >>> isinstance(out, pd.Series)
    True
    >>> set(out.unique()) - set(['MD', 'MCAR', 'MAR', 'MNAR', np.NaN]) == set()
    True
    """

    return ...


def predict_null(row):
    """
    predict_null takes in a row of the flights data 
    (that is, a Series) and returns True if the 
    ARRIVAL_DELAY is null and otherwise False. Since the 
    function doesn't depend on ARRIVAL_DELAY, it should 
    work a row even if that index is dropped.

    :param row: a Series that represents a row of `flights`
    :returns: a boolean representing when `ARRIVAL_DELAY` is null.

    :Example:
    >>> flights = pd.read_csv('flights.csv', nrows=100)
    >>> out = flights.drop('ARRIVAL_DELAY', axis=1).apply(predict_null, axis=1)
    >>> set(out.unique()) - set([True, False]) == set()
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------

def cnts_by_airline_dow(flights):
    """
    cnts_by_airline_dow that takes in a dataframe 
    like flights and outputs a dataframe with
    - a column for each distinct value of AIRLINE,
    - a row for each day of the week, and
    - entries that give the total number of flights 
    that airline has on that day of the week over 2015.
    :param flights: a dataframe similar to flights.
    :returns: a dataframe of counts as above.

    :Example:
    >>> flights = pd.read_csv('flights.csv', nrows=100)
    >>> out = cnts_by_airline_dow(flights)
    >>> set(out.columns) == set(flights['AIRLINE'].unique())
    True
    >>> set(out.index) == set(flights['DAY_OF_WEEK'].unique())
    True
    >>> (out >= 0).all().all()
    True
    """

    return ...


def mean_by_airline_dow(flights):
    """

    mean_by_airline_dow that takes in a dataframe 
    like flights and outputs a dataframe with
    - a column for each distinct value of AIRLINE,
    - a row for each day of the week, and
    - entries that give the average ARRIVAL_DELAY for 
    the flights of each airline on that day of the week.

    :param flights: a dataframe similar to `flights`.
    :returns: a dataframe of means as above.

    :Example:
    >>> flights = pd.read_csv('flights.csv', nrows=100)
    >>> out = mean_by_airline_dow(flights)
    >>> set(out.columns) == set(flights['AIRLINE'].unique())
    True
    >>> set(out.index) == set(flights['DAY_OF_WEEK'].unique())
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------

def prop_delayed_by_airline(jb_sw):
    """

    prop_delayed_by_airline that takes in a dataframe 
    like jb_sw and returns a DataFrame indexed by airline 
    that contains the proportion of each airline's flights 
    that are delayed.

    :param jb_sw: a dataframe similar to jb_sw
    :returns: a dataframe as above

    :Example:
    >>> jb_sw = pd.read_csv('southwest_vs_jetblue.csv', nrows=100)
    >>> out = prop_delayed_by_airline(jb_sw)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> (out >= 0).all().all() and (out <= 1).all().all()
    True
    >>> len(out.columns) == 1
    True
    """

    return ...


def prop_delayed_by_airline_airport(jb_sw):
    """
    prop_delayed_by_airline_airport that takes in a 
    dataframe like jb_sw and returns a DataFrame, with 
    columns given by airports, indexed by airline, that 
    contains the proportion of each airline's flights 
    that are delayed at each airport.

    :param jb_sw: a dataframe similar to jb_sw
    :returns: a dataframe as above.

    :Example:
    >>> jb_sw = pd.read_csv('southwest_vs_jetblue.csv', nrows=100)
    >>> out = prop_delayed_by_airline_airport(jb_sw)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> ((out >= 0) | (out <= 1) | (out.isnull())).all().all()
    True
    >>> len(out.columns) == jb_sw['ORIGIN_AIRPORT'].nunique()
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------


def verify_simpson(df, group1, group2, occur):
    """
    Verifies that a dataset displays Simpson's Paradox.

    :param df: a dataframe
    :param group1: the first group being aggregated
    :param group2: the second group being aggregated
    :param occur: a column of df with values {0,1}, denoting
    if an event occured.
    :returns: a boolean. True if simpson's paradox is present,
    otherwise False.

    :Example:
    >>> df = pd.DataFrame([[4,2,1], [1,2,0], [1,4,0], [4,4,1]], columns=[0,1,2])
    >>> verify_simpson(df, 0, 1, 2) in [True, False]
    True
    >>> verify_simpson(df, 0, 1, 2)
    False
    """
    
    return ...


# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------

def translation_dict(datadict):
    """

    translation_dict  outputs a dictionary satisfying 
    the following conditions:
    - The keys are the column names of colleges that are 
    strings encoded as integers (i.e. columns for which 
    VALUE and LABEL in datadict are non-empty).
    - The values are also dictionaries; each has keys 
    given by VALUE and values LABEL.

    :param datadict: a dataframe like `datadict`.
    :returns: a dictionary of key-value correspondences

    :Example:
    Make your own!
    """

    return ...



# ---------------------------------------------------------------------
# Question # 9
# ---------------------------------------------------------------------

def merge_cost(colleges):
    """

    merge_cost that takes in a dataframe like colleges
    and outputs a column that contains average net price 
    for both public and private Title IV institutions.
    :param colleges: a dataframe like colleges.
    :returns: a Series containing average net price

    :Example:
    >>> df = pd.DataFrame([[1,np.NaN],[np.NaN,1]], columns=['NPT4_PUB', 'NPT4_PRIV'])
    >>> merge_cost(df).sum() == 2
    True
    """
    return ...


def missing_cost_prop(colleges, title4):
    """

    missing_cost_prop that takes in a dataframe like colleges 
    and a dataframe like title4 and returns a list with 
    two elements (in the following order):
    - What proportion of institutions don't report their average net price?
    - What proportion of those not reporting their average net 
    price are title IV institutions?

    :param colleges: a dataframe like colleges
    :param titl4: a dataframe like title4
    :returns: list as above.

    :Example:
    Make you own!
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
    'q01': ['non_quant_numeric'],
    'q02': ['depart_arrive_stats'],
    'q03': ['trip_breakdown'],
    'q04': ['prop_non_null', 'missing_types', 'predict_null'],
    'q05': ['cnts_by_airline_dow', 'mean_by_airline_dow'],
    'q06': ['prop_delayed_by_airline', 'prop_delayed_by_airline_airport'],
    'q07': ['verify_simpson'],
    'q08': ['translation_dict'],
    'q09': ['merge_cost', 'missing_cost_prop']
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

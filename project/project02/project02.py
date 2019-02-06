
import os
import io
import pandas as pd
import numpy as np

BASIC_COLS = ['UNITID', 'OPEID', 'OPEID6', 
              'INSTNM', 'ZIP', 'LATITUDE', 
              'LONGITUDE', 'CONTROL', 'PREDDEG', 'UGDS']

# ---------------------------------------------------------------------
# Question # 1
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
    >>> datadict_path = os.path.join('data', 'CollegeScorecardDataDictionary.xlsx')
    >>> datadict = pd.read_excel(datadict_path, sheet_name='data_dictionary')
    >>> d = translation_dict(datadict)
    >>> len(d.keys())
    28
    >>> set(d['PREDDEG'].keys()) == set([0,1,2,3,4])
    True
    >>> 'Not classified' in d['PREDDEG'].values()
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------


def basic_stats(college):
    """

    basic_stats takes in college and returns 
    a Series of the above statistics index by:
    ['num_schools', 'num_satellite', 'num_students', 'avg_univ_size']

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = basic_stats(college)
    >>> out.index[0] == 'num_schools'
    True
    >>> out['num_students'] > 10**6
    True
    """

    return ...


def plot_school_sizes(college):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> ax = plot_school_sizes(college)
    >>> ax.get_ylabel()
    'Frequency'
    """
    return ...

# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------


def num_of_small_schools(college, k):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> nschools = len(college)
    >>> out = num_of_small_schools(college, nschools - 1)
    >>> out == (len(college) - 1)
    True
    >>> import numbers
    >>> isinstance(num_of_small_schools(college, 2), numbers.Integral)
    True
    """
    return ...


# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------


def col_pop_stats(college, col):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = col_pop_stats(college, "PREDDEG")
    >>> (out.columns == ['size', 'sum', 'mean', 'median']).all()
    True
    >>> (out.index == [1,2,3]).all()
    True
    >>> (out > 0).all().all()
    True
    """

    return ...


def col_pop_stats_plots(stats, datadict):
    """

    :Example:
    >>> datadict_path = os.path.join('data', 'CollegeScorecardDataDictionary.xlsx')
    >>> datadict = pd.read_excel(datadict_path, sheet_name='data_dictionary')
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = col_pop_stats(college, "PREDDEG")
    >>> ax = col_pop_stats_plots(out, datadict)
    >>> len(ax)
    4
    >>> ax[-1].get_title()
    'median'
    """
    return ...


# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


def control_preddeg_stats(college, f):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = control_preddeg_stats(college, lambda x:1)
    >>> (out == 1).all().all()
    True
    >>> out.index.name
    'CONTROL'
    >>> out.columns.name
    'PREDDEG'
    """

    return ...


def control_preddeg_stats_plot(out, datadict):
    """
    :Example:
    >>> datadict_path = os.path.join('data', 'CollegeScorecardDataDictionary.xlsx')
    >>> datadict = pd.read_excel(datadict_path, sheet_name='data_dictionary')
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = control_preddeg_stats(college, lambda x:1)
    >>> ax = control_preddeg_stats_plot(out, datadict)
    >>> ax.get_children()[0].get_height()
    1
    >>> ax.get_xlabel()
    'CONTROL'
    """

    return ...


# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------

def scatterplot_us(college):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> ax = scatterplot_us(college)
    >>> ax.get_xlabel()
    'LONGITUDE'
    >>> ax.get_title()
    'Undergraduate Institutions'
    >>>
    

    """

    return ...

# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------


def plot_folium():
    """

    :Example:
    >>> d = plot_folium()
    >>> isinstance(d, dict)
    True
    >>> 'geo_data' in d.keys()
    True
    >>> isinstance(d.get('key_on'), str)
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------


def control_type_by_state(college):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = control_type_by_state(college)
    >>> len(out)
    49
    >>> np.allclose(out.sum(axis=1), 1)
    True
    """

    return ...


def tvd_states(college):
    """
    
    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = tvd_states(college)
    >>> len(out)
    49
    >>> 'NV' in out.index[:5]
    True
    >>> 'OR' in out.index[-5:]
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 9
# ---------------------------------------------------------------------

def num_subjects(college):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = num_subjects(college)
    >>> len(out) == len(college)
    True
    >>> out.nunique()
    34
    """

    return ...


def subject_counts(college):
    """

    :Example:
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = subject_counts(college)
    >>> len(out)
    34
    >>> out.loc[0].sum() == 3060
    True
    """
    return ...


def create_specialty(college, datadict):
    """

    :Example:
    >>> datadict_path = os.path.join('data', 'CollegeScorecardDataDictionary.xlsx')
    >>> datadict = pd.read_excel(datadict_path, sheet_name='data_dictionary')
    >>> college_path = os.path.join('data', 'MERGED2016_17_PP.csv')
    >>> college = pd.read_csv(college_path)
    >>> out = create_specialty(college, datadict)
    >>> len(out.columns) == len(college.columns) + 1
    True
    >>> 'Psychology' in out['SPECIALTY'].unique()
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
    'q01': ['translation_dict'],
    'q02': ['basic_stats', 'plot_school_sizes'],
    'q03': ['num_of_small_schools'],
    'q04': ['col_pop_stats', 'col_pop_stats_plots'],
    'q05': ['control_preddeg_stats', 'control_preddeg_stats_plot'],
    'q06': ['scatterplot_us'],
    'q07': ['plot_folium'],
    'q08': ['control_type_by_state', 'tvd_states'],
    'q09': ['num_subjects', 'subject_counts', 'create_specialty']
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

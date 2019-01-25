
import pandas as pd
import numpy as np
import glob
import os

# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

def major_drop(df):
    """
    major_drop removes the columns specified in the write up
    :param dataframe: pandas dataframe
    :returns: an updated table
    :Example:
    >>> grades = pd.read_csv("grades.csv")
    >>> result = major_drop(grades)
    >>> result.shape[1]
    25
    """

    return ...


# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------

def merged_exams(df):
    """
    major_drop removes the columns specified in the write up
    :param dataframe: pandas dataframe
    :returns: an updated table
    :Example:
    >>> grades = pd.read_csv("grades.csv")
    >>> grades = major_drop(grades)
    >>> result = merged_exams(grades)
    >>> result.shape[1]
    22
    """


    return ...


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def read_all(dirname):
    """
    Finds and reads .csv files from the timeData directory
    :param dirname: Directory with the files
    :return: List of dataframes
    >>> output = read_all('timeData')
    >>> len(output)
    10
    """
    return ...




def extract_and_create(hws):
    """
    :param hws: list of dataframes
    :return: dataframe with two columns that represent penalties for 20 and 50%
    >>> hws = read_all('timeData')
    >>> df = extract_and_create(hws)
    >>> df.loc[:, "Penalty_20"].max()
    5
    """
    return ...



# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------


def compute_stats(fh1, fh2, fh3):
    """
    >>> fh1, fh2, fh3 = open('linkedin1.csv'), open('linkedin2.csv'), open('linkedin3.csv')
    >>> out = compute_stats(fh1, fh2, fh3)
    >>> set(map(lambda x:isinstance(x, str), out)) == {True}
    True
    >>> len(out)  # first name, job, slogan, animal
    4
    """

    return ...



# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


def job_word_distribution(jobtitles):
    """
    >>> salaries = pd.read_csv('san-diego-2017.csv')
    >>> jobtitle = salaries['Job Title']
    >>> out = job_word_distribution(jobtitle)
    >>> 'Police' in out.index
    True
    >>> set(map(lambda x:x.count(' ') == 0, out.index)) == {True}
    True
    >>> (len(out) >= 500) and (len(out) <= 550) # number of distinct words
    True
    """

    return ..



def describe_salaries_by_job_type(salaries):
    """
    >>> salaries = pd.read_csv('san-diego-2017.csv')
    >>> out = describe_salaries_by_job_type(salaries)
    >>> (out.columns == ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']).all()
    True
    """
    return ...


def std_salaries_by_job_type(salaries):
    """
    >>> salaries = pd.read_csv('san-diego-2017.csv')
    >>> out = std_salaries_by_job_type(salaries)
    >>> set(out.columns) == set(['Base Pay', 'Overtime Pay', 'Total Pay', 'Job Type'])
    True
    >>> np.all(abs(out.select_dtypes(include='number').mean()) < 10**-7)  # standard units should average to 0!
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------

def bucket_total_pay(totpay):
    """
    >>> salaries = pd.read_csv('san-diego-2017.csv')
    >>> out = bucket_total_pay(salaries['Total Pay'])
    >>> set(np.unique(out)) == set(range(1,11))
    True
    >>> np.all(np.abs(np.histogram(out)[0] - out.size/10) < 1)  # equal bin sizes!
    True
    """

    return ...


def mean_salary_per_decile(salaries):
    """
    >>> salaries = pd.read_csv('san-diego-2017.csv')
    >>> out = mean_salary_per_decile(salaries)
    >>> len(out) == 10
    True
    >>> 50000 <= out[5] <= 60000
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------


def robo_table(phones):
    """
    >>> phones = pd.read_csv('phones.csv')
    >>> out = robo_table(phones)
    >>> set(out.columns) == set(['id', 'first_name', 'last_name', 'phone'])
    True
    >>> _ = out.phone.dropna().astype(int)
    """

    return ...

# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------


def read_names(dirname):
    """
    >>> out = read_names('names')
    >>> set(out.columns) == set(['first_name', 'sex', 'number', 'year'])
    True
    >>> out.year.nunique()
    138
    """

    return ...


def age_guess(names):
    """
    >>> cols = ['first_name', 'sex', 'number', 'year']
    >>> data = [['Al', 'M', 100, 1971], ['Al', 'M', 60, 1952]]
    >>> names = pd.DataFrame(data, columns=cols)
    >>> out = age_guess(names)
    >>> isinstance(out, pd.Series)
    True
    >>> out.loc['Al']
    48
    """

    return ...


def get_age_group(phones, ages):
    """
    >>> cols = ['first_name', 'sex', 'number', 'year']
    >>> data = [['Al', 'M', 100, 1971], ['Al', 'M', 60, 1952]]
    >>> names = pd.DataFrame(data, columns=cols)
    >>> phones = pd.read_csv('phones.csv')
    >>> out = get_age_group(phones, age_guess(names))
    >>> set(phones.columns) == set(out.columns)
    True
    >>> 'Al' in out['first_name'].unique()
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
    'q01': ['major_drop'],
    'q02': ['merged_exams'],
    'q03': ['read_all', 'extract_and_create'],
    'q04': ['compute_stats'],
    'q05': [
        'job_word_distribution',
        'describe_salaries_by_job_type', 
        'std_salaries_by_job_type'
    ],
    'q06': ['bucket_total_pay', 'mean_salary_per_decile'],
    'q07': ['convert_phone', 'robo_table'],
    'q08': ['read_names', 'age_guess', 'get_age_group']
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

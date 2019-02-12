import os
import pandas as pd
import numpy as np
import requests
import bs4
import time

# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

# None

# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------

def answers():
    """
    Returns two lists with your answers
    :return: Two lists: one with your answers to multiple choice questions
    and the second list has 6 websites that satisfy given requirements.
    >>> list1, list2 = answers()
    >>> len(list1)
    4
    >>> len(list2)
    6
    """
    return ...

# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------


def find_countries(url):
    """
    Scrapes the site to extract the name of the countries.
    :param url:
    :return: dataframe with all countries listed in a column
    # >>> url = "http://example.webscraping.com/"
    # >>> df = find_countries(url)
    # >>> df.shape
    (252, 1)
    """

    return ...


def first_letters_count(df):
    """
    Counts number of countries that begin with the same letter
    :param df:
    :return: dataframe, indexed by a capital letter and the column
             containing the number of countries starting from this letter

    :Example:
    >>> fp = os.path.join('data', 'countries-sample.csv')
    >>> df = pd.read_csv(fp)
    >>> counts = first_letters_count(df)
    >>> counts.shape
    (7, 1)
    """
    return ...


# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------


def extract_book_links(text):
    """
    :Example:
    >>> fp = os.path.join('data', 'products.html')
    >>> out = extract_book_links(open(fp).read())
    >>> url = 'scarlet-the-lunar-chronicles-2_218/index.html'
    >>> out[0] == url
    True
    """
    
    return ...


def get_product_info(text):
    """
    :Example:
    >>> fp = os.path.join('data', 'Frankenstein.html')
    >>> out = get_product_info(open(fp).read())
    >>> isinstance(out, dict)
    True
    >>> 'UPC' in out.keys()
    True
    >>> out['Rating']
    'Two'
    """
    
    return ...


def scrape_books(k):
    """
    :param k: number of book-listing pages to scrape.
    :returns: a dataframe of information on (certain) books
    on the k pages (as described in the question).

    :Example:
    >>> out = scrape_books(1)
    >>> out.shape
    (1, 10)
    >>> out['Rating'][0] == 'Five'
    True
    >>> out['UPC'][0] == 'ce6396b0f23f6ecc'
    True
    """
        
    return ...

# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------


def depth(comments):
    """
    
    :Example:
    >>> fp = os.path.join('data', 'comments.csv')
    >>> comments = pd.read_csv(fp, sep='|')
    >>> (depth(comments) == [1, 2, 2, 3, 4, 1, 2, 1]).all()
    True
    """

    return ...


def descendants(comments):
    """
    
    :Example:
    >>> fp = os.path.join('data', 'comments.csv')
    >>> comments = pd.read_csv(fp, sep='|')
    >>> (descendants(comments) == [4, 0, 2, 1, 0, 1, 0, 0]).all()
    True
    """

    return ...


def distinct_descendants(comments):
    """
    
    :Example:
    >>> fp = os.path.join('data', 'comments.csv')
    >>> comments = pd.read_csv(fp, sep='|')
    >>> (distinct_descendants(comments) == [3, 0, 2, 1, 0, 1, 0, 0]).all()
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
    'q01': [],
    'q02': ['answers'],
    'q03': ['find_countries', 'first_letters_count'],
    'q04': ['extract_book_links', 'get_product_info', 'scrape_books'],
    'q05': ['depth', 'descendants', 'distinct_descendants']
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

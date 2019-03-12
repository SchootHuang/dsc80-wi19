
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_perm_test_mean(df, labcol, distcol, n=500):

    # calculate observed difference
    observed_difference = (
        df
        .groupby(labcol)[distcol]
        .mean()
        .diff()
        .iloc[-1]
    )
    
    differences = []
    for _ in range(n):

        # shuffle the weights
        shuffled_distr = (
            df[distcol]
            .sample(replace=False, frac=1)
            .reset_index(drop=True)
        )

        # put them in a table
        shuffled = df.assign(**{'Shuffled Distr': shuffled_distr})

        # compute the group differences
        group_means = (
            shuffled
            .groupby(labcol)
            .mean()
            .loc[:, 'Shuffled Distr']
        )

        difference = (group_means.diff().iloc[-1])

        # add it to the list of results
        differences.append(difference)

    return observed_difference, differences


# plotting PDF vs CDF for KS

def plt_gp(df):

    b = np.arange(0, 100, 5)
    cnts, bins = np.histogram(df.age.dropna(), bins=b)
    return pd.concat([
        pd.Series(cnts / np.sum(cnts), index=bins[1:]).rename('pdf'),
        pd.Series(np.cumsum(cnts / np.sum(cnts)), index=bins[1:]).rename('cdf')
    ], axis=1)


def plot_pdf_cdf(payments):

    fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    (
        payments
        .groupby('cc_isnull')
        .apply(plt_gp)
        .reset_index()
        .rename(columns={'level_1': 'age'})
        .pivot('age', 'cc_isnull', 'pdf')
        .plot(kind='bar', ax=axes[0], title='distribution of ages')
    )

    (
        payments
        .groupby('cc_isnull')
        .apply(plt_gp)
        .reset_index()
        .rename(columns={'level_1': 'age'})
        .pivot('age', 'cc_isnull', 'cdf')
        .plot(kind='bar', ax=axes[1])
    )

    return axes

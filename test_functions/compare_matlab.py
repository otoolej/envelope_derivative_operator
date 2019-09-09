"""
functions to load test files (.csv) from Matlab-generated EDO and compare with this Python
implementation

John M. O' Toole, University College Cork
Started: 04-09-2019
last update: Time-stamp: <2019-09-04 13:36:39 (otoolej)>
"""

from energy_operators import edo as ed
from matplotlib import pyplot as plt
import pandas as pd


def load_file_and_compare(fname_x, fname_y, DBplot=False):
    """
    load test signals and matlab EDO values and compare

    Parameters
    ----------
    fname_x: string
        name of file with test signal
    fname_y: string
        name of file with Matlab-version of EDO
    DBplot: bool
        plot or not
    """

    # load files
    df_x = pd.read_csv(fname_x, sep=',', header=None)
    df_y = pd.read_csv(fname_y, sep=',', header=None)

    # more than one test signal per file so iterate:
    for n in range(df_x.shape[1]):
        x = df_x[n].values
        y_matlab = df_y[n].values
        y_py = ed.gen_edo(x)

        print('max. difference = {:g}'.format(max(abs(y_matlab - y_py))))

        if DBplot:
            fig, ax = plt.subplots(nrows=3, ncols=1, num=2, clear=True)
            ax[0].plot(x, '-o')
            ax[1].plot(y_matlab, '-x')
            ax[1].plot(y_py, '-o')
            ax[2].plot(y_matlab - y_py, '-x')
            plt.pause(1.2)


def test_compare_all_files():
    """
    compare Matlab and Python EDOs from test files
    """

    DBplot = True
    print('** compare with N=256 test signals')
    fname_x = 'data/test_signals_N256_.csv'
    fname_y = 'data/edo_test_signals_N256_.csv'
    load_file_and_compare(fname_x, fname_y, DBplot)

    print('\n** compare with N=101 test signals')
    fname_x = 'data/test_signals_N101_.csv'
    fname_y = 'data/edo_test_signals_N101_.csv'
    load_file_and_compare(fname_x, fname_y, DBplot)


if __name__ == '__main__':
    test_compare_all_files()

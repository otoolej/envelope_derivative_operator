"""
functions to run through all 5 test signals and plot

John M. O' Toole, University College Cork
Started: 05-09-2019
last update: <2019-09-04 13:36:01 (otoolej)>
"""
import numpy as np
from matplotlib import pyplot as plt
from energy_operators import edo as ed
from test_functions import gen_test_signals as gs


def compare_edo_test_signals(sig_num=0, DBplot=True):
    """generate EDO for 5 different test signals


    Parameters
    ----------
    sig_num: string, {'0', '1', '2', '3', '4'}
        which test signal to use
    DBplot: bool
        plot or not
    """
    # generate the signal:
    xd = gs.gen_signals(sig_num, False)
    # generate the EDO:
    x_e = ed.gen_edo(xd['x'])

    if DBplot:
        N = len(x_e)
        fig, ax = plt.subplots(nrows=2, ncols=1, num=3, clear=True)
        ax[0].plot(xd['x'], '-o', label='test signal')
        ax[1].plot(xd['fwe'], '-x', label='frequency-weighted energy')
        npart = np.arange(3, N - 4)
        ax[1].plot(npart, x_e[npart], '-x', label='EDO')
        ax[0].legend(loc='upper left')
        ax[1].legend(loc='upper left')


def do_all_tone_tests():
    """ Run through all tests """
    DBplot = True
    all_test = ['0', '1', '2', '3', '4']
    for n in all_test:
        print("test", n)
        compare_edo_test_signals(n, DBplot)
        plt.pause(1.2)


if __name__ == '__main__':
    do_all_tone_tests()

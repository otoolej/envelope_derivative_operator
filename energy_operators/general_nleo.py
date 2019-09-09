"""
 general_nleo: ''General'' NLEO expression: Ψ(n)=x(n-l)x(n-p)-x(n-q)x(n-s)
                for l+p=q+s  (and [l,p]≠[q,s], otherwise Ψ(n)=0)


 John M. O' Toole, University College Cork
 Started: 28-01-2014

 last update: Time-stamp: <2019-09-06 10:49:37 (otoolej)>
"""
import numpy as np
from matplotlib import pyplot as plt


def gen_nleo(x, l=1, p=2, q=0, s=3):
    """general form of the nonlinear energy operator (NLEO)

    General NLEO expression: Ψ(n) = x(n-l)x(n-p) - x(n-q)x(n-s)
    for l+p=q+s  (and [l,p]≠[q,s], otherwise Ψ(n)=0)

    Parameters
    ----------
    x: ndarray
        input signal
    l: int, optional
        parameter of NLEO expression (see above)
    p: int, optional
        parameter of NLEO expression (see above)
    q: int, optional
        parameter of NLEO expression (see above)
    s: int, optional
        parameter of NLEO expression (see above)

    Returns
    -------
    x_nleo : ndarray
        NLEO array

    Example
    -------
    import numpy as np

    # generate test signal
    N = 256
    n = np.arange(N)
    w1 = np.pi / (N / 32)
    ph1 = -np.pi + 2 * np.pi * np.random.rand(1)
    a1 = 1.3
    x1 = a1 * np.cos(w1 * n + ph1)

    # compute instantaneous energy:
    x_nleo = gen_nleo(x1, 1, 2, 0, 3)

    # plot:
    plt.figure(1, clear=True)
    plt.plot(x1, '-o', label='test signal')
    plt.plot(x_nleo, '-o', label='Agarwal-Gotman')
    plt.legend(loc='upper left')
    """
    # check parameters:
    if ((l + p) != (q + s) and any(np.sort((l, p)) != np.sort((q, s)))):
        warning('Incorrect parameters for NLEO. May be zero!')

    N = len(x)
    x_nleo = np.zeros(N)

    iedges = abs(l) + abs(p) + abs(q) + abs(s)
    n = np.arange(iedges + 1, (N - iedges - 1))

    x_nleo[n] = x[n-l] * x[n-p] - x[n-q] * x[n-s]

    return(x_nleo)


def specific_nleo(x, type='teager'):
    """ generate different NLEOs based on the same operator 

    Parameters
    ----------
    x: ndarray
        input signal
    type: {'teager', 'agarwal', 'palmu', 'abs_teager', 'env_only'}
        which type of NLEO? 

    Returns
    -------
    x_nleo : ndarray
        NLEO array
    """

    def teager():
        return(gen_nleo(x, 0, 0, 1, -1))

    def agarwal():
        return(gen_nleo(x, 1, 2, 0, 3))

    def palmu():
        return(abs(gen_nleo(x, 1, 2, 0, 3)))

    def abs_teager():
        return(abs(gen_nleo(x, 0, 0, 1, -1)))

    def env_only():
        return(abs(x) ** 2)

    def default_nleo():
        # -------------------------------------------------------------------
        # default option
        # -------------------------------------------------------------------
        print('Invalid NLEO name; defaulting to Teager')
        return(teager())

    # pick which function to execute
    which_nleo = {'teager': teager, 'agarwal': agarwal,
                  'palmu': palmu, 'abs_teager': abs_teager,
                  'env_only': env_only}

    def get_nleo(name):
        return which_nleo.get(name, default_nleo)()

    x_nleo = get_nleo(type)
    return(x_nleo)


def test_compare_nleos(x=None, DBplot=True):
    """ test all NLEO variants with 1 signal

    Parameters
    ----------
    x: ndarray, optional
        input signal (defaults to coloured Gaussian noise)
    DBplot: bool
        plot or not
    """
    if x is None:
        N = 128
        x = np.cumsum(np.random.randn(N))

    all_methods = ['teager', 'agarwal', 'palmu']
    all_methods_strs = {'teager': 'Teager-Kaiser', 'agarwal': 'Agarwal-Gotman',
                        'palmu': 'Palmu et.al.'}
    x_nleo = dict.fromkeys(all_methods)

    for n in all_methods:
        x_nleo[n] = specific_nleo(x, n)

    if DBplot:
        fig, ax = plt.subplots(nrows=2, ncols=1, num=4, clear=True)
        ax[0].plot(x, '-o', label='test signal')
        for n in all_methods:
            ax[1].plot(x_nleo[n], '-o', label=all_methods_strs[n])
        ax[0].legend(loc='upper right')
        ax[1].legend(loc='upper left')
        plt.pause(0.0001)

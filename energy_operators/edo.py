"""compute the envelope derivative operator (EDO), as defined in [1].

[1] JM O' Toole, A Temko, NJ Stevenson, “Assessing instantaneous energy in the EEG: a
non-negative, frequency-weighted energy operator”, IEEE Int. Conf.  on Eng. in Medicine
and Biology, Chicago, August 2014


John M. O' Toole, University College Cork
Started: 05-09-2019
last update: <2019-09-04 13:36:01 (otoolej)>
"""
import numpy as np
from matplotlib import pyplot as plt


def discrete_hilbert(x, DBplot=False):
    """Discrete Hilbert transform

    Parameters
    ----------
    x: array_type
        input signal
    DBplot: bool, optional
        plot or not 

    Returns
    -------
    x_hilb : array_type
        Hilbert transform of x

    """
    N = len(x)
    Nh = np.ceil(N / 2)
    k = np.arange(N)

    # build the Hilbert transform in the frequency domain:
    H = -1j * np.sign(Nh - k) * np.sign(k)
    x_hilb = np.fft.ifft(np.fft.fft(x) * H)
    x_hilb = np.real(x_hilb)

    if DBplot:
        plt.figure(10, clear=True)
        plt.plot(np.imag(H))

    return(x_hilb)


def gen_edo(x, DBplot=False):
    """Generate EDO Γ[x(n)] from simple formula in the time domain:

    Γ[x(n)] = y(n)² + H[y(n)]²

    where y(n) is the derivative of x(n) using the central-finite method and H[.] is the
    Hilbert transform.

    Parameters
    ----------
    x: array_type
        input signal
    DBplot: bool, optional
        plot or not

    Returns
    -------
    x_edo : array_type
        EDO of x

    """
    # 1. check if odd length and if so make even:
    N_start = len(x)
    if (N_start % 2) != 0:
        x = np.hstack((x, 0))

    N = len(x)
    nl = np.arange(1, N - 1)
    xx = np.zeros(N)

    # 2. calculate the Hilbert transform
    h = discrete_hilbert(x)

    # 3. implement with the central finite difference equation
    xx[nl] = ((x[nl+1] ** 2) + (x[nl-1] ** 2) +
              (h[nl+1] ** 2) + (h[nl-1] ** 2)) / 4 - ((x[nl+1] * x[nl-1] +
                                                       h[nl+1] * h[nl-1]) / 2)

    # trim and zero-pad and the ends:
    x_edo = np.pad(xx[2:(len(xx) - 2)], (2, 2),
                   'constant', constant_values=(0, 0))

    return(x_edo[0:N_start])


def test_edo_random():
    """test EDO with a random signal"""
    # if (__name__ == '__main__'):

    DBplot = True
    x = np.random.randn(102)
    x_e = gen_edo(x)

    # -------------------------------------------------------------------
    # plot
    # -------------------------------------------------------------------
    if DBplot:
        plt.figure(2, clear=True)
        hl1, = plt.plot(x, label='test signal')
        hl2, = plt.plot(x_e, label='EDO')
        plt.legend(handles=[hl1, hl2], loc='upper right')
        plt.pause(0.0001)
        # plt.show(block=False)

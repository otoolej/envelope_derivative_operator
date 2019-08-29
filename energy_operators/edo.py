import numpy as np
from matplotlib import pyplot as plt
import matplotlib
# Problem with GTK3Agg (the default) so use this (must have PyQT5 installed):
matplotlib.use('Qt5Agg')
# matplotlib.use('GTK3Cairo')

# testing only, shouldn't need this in the future:


def discrete_hilbert(x, DBplot=False):
    """
    Discrete Hilbert transform
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
    # if (__name__ == '__main__'):
    DBplot = True

    x = np.random.randn(102)
    x_e = gen_edo(x)

    # -------------------------------------------------------------------
    # plot
    # -------------------------------------------------------------------
    if DBplot:
        plt.figure(1, clear=True)
        plt.plot(x)
        plt.plot(x_e)
        plt.title('EDO')

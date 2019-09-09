"""
generate 5 different test signals of the form: a₁cos(ω₁t + φ₁)

John M. O' Toole, University College Cork
Started: 04-09-2019
last update: <2019-09-04 13:36:01 (otoolej)>
"""
import numpy as np
from matplotlib import pyplot as plt
import matplotlib


def gen_signals(sig_num=0, DBplot=True):
    """define some simple test signals of the form: a₁cos(ω₁t + φ₁)

    Parameters
    ----------
    sig_num: string, {'0', '1', '2', '3', '4'}
        which signal type
    DBplot: bool
        plot or not


    Returns
    -------
    x_dt : dict, keys: 'x' and 'fwe'
        returns test signal 'x' and the expected frequency-weighted energy 'fwe'
    """

    N = 256
    Nh = np.ceil(N / 2)
    n = np.arange(N)
    w1 = np.pi / (N / 32)
    w2 = np.pi / (N / 8)
    ph1 = -np.pi + 2 * np.pi * np.random.rand(1)
    ph2 = -np.pi + 2 * np.pi * np.random.rand(1)
    a1 = 1.3
    a2 = 3.1
    x1 = a1 * np.cos(w1 * n + ph1)
    x2 = a2 * np.cos(w2 * n + ph2)

    def sig0():
        # ---------------------------------------------------------------------
        # stationary signal: a₁cos(ω₁t + φ₁)
        # ---------------------------------------------------------------------
        x = x2  # / max(x2)
        extact_x = np.full(N, (a2 ** 2) * (w2 ** 2))
        return({'x': x, 'fwe': extact_x})

    def sig1():
        # ---------------------------------------------------------------------
        # concatentated (in time) signals: a₁cos(ω₁t + φ₁) PLUS a₂cos(ω₂t + φ₂)
        # ---------------------------------------------------------------------
        a1 = 1
        a2 = 1
        w1 = np.pi / (N / 32)
        w2 = np.pi / (N / 16)

        x = np.hstack((a1 * np.cos(w1 * np.arange(Nh + 1)),
                       a2 * np.cos(w2 * np.arange(Nh + 1, N))))
        extact_x = np.hstack((np.full((int(Nh)), a1 ** 2) * np.sin(w1) ** 2,
                              np.full((int(Nh)), a2 ** 2) * np.sin(w2) ** 2))
        return({'x': x, 'fwe': extact_x})

    def sig2():
        # ---------------------------------------------------------------------
        # signal with amplitude modulation: e^{rt} a₁cos(ω₁t + φ₁)
        # ---------------------------------------------------------------------
        r1 = 0.005
        x = np.exp(-r1 * n) * x1

        extact_x = (a1 ** 2) * np.exp(-2*r1*n) * (np.sin(w1) ** 2+r1 ** 2)
        return({'x': x, 'fwe': extact_x})

    def sig3():
        # ---------------------------------------------------------------------
        # signal with frequency modulation: a₁cos(φ(t))
        # ---------------------------------------------------------------------
        if_law = 0.1 + 0.3 * np.sin(n * np.pi / N)
        ph = np.cumsum(if_law)
        x = a1 * np.cos(ph + ph1)
        extact_x = (a1 ** 2) * (if_law) ** 2
        # extact_x = (a1 ** 2) * (np.sin(if_law)) ** 2
        return({'x': x, 'fwe': extact_x})

    def sig4():
        # ---------------------------------------------------------------------
        # sum of two signals: a₁cos(ω₁t + φ₁) + a₂cos(ω₂t + φ₂)
        # ---------------------------------------------------------------------
        x = x1 + x2
        edo_x1 = (a1 ** 2) * (w1 ** 2)
        edo_x2 = (a2 ** 2) * (w2 ** 2)
        a_12 = 2 * a1 * a2 * w1 * w2
        extact_x = edo_x1 + edo_x2 + a_12 * np.cos(n * (w1 - w2) + ph1 - ph2)
        return({'x': x, 'fwe': extact_x})

    def default_sig():
        # -------------------------------------------------------------------
        # default option
        # -------------------------------------------------------------------
        print('Invalid signal name; defaulting to sig0')
        return(sig0())

    # pick which function to execute
    which_sig = {'0': sig0, '1': sig1, '2': sig2, '3': sig3, '4': sig4}

    def get_sig(name):
        return which_sig.get(name, default_sig)()

    x_dt = get_sig(sig_num)

    if DBplot:
        plt.figure(10, clear=True)
        plt.plot(x_dt['x'], '-x')
        plt.plot(x_dt['fwe'], '-o')

    return(x_dt)


# testing :
# xd = gen_signals('0', True)

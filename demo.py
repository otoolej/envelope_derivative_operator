"""

Functions to test the envelope derivative operator (EDO), see [1]
for more details.

[1] JM O' Toole, A Temko, NJ Stevenson, “Assessing instantaneous energy in the 
EEG: a non-negative, frequency-weighted energy operator”, IEEE Int. Conf.
on Eng. in Medicine and Biology, Chicago, August 2014


John M. O' Toole, University College Cork
Started: 05-09-2019
last update: <2019-09-04 13:36:01 (otoolej)>
"""

# Version of the energy_operators package
__version__ = "0.0.1"

import numpy as np
from matplotlib import pyplot as plt


from energy_operators import general_nleo
from energy_operators import edo
from test_functions import gen_test_signals
from test_functions import test_edo

start_message = """
Envelope Derivative Operator (EDO): a frequency-weighted energy operator
========================================================================

JM O' Toole, A Temko, NJ Stevenson, “Assessing instantaneous energy in the 
EEG: a non-negative, frequency-weighted energy operator”, IEEE Int. Conf.
on Eng. in Medicine and Biology, Chicago, August 2014
"""
print('\n' + start_message)

# -------------------------------------------------------------------
# Test #1: EDO with sum of 2 sinusoids
# -------------------------------------------------------------------
print('\n\n ------------------------------------------')
print(' 1. test EDO and compare with Teager-Kaiser operator')

# 1. generate 2 sinusoidal signals
N = 256
n = np.arange(N)
w = (np.pi / (N / 32), np.pi / (N / 8))
ph = (-np.pi + 2 * np.pi * np.random.rand(1),
      -np.pi + 2 * np.pi * np.random.rand(1))
a = (1.3, 3.1)
x = a[0] * np.cos(w[0] * n + ph[0]) + a[1] * np.cos(w[1] * n + ph[1])

# 2. estimate the EDO
x_edo = edo.gen_edo(x, True)

# 3. generate Teager--Kaiser operator for comparison:
x_nleo = general_nleo.specific_nleo(x, type='teager')

# 4. plot
fig, ax = plt.subplots(nrows=2, ncols=1, num=1, clear=True)
ax[0].plot(x, '-', label='test signal')
ax[1].plot(x_edo, '-', label='EDO')
ax[1].plot(x_nleo, label='Teager-Kaiser')
ax[0].legend(loc='upper right')
ax[1].legend(loc='upper left')
plt.pause(0.0001)

input("\n Any key to continue...")


# -------------------------------------------------------------------
# Test #2: EDO with Gaussian white noise
# -------------------------------------------------------------------
print('\n\n ------------------------------------------')
print(' 2. test EDO with Gaussian random noise')
# 1. test with random signal:
edo.test_edo_random()

input("\n Any key to continue...")

# -------------------------------------------------------------------
# Test #3: EDO with 4 different signal types
# -------------------------------------------------------------------
print('\n\n ------------------------------------------')
print(' 3. test EDO with different types and plot against expected ')
print('    frequency-weighted energy')
# 2. test with lots of different signals:
test_edo.do_all_tone_tests()

input("\n Any key to continue...")

# -------------------------------------------------------------------
# Test #4: compare different versions of the NLEO operator of the form:
# Ψ(n) = x(n-l)x(n-p) - x(n-q)x(n-s)
# -------------------------------------------------------------------
print('\n\n ------------------------------------------')
print(' 4. compare different NLEO of the form: x(n-l)x(n-p) - x(n-q)x(n-s)')

# 1. get test signal:
x1 = gen_test_signals.gen_signals('4', False)

# 2. compare methods based on the general NLEO expression:
general_nleo.test_compare_nleos(x1['x'], True)


input("\n Any key to finish.")


# -------------------------------------------------------------------
# compare with Matlab
# -------------------------------------------------------------------
# from test_functions import compare_matlab as cmp

# # load .csv files and compare with Matlab:
# cmp.test_compare_all_files()

# -------------------------------------------------------------------
# compare with Matlab
# -------------------------------------------------------------------
# from test_functions import compare_matlab as cmp

# # load .csv files and compare with Matlab:
# cmp.test_compare_all_files()


# need to re-load packages and modules if changed
# not working!
# %load_ext autoreload
# %autoreload 2


# -------------------------------------------------------------------
# test envelope-derivative operator
# -------------------------------------------------------------------
from energy_operators import general_nleo, edo
from test_functions import gen_test_signals, test_edo

# 1. test with random signal:
edo.test_edo_random()

# 2. test with lots of different signals:
test_edo.do_all_tone_tests()

# -------------------------------------------------------------------
# compare different versions of the NLEO operator of the form:
# Ψ(n) = x(n-l)x(n-p) - x(n-q)x(n-s)
# -------------------------------------------------------------------
# 1. get test signal:
x1 = gen_test_signals.gen_signals('4', True)

# 2. compare methods based on the general NLEO expression:
nleo.test_compare_nleos(x1['x'], True)

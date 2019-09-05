# Estimating Instantaneous Energy 

Python code to implement instantaneous energy measures, including the "envelope derivative
operator", as described in [[1]](#references).  Requires the Python 3 with NumPy, Matplotlib,
and Pandas packages.

This is Python implementation of the Matlab code, also on [github](https://github.com/otoolej/nonlinear-energy-operators).



# overview
Implements methods to estimate frequency-weighted instantaneous energy including the
Teager–Kaiser operator (also referred to as the nonlinear energy operator) and a similar
frequency-weight operator proposed in reference [[1]](#references). The Teager–Kaiser operator is
simply defined, for discrete signal x(n), as
```
Ψ[x(n)] = x²(n) - x(n+1)x(n-1)
```  
and the proposed energy measure—which we call the envelope derivative operator (EDO)—is defined as
```
 Γ[x(n)] = y²(n) + H[y(n)]²
```
where y(n) is the derivative of x(n), estimated using the central-finite difference
equation y(n)=[x(n+1)-x(n-1)]/2, and H[·] is the discrete Hilbert transform of x(n). 
Reference [[1]](#references) contains more details.


# quick start
Use the `demo.py` to run a few examples from the command line:
```bash
$ python3 demo.py
```

# examples

Test EDO with a random signal:
```python
	from energy_operators import edo

	edo.test_edo_random()
```	

Generates the EDO and the Teager–Kaiser operator for a test signal, the sum of two sinusoidal signals:
```python
	import numpy as np
	from matplotlib import pyplot as plt

	from energy_operators import general_nleo
	from energy_operators import edo
	from test_functions import gen_test_signals
	from test_functions import test_edo


	# 1. generate test signal composed of 2 sinusoidal signals
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
```


## properties
To test the properties of the operators with some example signals, call
`test_edo.compare_edo_test_signals(number)` with argument `number` either '0', '1', '2',
'3', or '4'. 
For example, 
```python
   from test_functions import test_edo

   test_edo.compare_edo_test_signals('3')
```
calls the function with frequency modulated signal with instantaneous frequency law of
0.1+0.3sin(tπ/N).


# files
Directory structure as follows: 
```
.
├── data                        # csv files for testing with Matlab implementation
├── docs                        # papers and docs. related to the package
├── energy_operators            # PACKAGE: modules to generate the energy operators
│   ├── edo.py             
│   └── general_nleo.py
├── LICENSE.md
├── demo.py                     # script containing examples on how to use this package
├── README.md
├── requirements.txt
└── test_functions              # PACKAGE: modules to generate test signals
    ├── compare_matlab.py
    ├── gen_test_signals.py
    └── test_edo.py
```


# requirements
Developed and tested with Python 3.7. Requires:
- NumPy version 1.17.0
- matplotlib version 3.1.1
- pandas version 0.25.0

---

# licence

```
Copyright (c) 2019, John O' Toole, University College Cork
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

  Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

  Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

  Neither the name of the University College Cork nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```


# references

1. JM O' Toole and NJ Stevenson, “Assessing instantaneous energy in the EEG: a
non-negative, frequency-weighted energy operator”, IEEE Int. Conf. on Eng. in Medicine and
Biology, EMBC’14, Chicago, USA, August 2014. [ [paper](docs/JMOToole_energy_EMBC14.pdf) |
[poster](docs/EMBC_poster_Aug2014_NLEO.pdf) ]


---

# contact

John M. O' Toole

Neonatal Brain Research Group,  
INFANT Research Centre ([INFANT](http://www.infantcentre.ie)),  
Department of Paediatrics and Child Health,  
University College Cork,  
Cork, Ireland

email: jotoole -- AT -- ucc .-. DOT ._. ie

Estimating Instantaneous Energy 
================================

Collection of M-files (computer code) to implement instantaneous energy measures, including the "nonlinear energy operator", as
described in [[1]](#references).
Requires Matlab or Octave programming environments.


# contents
* [overview](#overview)
* [quick start](#quick-start)
* [requirements](#requirements)
* [test computer setup](#test-computer-setup)
* [licence](#licence)
* [references](#references)
* [contact](#contact)


# overview
Implements methods to estimate frequency-weighted instantaneous energy.  Implements the
Teager–Kaiser operator, often referred to as the nonlinear energy operator, and a similar
frequency-weight operator proposed in reference [[1]](#references). The Teager–Kaiser operator is
simply defined, for discrete signal x(n), as
```
Ψ[x(n)] = x²(n) - x(n+1)x(n-1)
```  
and the proposed energy measure is defined as
```
 Γ[x(n)] = y²(n) + H[y(n)]²
```
where y(n) is the derivative of x(n), estimated using the central-finite difference
equation y(n)=[x(n+1)-x(n-1)]/2, and H[·] is the discrete Hilbert transform of x(n).  Reference [[1]](#references) contains more details.


# quick start

The following example generates the Teager–Kaiser operator and the proposed
envelope–derivative operator for a test signal (sum of two sinusoidals signals),
cut-and-paste the following code into Matlab (or Octave):
```matlab
  % generate two sinusoidal signals:
  N=256; n=0:N-1;
  w1=pi/(N/32); ph1=-pi+2*pi*rand(1,1);  a1=1.3;
  w2=pi/(N/8); ph2=-pi+2*pi*rand(1,1);  a2=3.1;
  x1=a1.*cos(w1.*n + ph1);  x2=a2.*cos(w2.*n + ph2);
  x=x1+x2;

  % compute instantaneous energy:
  x_env_diff=cal_freqweighted_energy(x,1,'envelope_diff');
  x_teager  =cal_freqweighted_energy(x,1,'teager');

  % plot:
  figure(1); clf; 
  subplot(211); hold all; plot(x); ylabel('amplitude');
  subplot(212); hold all; plot(x_env_diff,'-'); plot(x_teager,'--');
  ylabel('energy');
  legend('envelope-derivative','Teager-Kaiser');
```


## properties
To test the properties of the operators with some example signals, call
`properties_test_Hilbert_NLEO(number)` with argument `number` either 0,1,2,3, or 4. For
example, 
```matlab
  >> properties_test_Hilbert_NLEO(3);
```
calls the function with frequency modulated signal with instantaneous frequency law of
0.1+0.3sin(tπ/N).

## noise analysis
To compare the bias for each method, run the function
```matlab
  >> bias_of_estimators;
```
which computes the mean-value (and therefore an approximation to the Expectation operator)
of 10,000 iterations of white Gaussian noise. This then produces Fig. 2 in the ‘Noise
Analysis’ section of [[1]](#references).


# files
All Matlab files (.m files) have a description and an example in the header. To read this
header, type `help <filename.m>` in Matlab.  Directory structure is as follows: 
```
.
├── bias_of_estimators.m              # noise analysis: estimate bias with WGN
├── cal_freqweighted_energy.m         # select method to estimate instantaneous energy
├── discrete_Hilbert_diff_operator.m  # proposed envelope–derivative operator
├── do_bandpass_filtering.m           # simply band-pass filtering
├── general_nleo.m                    # general Nonlinear Energy Operator (Plotkin–Swamy)
├── nleo_parameters.m                 # set parameters here (directions etc.)
├── pics/                             # directory for figures
├── properties_test_Hilbert_NLEO.m    # test properties of the different operator
└── requires_EEG_data		          # directory containing files for EEG analysis
    ├── compare_nleo_methods.m		  # these files require EEG data to run.
    ├── plot_eeg_examples.m	
    └── script_test_eeg_data.m
```


# requirements
Either Matlab (R2012 or newer,
[Mathworks website](http://www.mathworks.co.uk/products/matlab/)) or Octave (v3.6 or
newer, [Octave website](http://www.gnu.org/software/octave/index.html), with the
'octave-signal' add-on package).



# test computer setup
- hardware:  Intel(R) Xeon(R) CPU E5-1603 0 @ 2.80GHz; 8GB memory.
- operating system: Ubuntu GNU/Linux x86_64 distribution (Trusty Tahr, 14.04), with Linux kernel 3.13.0-27-generic
- software: Octave 3.8.1 (using Gnuplot 4.6 patchlevel 4), with 'octave-signal' toolbox and Matlab (R2009b, R2012a, and R2013a)

---

# licence

```
Copyright (c) 2014, John O' Toole, University College Cork
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
Biology, EMBC’14, Chicago, USA, August 2014. [ [paper](publications/JMOToole_energy_EMBC14.pdf) | [poster](publications/EMBC_poster_Aug2014_NLEO.pdf) ]


---

# contact

John M. O' Toole

Neonatal Brain Research Group,  
Irish Centre for Fetal and Neonatal Translational Research ([INFANT](http://www.infantcentre.ie)),  
Department of Paediatrics and Child Health,  
University College Cork,  
Cork, Ireland



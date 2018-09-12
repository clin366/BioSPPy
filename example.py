'''
    File name: example.py
    Author: Chen Lin
    Email: chen.lin@emory.edu
    Date created: 9/11/2018
    Date last modified: 9/11/2018
    Python Version: 3.6
    Source code copied from: https://github.com/PIA-Group/BioSPPy/blob/master/README.md
'''

# from biosppy import storage
from biosppy import storage
# from biosppy.signals import ecg
from biosppy.signals import *

# load raw ECG signal
signal, mdata = storage.load_txt('./examples/ecg.txt')

# process it and plot
out = ecg.ecg(signal = signal, sampling_rate = 1000., show = True)

# load raw BVP signal
bvp_signal, bvp_mdata = storage.load_txt('examples/bvp.txt')

# process it and plot
bvp_out = bvp.bvp(signal = bvp_signal, sampling_rate = 1000., show = True)


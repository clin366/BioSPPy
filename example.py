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


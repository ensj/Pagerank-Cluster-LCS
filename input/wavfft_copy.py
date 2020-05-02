import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
rate, data = wavfile.read('muse.wav') # load the data
a = data.T[0] # this is a two channel soundtrack, I get the first track
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
print('sample rate:', rate)
print('time:', len(b)/rate)
c = fft(b) # calculate fourier transform (complex numbers list)
d = math.floor(len(c)/2)  # you only need half of the fft list (real signal symmetry)
#plt.plot(abs(c[:d-1]),'r') 
plt.plot(a)
plt.show()
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get api
rate, data = wavfile.read('muse.wav') # the
a = data.T[0] # this a two channel, I get the track
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
print('sample rate:', rate)
print('time:', len(b)/rate)
c = fft(b) # calculate transform (complex numbers list)
d = math.floor(len(c)/2)  # you only need of the fft list (real signal symmetry)
#plt.plot(abs(c[:d-1]),'r') 
plt.plot(a)
plt.show()
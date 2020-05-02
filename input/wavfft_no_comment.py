import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile 
rate, data = wavfile.read('muse.wav')
a = data.T[0] 
b=[(ele/2**8.)*2-1 for ele in a] 
print('sample rate:', rate)
print('time:', len(b)/rate)
c = fft(b) 
d = math.floor(len(c)/2)  
plt.plot(a)
plt.show()
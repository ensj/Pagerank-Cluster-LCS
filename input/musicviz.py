from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

"""CHUNK = 1024

RATE, data = wavfile.read('muse.wav')

for i in range(1, int(len(data)/(CHUNK))):
	time.sleep(0.1)
	peak = np.average(np.abs(data[(i-1)*CHUNK:i*CHUNK]))*2
	bars = '#'*int((50*peak)/(2**16))
	print("%04d %05d %s"%(i, peak, bars)) # newline flushes immediately."""

fig = plt.figure()
ax = plt.axes(xlim=(0,4), ylim=(-2,2))
line, = ax.plot([], [], lw=3)

def init():
	line.set_data([],[])
	return line,

def animate(i):
	x = np.linspace(0,4,1000)
	y = np.sin(2 * np.pi * (x - 0.01 * i))
	line.set_data(x, y)
	return line,

anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True)

plt.show()
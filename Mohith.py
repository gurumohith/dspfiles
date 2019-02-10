import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('moh1.wav')
print(fs,len(data),data)
plt.subplot(411)
plt.plot(data)
t=np.arange(0,len(data)/fs,1.0/fs)
plt.subplot(412)
plt.plot(t,data)
print(data)
plt.plot(data)
wav.write('voice1.wav',2*fs,data)
plt.subplot(413)
plt.plot(data)
wav.write('voice2.wav',0.5*fs,data)
plt.subplot(414)
plt.plot(data)
plt.show()

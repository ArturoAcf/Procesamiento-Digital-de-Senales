# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 2 - Series y Transformada de Fourier
# Tarea 2 - Generación de Señal Cuadrada y Transformada de Fourier

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss

# --------------------------------------------------------------- #

T=16
N=64*T
t=np.arange(0, N)
f=1/T
signal=ss.square(2*np.pi*f*t) # Señal cuadrada

# --------------------------------------------------------------- #

# Fourier

X=np.fft.fft(signal)
freqs=np.fft.fftfreq(X.size) # Frecuencias

# --------------------------------------------------------------- #

# Mostrar señal

plt.title('Fourier')
plt.plot(freqs, np.abs(X), color='blue', label='Fourier') # Debe ser abs (módulo)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.grid()
plt.legend()

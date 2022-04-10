# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 2 - Series y Transformada de Fourier
# Tarea 3 - DFT

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss

# --------------------------------------------------------------- #

# DFT

T=16
N=64*T # 64 periodos
t=np.arange(0, N)
w=np.exp(-1j*2*np.pi/N) # -1j -> número complejo
dft=np.zeros(N, dtype=complex) # Debe ser de tipo complejo
f=1/T
signal=ss.square(2*np.pi*f*t) # Señal de entrada

def dft_alt(s):
    for k in range(1, N):
        x=0
        for n in range(1, N):
            nk=(n-1)*(k-1)
            x+=s[n]*w**nk # Ecuacion de DFT
        dft[k]=x
    return dft

sres=dft_alt(signal)
freqs=np.fft.fftfreq(len(sres))

# --------------------------------------------------------------- #

# Mostrar señal

plt.title('DFT')
plt.plot(freqs, abs(sres), color='lightblue', label='DFT')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.grid()
plt.legend()

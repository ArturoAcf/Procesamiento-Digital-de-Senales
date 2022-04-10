# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 2 - Series y Transformada de Fourier
# Tarea 1 - Generación de Señal Cuadrada

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------- #

To=2*np.pi
Fo=1/To
wo=2*np.pi*Fo

Fs=100 # Frecuencia de muestreo / Ts=0.01
time=18.85 # Tiempo de duración de la señal
A=F=1 # Amplitud y frecuencia
t=np.arange(0, time, 1/Fs)
com=0

for i in range(1, 11, 2):
    com+=np.sin(i*t)/i

signal=4*com/np.pi

# --------------------------------------------------------------- #

# Mostrar señal

plt.title('Señal Cuadrada')
plt.plot(t, signal, color='purple', label='Señal cuadrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (Hz)')
plt.grid()
plt.legend()

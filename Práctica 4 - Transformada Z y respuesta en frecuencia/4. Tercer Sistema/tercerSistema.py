# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 4 - Transformada Z y respuesta en frecuecncia
# Tarea 4 - Tercer sistema

import numpy as np
import pds
import matplotlib.pyplot as plt
import scipy.signal as signal

# --------------------------------------------------------------- #

# a y b

a=np.array([1, -0.9, +0.81])
b=np.array([1, 1, 0])
n=np.linspace(-20, 100, 121)

# --------------------------------------------------------------- #

# Magnitud y fase

plt.figure()
pds.plot_freq_resp(b, a)
plt.axvline(x=np.pi, color='lightblue', label='PI')
plt.axvline(x=np.pi/3, color='lightblue', label='PI/3')

# --------------------------------------------------------------- #

# Señal

n=np.linspace(0, 199, 200)
signalOut=np.sin(np.pi*n/3)+5*np.cos(np.pi*n)
y=signal.lfilter(b, a, signalOut)

# Mostrar señal

plt.figure()
plt.plot(y, label="y(n)")
plt.legend()
plt.grid()

# --------------------------------------------------------------- #

# ¿Cómo se modifican amplitudes y fases de las dos sinusoides?

# Wuolah

# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 5 - Disño de Filtros Digitales FIR
# Tarea 2 - Ventanas

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pds

# --------------------------------------------------------------- #

n1=15
n2=31
n3=63
cutoff=0.5

b1=signal.firwin(n1, cutoff)
b2=signal.firwin(n2, cutoff)
b3=signal.firwin(n3, cutoff)

# --------------------------------------------------------------- #

# Respuesta en frecuancia

# 15
plt.figure()
pds.plot_freq_resp(b1, a=1)

# 31
plt.figure()
pds.plot_freq_resp(b2, a=1)

# 63
plt.figure()
pds.plot_freq_resp(b3, a=1)

# --------------------------------------------------------------- #

# Comparar para 31 con ventanas de Hamming y Barlett

hamming=np.hamming(n2)
b_ham=b2*hamming
plt.figure()
pds.plot_freq_resp(b_ham, a=1)

bartlett=signal.firwin(n2, cutoff, window="bartlett")
plt.figure()
pds.plot_freq_resp(bartlett, a=1)

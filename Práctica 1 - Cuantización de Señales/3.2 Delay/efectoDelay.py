# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 1 - Cuantización de Señales
# Tarea 3.2 - Efecto Delay

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf

# --------------------------------------------------------------- #

# Cargar archivo .wav

Fs, signal=wavfile.read('./muneca.wav') # Ruta del archivo con la señal
signal=signal.astype(float)
t=np.arange(0, len(signal)/Fs, 1/Fs)

# --------------------------------------------------------------- #

# 3.2 - Efecto Delay

# y(t) = 0.9*z(t-1800)   \
#                        -> y(t) = 0.9*(x(t-1800) + 0.8*y(t-1800))
# z(t) = x(t) + 0.8*y(t) /

signalDelay=np.zeros(len(signal)+1800)

for i in range(0, len(signalDelay)):
    if i<1800:
        signalDelay[i]=signal[i]
    elif i<len(signal):
        signalDelay[i]=0.9*(signal[i]+0.8*signalDelay[i-1800])
    else:
        signalDelay[i]=0.9*0.8*signalDelay[i-1800]

signalDelayCorte=signalDelay[1800:]

# Mostrar gráfica
plt.plot(t, signal, label="signal")
plt.plot(t, signalDelayCorte, color='green', label="Delay")

plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (Hz)")
plt.title("Señal original con Delay")

plt.legend()
plt.grid()

# Generar archivo de salida
nombreArchivo='munecaDelay.wav'
wf.write(nombreArchivo, Fs, signalDelay.astype('int16'))

# --------------------------------------------------------------- #

# EXTRA -> Efecto señal invertida

signalInvert=np.flip(signal) # Invierte la señal

# Mostrar gráfica
# plt.plot(t, signalInvert, color='red', label="sigal-Invertida")

# plt.xlabel("Tiempo (s)")
# plt.ylabel("Amplitud (Hz)")
# plt.title("Señal original invertida")

# plt.grid()

nombreArchivo='munecaInverso.wav'
wf.write(nombreArchivo, Fs, signalInvert.astype('int16'))

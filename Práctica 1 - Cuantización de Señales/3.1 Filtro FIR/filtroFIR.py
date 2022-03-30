# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 1 - Cuantización de Señales
# Tarea 3.1 - Filtro FIR

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf

# --------------------------------------------------------------- #

# Cargar archivo .wav

Fs, signal=wavfile.read('./muneca.wav') # Ruta del archivo con la señal a filtrar
signal=signal.astype(float)
t=np.arange(0, len(signal)/Fs, 1/Fs)

# --------------------------------------------------------------- #

# Salida del sistema y filtro FIR

signalOut=np.zeros_like(signal) # Vector de 0's del tamaño de 'signal'

for i in range(2, len(signal)): # Empiza más tarde porque para 0 y 1 no se puede hacer media de las tres anteriores
    signalOut[i-2]=(signal[i]+signal[i-1]+signal[i-2])/3

# Mostrar gráfica
plt.plot(t, signal, label="signal")
plt.plot(t, signalOut, color='red', label="signalOut")

plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (Hz)")
plt.title("Señal filtrada (FIR) y señal original")

plt.grid()
plt.legend()

# Generar archivo de salida
nombreArchivo='munecaFir.wav'
wf.write(nombreArchivo, Fs, signalOut.astype('int16'))

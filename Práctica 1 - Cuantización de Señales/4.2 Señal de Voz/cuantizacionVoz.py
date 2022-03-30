# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 1 - Cuantización de Señales
# Tarea 4.2 - Cuantización Uniforme de señal de voz

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf

# --------------------------------------------------------------- #

# Múltiples plots

fig, graph=plt.subplots(1)
fig2, graph2=plt.subplots(1)
fig3, graph3=plt.subplots(1)

# --------------------------------------------------------------- #

# Cuantizador de 4 bits - delta = 2/16
A=2048
x=16
delta=2/x

# Función para la cuantización
def quantize(s, delta):
    return delta*np.round(s/delta)

# --------------------------------------------------------------- #

# Cargar archivo .wav

Fs, signal=wavfile.read('./muneca.wav') # Ruta del archivo con la señal a filtrar
signal=signal.astype(float)
t=np.arange(0, len(signal)/Fs, 1/Fs)

signal=quantize(signal, delta) # Señal del audio cuantizada

# Generar archivo de salida
nombreArchivo='munecaCuantizada.wav'
wf.write(nombreArchivo, Fs, signal.astype('int16'))

# --------------------------------------------------------------- #

# 8 bits -> cuanto = 16
delta=16

graph.plot(t, signal, color='black', label='Original')

# Cuantización
signalQ=quantize(signal, delta) # Señal del audio cuantizada

# Error
signalE=signalQ-signal

# Mostrar gráficas
graph.plot(t, signalQ, color='lightblue', label='8 bits')
graph.plot(t, signalE, color='orange', label='Error')
graph.set_title('Señal de voz cuantizada - 8 bits')
graph.set_xlabel('Tiempo (s)')
graph.set_ylabel('Amplitud (Hz)')
graph.grid()
graph.legend()

# SNR
Ex=(A**2)/2
SNR=10*np.log10(Ex/(delta**2/12)) # SNR teórico
print('SNR teórico para 8 bits ->', SNR, 'db')

SNRsim=10*np.log10(sum(signal*signal)/sum(signalE*signalE)) # SNR obtenido
print('SNR para 8 bits ->', SNRsim, 'db')

# Generar archivo de salida
nombreArchivo='muneca8bits.wav'
wf.write(nombreArchivo, Fs, signalQ.astype('int16'))

# --------------------------------------------------------------- #

# 6 bits -> cuanto = 64
delta=64

graph2.plot(t, signal, color='black', label='Original')

# Cuantización
signalQ=quantize(signal, delta)

# Error
signalE=signalQ-signal

# Mostrar gráficas
graph2.plot(t, signalQ, color='lightgreen', label='6 bits')
graph2.plot(t, signalE, color='orange', label='Error')
graph2.set_title('Señal de voz cuantizada - 6 bits')
graph2.set_xlabel('Tiempo (s)')
graph2.set_ylabel('Amplitud (Hz)')
graph2.grid()
graph2.legend()

# SNR
Ex=A**2/2
SNR=10*np.log10(Ex/(delta**2/12)) # SNR teórico
print('SNR teórico para 6 bits ->', SNR, 'db')

SNRsim=10*np.log10(sum(signal*signal)/sum(signalE*signalE)) # SNR obtenido
print('SNR para 6 bits ->', SNRsim, 'db')

# Generar archivo de salida
nombreArchivo='muneca6bits.wav'
wf.write(nombreArchivo, Fs, signalQ.astype('int16'))

# --------------------------------------------------------------- #

# 4 bits -> cuanto = 256

delta=256

graph3.plot(t, signal, color='black', label='Original')

# Cuantización
signalQ=quantize(signal, delta)

# Error
signalE=signalQ-signal

# Mostrar gráficas
graph3.plot(t, signalQ, color='grey', label='4 bits')
graph3.plot(t, signalE, color='orange', label='Error')
graph3.set_title('Señal de voz cuantizada - 4 bits')
graph3.set_xlabel('Tiempo (s)')
graph3.set_ylabel('Amplitud (Hz)')
graph3.grid()
graph3.legend()

# SNR
Ex=A**2/2
SNR=10*np.log10(Ex/(delta**2/12)) # SNR teórico
print('SNR teórico para 4 bits ->', SNR, 'db')

SNRsim=10*np.log10(sum(signal*signal)/sum(signalE*signalE)) # SNR obtenido
print('SNR para 4 bits ->', SNRsim, 'db')

# Generar archivo de salida
nombreArchivo='muneca4bits.wav'
wf.write(nombreArchivo, Fs, signalQ.astype('int16'))

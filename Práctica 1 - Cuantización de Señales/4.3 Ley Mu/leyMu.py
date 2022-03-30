# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 1 - Cuantización de Señales
# Tarea 4.3 - Ley Mu

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

# Cargar archivo .wav

Fs, signal=wavfile.read('./muneca.wav') # Ruta del archivo con la señal a filtrar
signal=signal.astype(float)
t=np.arange(0, len(signal)/Fs, 1/Fs)

# --------------------------------------------------------------- #

# Funciones para la cuantización - Ley Mu

A=2048
mu=255

def quantize(s, delta):
    return delta*np.round(s/delta)

def leyMu(x, mu, A):
    y=A*np.sign(x)*np.log(1+mu*np.abs(x)/A)/np.log(1+mu)
    return y

def expansionAnalog(x, mu, A):
    y=np.sign(x)*A*((1+mu)**(np.abs(x)/A)-1)/mu
    return y

# --------------------------------------------------------------- #

# Para 8 bits -> delta = 16
delta=16

# Ley Mu -> F(x)
signalMu=leyMu(signal, mu, A)

# Cuantización
signalQ=quantize(signalMu, delta)

# Expansión analógica -> F^-1(y)
signalInv=expansionAnalog(signalQ, mu, A)

# Error
signalE=signalInv-signal

# Mostrar gráficas
graph.plot(t, signalMu, color='lightblue', label='F(x)')
graph.plot(t, signalInv, color='purple', label='F^-1(y)')
graph.plot(t, signalE, color='orange', label='Error')
graph.set_title('Ley $\mu$ - 8 bits')
graph.set_xlabel('Tiempo (s)')
graph.set_ylabel('Amplitud (Hz)')
graph.grid()
graph.legend()

# SNR
Ex=A**2/2
SNR=10*np.log10(Ex/(delta**2/12)) # SNR teórico
print('SNR teórico para 8 bits ->', SNR, 'db')

SNRsim=10*np.log10(sum(signal*signal)/sum(signalE*signalE)) # SNR obtenido
print('SNR para 8 bits ->', SNRsim, 'db')

# Generar archivos de salida
nombreArchivo='munecaMu8b.wav'
wf.write(nombreArchivo, Fs, signalMu.astype('int16'))

nombreArchivo='munecaMuInv8b.wav'
wf.write(nombreArchivo, Fs, signalInv.astype('int16'))

# --------------------------------------------------------------- #

# Para 6 bits -> delta = 64
delta=64

# Ley Mu -> F(x)
signalMu=leyMu(signal, mu, A)

# Cuantización
signalQ=quantize(signalMu, delta)

# Expansión analógica -> F^-1(y)
signalInv=expansionAnalog(signalQ, mu, A)

# Error
signalE=signalInv-signal

# Mostrar gráficas
graph2.plot(t, signalMu, color='blue', label='F(x)')
graph2.plot(t, signalInv, color='black', label='F^-1(y)')
graph2.plot(t, signalE, color='orange', label='Error')
graph2.set_title('Ley $\mu$ - 6 bits')
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

# Generar archivos de salida
nombreArchivo='munecaMu6b.wav'
wf.write(nombreArchivo, Fs, signalMu.astype('int16'))

nombreArchivo='munecaMuInv6b.wav'
wf.write(nombreArchivo, Fs, signalInv.astype('int16'))

# --------------------------------------------------------------- #

# Para 4 bits -> delta = 256
delta=256

# Ley Mu -> F(x)
signalMu=leyMu(signal, mu, A)

# Cuantización
signalQ=quantize(signalMu, delta)

# Expansión analógica -> F^-1(y)
signalInv=expansionAnalog(signalQ, mu, A)

# Error
signalE=signalInv-signal

# Mostrar gráficas
graph3.plot(t, signalMu, color='lightgreen', label='F(x)')
graph3.plot(t, signalInv, color='green', label='F^-1(y)')
graph3.plot(t, signalE, color='orange', label='Error')
graph3.set_title('Ley $\mu$ - 4 bits')
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

# Generar archivos de salida
nombreArchivo='munecaMu4b.wav'
wf.write(nombreArchivo, Fs, signalMu.astype('int16'))

nombreArchivo='munecaMuInv4b.wav'
wf.write(nombreArchivo, Fs, signalInv.astype('int16'))

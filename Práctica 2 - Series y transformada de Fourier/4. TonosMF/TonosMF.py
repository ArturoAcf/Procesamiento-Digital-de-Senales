# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 2 - Series y Transformada de Fourier
# Tarea 4 - Detección de Tonos Multifrecuencia

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# --------------------------------------------------------------- #

# Cargar archivo .wav

Fs, signal=wavfile.read('./digitos.wav')
signal=signal.astype(float)
t=np.arange(0, len(signal)/Fs, 1/Fs)


# --------------------------------------------------------------- #

# Procesar tonos

tamV=200 # Tamaño de cada grupo de muestras
tonos=np.zeros(len(signal), dtype=complex)

def procesarTonos(signal):
    x=np.zeros(len(signal), dtype=complex)
    for i in range(0, len(signal), tamV): # De 0 a len(signal) de 200 en 200
        x=np.fft.fft(signal[i : i+tamV]) # fft de 200 en 200 elementos de la señal
    return x

tonos=procesarTonos(signal) # fft de todas las muestras

# --------------------------------------------------------------- #

# Obtener picos

umbral=tamV**2 # Umbral para detectar los picos

def obtenerPicos(tonos):
    picos=np.zeros(len(tonos), dtype=complex)

    for i in range(0, len(tonos)):
        if(tonos[i]>umbral):
            picos[i]=abs(tonos[i]) # Módulo de los que superan el umbral
    return picos
        
picos=obtenerPicos(tonos)
freqs=np.fft.fftfreq(picos.size) # Frecuencias

print("PICOS", "\n") # Muestro los picos y aparecen 10 -> 1 por tono
for i in range(0, len(picos)):
    print(picos[i])
    
# --------------------------------------------------------------- #

# Obtener candidatos

def obtenerCandidatos(freqs):
    candidatos=freqs[abs(tonos)>umbral]*Fs # Frecuencias de los valores que superaban el umbral
    return candidatos

cand=obtenerCandidatos(freqs)

print('\n')
print("---------------------------")
print('\n')

print("CANDIDATOS", "\n")
print(cand[cand>0])

# --------------------------------------------------------------- #

# Mostrar señal

fig, fpl=plt.subplots(2)
fig.tight_layout()

fpl[0].set_title('Tonos')
fpl[0].set_xlabel('Tiempo (s)')
fpl[0].set_ylabel('Amplitud (Hz)')
fpl[0].plot(t, abs(signal), color='lightblue', label='Señal original')
fpl[0].grid()
fpl[0].legend()

fpl[1].set_title('Fourier')
fpl[1].set_xlabel('Tiempo (s)')
fpl[1].set_ylabel('Amplitud (Hz)')
fpl[1].plot(freqs, abs(picos), color='black', label='Fourier')
fpl[1].grid()
fpl[1].legend()
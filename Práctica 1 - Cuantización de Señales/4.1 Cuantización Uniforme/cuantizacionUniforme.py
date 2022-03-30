# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 1 - Cuantización de Señales
# Tarea 4.1 - Cuantización Uniforme

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------- #

# Múltiples plots

fig, graph=plt.subplots(1)
fig2, graph2=plt.subplots(1)
fig3, graph3=plt.subplots(1)
fig4, graph4=plt.subplots(1)

# fig, graph=plt.subplots(2, 2)
# fig.suptitle('Cuantización Uniforme')
#
# for g in graph.flat:
#     g.set(xlabel='Tiempo (s)', ylabel='Amplitud (Hz)')
#
# fig.tight_layout()

# --------------------------------------------------------------- #

# Generación de la señal original

Fs=100 # Frecuencia de muestreo / Ts=0.01
time=3 # Tiempo de duración de la señal
A=F=1 # Amplitud y frecuencia
t=np.arange(0, time, 1/Fs)
signal=A*np.sin(t*F*2*np.pi)

# Función para la cuantización
def quantize(s, delta):
    return delta*np.round(s/delta)

# Mostrar gráficas
graph.set_title('Cuantización Uniforme')
graph.plot(t, signal, color='black', label='Señal original')
graph.set_xlabel('Tiempo (s)')
graph.set_ylabel('Amplitud (Hz)')
graph.grid()
graph.legend()

# graph[0, 0].plot(t, signal, color='black', label='Original')
# graph[0, 0].set_title('Señal original')
# graph[0, 0].grid()

# --------------------------------------------------------------- #

# NOTA -> En este caso la saturación no tendrá ningún efecto, por lo
#         que aparecerá comentada a lo largo del ejercicio.

# Saturación

# satFijaMax=np.maximum(signal,-1)
# satFijaMin=np.minimum(satFijaMax,1)

# --------------------------------------------------------------- #

# Para 4 bits -> delta = 2/2^4 = 2/16
x=16
delta=2/x

# Cuantización
signalQ=quantize(signal, delta)

# Error
signalE=signalQ-signal

# Mostrar gráficas
graph2.plot(t, signalQ, color='blue', label='4 bits')
# graph[0, 1].plot(t, signalQ, color='blue', label='4 bits')
graph2.plot(t, signalE, color='orange', label='Error')
# graph[0, 1].plot(t, signalE, color='orange', label='Error')
graph2.set_title('Cuantización Uniforme')
graph2.plot(t, signal, color='black', label='Señal original')
graph2.set_xlabel('Tiempo (s)')
graph2.set_ylabel('Amplitud (Hz)')
graph2.grid()
graph2.legend()

# graph[0, 1].set_title('4 bits')
# graph[0, 1].grid()
# graph[0, 1].legend()

# SNR
Ex=A**2/2
SNR=10*np.log10(Ex/(delta**2/12)) # SNR teórico
print('SNR teórico para 4 bits ->', SNR, 'db')

SNRsim=10*np.log10(sum(signal*signal)/sum(signalE*signalE)) # SNR obtenido
print('SNR para 4 bits ->', SNRsim, 'db')

# --------------------------------------------------------------- #

# Para 3 bits -> delta = 2/2^3 = 2/8
x=8
delta=2/x

# Cuantización
signalQ=quantize(signal, delta)

# Error
signalE=signalQ-signal

# Mostrar gráficas
graph3.plot(t, signalQ, color='purple', label='3 bits')
# graph[1, 0].plot(t, signalQ, color='purple', label='3 bits')
graph3.plot(t, signalE, color='orange', label='Error')
# graph[1, 0].plot(t, signalE, color='orange', label='Error')
graph3.set_title('Cuantización Uniforme')
graph3.plot(t, signal, color='black', label='Señal original')
graph3.set_xlabel('Tiempo (s)')
graph3.set_ylabel('Amplitud (Hz)')
graph3.grid()
graph3.legend()

# graph[1, 0].set_title('3 bits')
# graph[1, 0].grid()
# graph[1, 0].legend()

# SNR
Ex=A**2/2
SNR=10*np.log10(Ex/(delta**2/12)) # SNR teórico
print('SNR teórico para 3 bits ->', SNR, 'db')

SNRsim=10*np.log10(sum(signal*signal)/sum(signalE*signalE)) # SNR obtenido
print('SNR para 3 bits ->', SNRsim, 'db')

# --------------------------------------------------------------- #

# Para 2 bits -> delta = 2/2^2 = 2/4
x=4
delta=2/x

# Cuantización
signalQ=quantize(signal, delta)

# Error
signalE=signalQ-signal

# Mostrar gráficas
graph4.plot(t, signalQ, color='grey', label='2 bits')
# graph[1, 1].plot(t, signalQ, color='grey', label='2 bits')
graph4.plot(t, signalE, color='orange', label='Error')
# graph[1, 1].plot(t, signalE, color='orange', label='Error')
graph4.set_title('Cuantización Uniforme')
graph4.plot(t, signal, color='black', label='Señal original')
graph4.set_xlabel('Tiempo (s)')
graph4.set_ylabel('Amplitud (Hz)')
graph4.grid()
graph4.legend()

# graph[1, 1].set_title('2 bits')
# graph[1, 1].grid()
# graph[1, 1].legend()

# SNR
Ex=A**2/2
SNR=10*np.log10(Ex/(delta**2/12)) # SNR teórico
print('SNR teórico para 2 bits ->', SNR, 'db')

SNRsim=10*np.log10(sum(signal*signal)/sum(signalE*signalE)) # SNR obtenido
print('SNR para 2 bits ->', SNRsim, 'db')

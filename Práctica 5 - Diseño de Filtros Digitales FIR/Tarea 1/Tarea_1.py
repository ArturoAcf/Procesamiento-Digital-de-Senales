# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 5 - Diseño de Filtros Digitales FIR
# Tarea 1 - Filtro FIR de fase lineal

import pds
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------------- #

# Filtro FIR

def FIR(M,Wc):
	h=np.zeros(M)
	for n in range(0,M):
		if n!=(M-1)/2:
			h[n]=(np.sin(Wc*(n-(M-1)/2)))/(np.pi*(n-(M-1)/2))
		else:
			h[n]=Wc/np.pi
	return h

# Hamming

def FIRAtenuado(M,Wc):
	h=np.zeros(M)
	hamming=np.hamming(M)
	for n in range(0,M):
		if n != (M-1)/2:
			h[n]=(np.sin(Wc*(n-(M-1)/2)))/(np.pi*(n-(M-1)/2))
		else:
			h[n]=Wc/np.pi
	h=hamming*h
	return h

# --------------------------------------------------------------- #

# Mostrar la gráfica

M=31
Wc=np.pi/2
h=FIR(M,Wc)

plt.figure()
plt.title("Filtro FIR")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.plot(h,label="h")
plt.legend()
plt.grid()
plt.show()

# --------------------------------------------------------------- #

# Respuesta en frecuencia

a=1
b=h

plt.figure()
pds.plot_freq_resp(b,a)
h2=FIRAtenuado(M,Wc)

a2=1
b2=h2

plt.figure()
pds.plot_freq_resp(b2,a2)

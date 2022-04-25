# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 3 - Sistemas discretos. Respuesta temporal
# Tarea 3 - Analizar un sistema FIR

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# --------------------------------------------------------------- #

# Múltiples plots

fig, graph=plt.subplots(1)
fig2, graph2=plt.subplots(1)
fig3, graph3=plt.subplots(1)
fig4, graph4=plt.subplots(1)

# --------------------------------------------------------------- #

# a y b

a=np.zeros(10)
a[0]=1
b=np.ones(10)
b=b/10

# --------------------------------------------------------------- #

# FIR - Respuesta al impulso

x=np.zeros(30) # Impulso
x[0]=1
x=np.concatenate((np.zeros(10), x))

t=np.zeros_like(x)
for i in range(0, 10):
    t[i]=i-10

# pre-pend ceros
y=np.zeros_like(x)
y[:10]=x[:10]

# inicializamos las 3 primeras muestras
for n in range(10, len(x)):
    xn=x[n:n-10:-1]
    # muestras de x en orden descendente
    yn=y[n:n-10:-1]
    # muestras de y en orden descendente
    y[n]=np.dot(-a,yn)+np.dot(b,xn)
    t[n]=n-10

y2=signal.lfilter(b, a, x) # Para comprobar
h=y2.copy() # Respuesta al impulso para convolución
hx=x.copy()

# --------------------------------------------------------------- #

# Mostrar gráficas

graph.stem(t, y, label="Y")
graph.stem(t, y2, label="Y2") # Correcto
graph.set_xlabel("Tiempo (s)")
graph.set_ylabel("Amplitud (Hz)")
graph.set_title("Filtro FIR - Respuesta al impulso")
graph.legend()
graph.grid()

# --------------------------------------------------------------- #

# FIR - Respuesta al escalón

x=np.ones(30) # Escalón
x=np.concatenate((np.zeros(10), x))

t=np.zeros_like(x)
for i in range(0, 10):
    t[i]=i-10

# pre-pend ceros
y=np.zeros_like(x)
y[:10]=x[:10]

# inicializamos las 3 primeras muestras
for n in range(10, len(x)):
    xn=x[n:n-10:-1]
    # muestras de x en orden descendente
    yn=y[n:n-10:-1]
    # muestras de y en orden descendente
    y[n]=np.dot(-a,yn)+np.dot(b,xn)
    t[n]=n-10

y2=signal.lfilter(b, a, x) # Para comprobar
hx2=x.copy()

# --------------------------------------------------------------- #

# Mostrar gráficas

graph2.stem(t, y, label="Y")
graph2.stem(t, y2, label="Y2") # Correcto
graph2.set_xlabel("Tiempo (s)")
graph2.set_ylabel("Amplitud (Hz)")
graph2.set_title("Filtro FIR - Respuesta al escalón")
graph2.legend()
graph2.grid()

# --------------------------------------------------------------- #

# Convolución

y3=signal.convolve(h, hx) # Impulso
y4=signal.convolve(h, hx2) # Escalón

# --------------------------------------------------------------- #

# Mostrar gráficas - Convolución

graph3.stem(y3, label="Y3") # Correcto
graph3.set_xlabel("Tiempo (s)")
graph3.set_ylabel("Amplitud (Hz)")
graph3.set_title("Convolución - Impulso")
graph3.legend()
graph3.grid()

graph4.stem(y4, label="Y4") # Correcto
graph4.set_xlabel("Tiempo (s)")
graph4.set_ylabel("Amplitud (Hz)")
graph4.set_title("Convolución - Escalón")
graph4.legend()
graph4.grid()

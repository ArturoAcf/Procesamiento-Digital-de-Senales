# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 3 - Sistemas discretos. Respuesta temporal
# Tarea 2 - Analizar otro sistema IIR

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# --------------------------------------------------------------- #

# Múltiples plots

fig, graph=plt.subplots(1)
fig2, graph2=plt.subplots(1)

# --------------------------------------------------------------- #

# a y b

a=np.array([1, -2.5, 1])
b=np.array([4, 0, 0])

# --------------------------------------------------------------- #

# IIR - Respuesta al impulso

x=np.zeros(30) # Impulso
x[0]=1
x=np.concatenate((np.zeros(3), x))

t=np.zeros_like(x)
t[0]=-3
t[1]=-2
t[2]=-1

# pre-pend ceros
y=np.zeros_like(x)
y[:3]=x[:3]

# inicializamos las 3 primeras muestras
for n in range(3, len(x)):
    xn=x[n:n-3:-1]
    # muestras de x en orden descendente
    yn=y[n:n-3:-1]
    # muestras de y en orden descendente
    y[n]=np.dot(-a,yn)+np.dot(b,xn)
    t[n]=n-3

y2=signal.lfilter(b, a, x) # Para comprobar

# --------------------------------------------------------------- #

# Mostrar gráficas

graph.stem(t, y, label="Y")
graph.stem(t, y2, label="Y2") # Correcto
graph.set_xlabel("Tiempo (s)")
graph.set_ylabel("Amplitud (Hz)")
graph.set_title("Filtro IIR - Respuesta al impulso")
graph.legend()
graph.grid()


# --------------------------------------------------------------- #

# IIR - Respuesta al escalón

x=np.ones(30) # Escalón
x=np.concatenate((np.zeros(3), x))

t=np.zeros_like(x)
t[0]=-3
t[1]=-2
t[2]=-1

# pre-pend ceros
y=np.zeros_like(x)
y[:3]=x[:3]

# inicializamos las 3 primeras muestras
for n in range(3, len(x)):
    xn=x[n:n-3:-1]
    # muestras de x en orden descendente
    yn=y[n:n-3:-1]
    # muestras de y en orden descendente
    y[n]=np.dot(-a,yn)+np.dot(b,xn)
    t[n]=n-3

y2=signal.lfilter(b, a, x) # Para comprobar

# --------------------------------------------------------------- #

# Mostrar gráficas

graph2.stem(t, y, label="Y")
graph2.stem(t, y2, label="Y2") # Correcto
graph2.set_xlabel("Tiempo (s)")
graph2.set_ylabel("Amplitud (Hz)")
graph2.set_title("Filtro IIR - Respuesta al escalón")
graph2.legend()
graph2.grid()

# --------------------------------------------------------------- #

# El sistema es inestable al tender a infinito

# --------------------------------------------------------------- #

# Impulso -> 1 0 0 0 0 0 . . .
# Escalon -> 0 0 0 1 0.5 . . .

# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 4 - Transformada Z y respuesta en frecuecncia
# Tarea 3 - Segundo sistema

import numpy as np
import pds
import matplotlib.pyplot as plt
import scipy.signal as signal

# --------------------------------------------------------------- #

# a y b

a=np.array([1, 0.5, -0.25])
b=np.array([1, 0.5, 0])
n=np.linspace(-20, 100, 121)

# --------------------------------------------------------------- #

# Respuesta impulsiva

plt.figure()
pds.impz(b, a, n)

# --------------------------------------------------------------- #

# Diagrama de ceros y polos

plt.figure()
pds.zplane(b, a)

# Es estable ya que los polos están dentro de la circunferencia

# --------------------------------------------------------------- #

# y(n) para x(n) = 2*0.9^n*u(n)

u1=np.zeros(20)
u2=np.ones(101)
u=np.concatenate((u1, u2))
x=2*0.9**n*u
y=signal.lfilter(b, a, x)

plt.figure()
plt.stem(y, label="y(n)")
plt.title("Salida y(n) para x(n) = 2*0.9^n*u(n)")
plt.legend()
plt.grid()

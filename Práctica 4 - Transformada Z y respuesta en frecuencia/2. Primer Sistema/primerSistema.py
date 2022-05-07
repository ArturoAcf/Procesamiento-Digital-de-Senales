# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 4 - Transformada Z y respuesta en frecuecncia
# Tarea 2 - Primer sistema

import numpy as np
import pds
import matplotlib.pyplot as plt

# --------------------------------------------------------------- #

# a y b

a=np.array([1, -1, 0.9])
b=np.array([1, 0, 0])
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

# Magnitud y fase

plt.figure()
pds.plot_freq_resp(b, a, worN=None)

# --------------------------------------------------------------- #

# Respuesta al escalón

plt.figure()
pds.stepz(b, a, n)

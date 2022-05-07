# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 4 - Transformada Z y respuesta en frecuecncia
# Tarea 5 - Cuarto sistema

import numpy as np
import pds
import matplotlib.pyplot as plt

# --------------------------------------------------------------- #

# h(n)

h=np.array([0.0023, 0.0053, 0.0411, - 0.1233, -0.2310, 0.3087, 0.3087, -0.2310, -0.1233, 0.0411, 0.0053, 0.0023])

# --------------------------------------------------------------- #

# Magnitud y fase

plt.figure()
pds.plot_freq_resp(h)

# --------------------------------------------------------------- #

# Respuesta al escalón unitario

plt.figure()
n=np.linspace(-20, 40, 61)
pds.stepz(h, 1, n) # a=1 -> Unitario
plt.grid()

# --------------------------------------------------------------- #

# Retardo

plt.figure()
pds.plot_group_delay(h, 1) # Retardo -> 5.5

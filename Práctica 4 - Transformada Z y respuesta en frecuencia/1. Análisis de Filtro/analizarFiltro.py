# Realizado por: Arturo Alonso Carbonero
# Grupo: 4ºA - Curso: 21-22

# Práctica 4 - Transformada Z y respuesta en frecuecncia
# Tarea 1 - Analizar filtro FIR

import numpy as np
import pds

# --------------------------------------------------------------- #

# a y b

a=np.zeros(10)
a[0]=1
b=np.ones(10)
b=b/10

# --------------------------------------------------------------- #

# Mostrar con plot_freq_resp()

pds.plot_freq_resp(b, a=1, worN=None)

# --------------------------------------------------------------- #

# Frecuencia de corte -> 0.28

# --------------------------------------------------------------- #

# Tipo de filtro -> Filtro paso alta ya que únicamente pasa las frecuecnias 
# que se encuenten por encima de los -3dB (rechazando el resto)
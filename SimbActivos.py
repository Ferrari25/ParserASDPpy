from Primeros import * 
from Siguientes import *

# Conjunto de símbolos activos (terminales activos)
activos = set()

# Agrega los símbolos terminales que aparecen en los primeros conjuntos de los símbolos no terminales
for no_terminal, conjunto_primeros in primeros.items():
    activos |= conjunto_primeros

# Agrega los símbolos terminales que aparecen en los siguientes conjuntos de los símbolos no terminales
for no_terminal, conjunto_siguientes in siguientes.items():
    activos |= conjunto_siguientes



## EXPLICACION 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
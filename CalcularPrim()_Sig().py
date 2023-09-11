from Gramatica import *
from Primeros import * 
from Siguientes import *

# Calcular los primeros y siguientes para todos los símbolos no terminales
for no_terminal in grammar:
    calcular_primeros(no_terminal)
    calcular_siguientes(no_terminal)
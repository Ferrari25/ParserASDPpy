from Gramtica import *
from Primeros import *

# Conjuntos siguientes
siguientes = {}

# Función para calcular los siguientes de un símbolo
def calcular_siguientes(no_terminal):
    if no_terminal in siguientes:
        return

    siguientes[no_terminal] = set()

    if no_terminal == 'simbolo_distinguido':
        siguientes[no_terminal].add('$') 

    for no_terminal, producciones in grammar.items():
        for produccion in producciones:
            for i, simb in enumerate(produccion):
                if simb == no_terminal:
                    if i < len(produccion) - 1:
                        siguientes[no_terminal] |= primeros[produccion[i + 1]]
                    if i == len(produccion) - 1 or all(x == 'ε' for x in produccion[i + 1:]):
                        if no_terminal != no_terminal:
                            calcular_siguientes(no_terminal)
                            siguientes[no_terminal] |= siguientes[no_terminal]
                            
                            

## EXPLICACION 
# si el t ∈ VN 
# crea un numero conjunto para ese simbolo t 
# si t es el simbolo distinguido, por lo menos aparecera el fin de cadena ya que se entiende que la gramatica esta ampliada (con la marca de EOF)
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

#en el bucle for i, simb in enumerate(produccion): 
#i representa el índice del símbolo actual en la producción, y simb representa el valor (el símbolo en sí) del símbolo actual.
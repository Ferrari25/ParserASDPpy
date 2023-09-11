from Gramatica import *


# Conjunto de símbolos anulables
anulables = set()

# Paso 1: Inicializar el conjunto de símbolos anulables con aquellos que tienen producciones ε
for no_terminal, producciones in grammar.items():
    for produccion in producciones:
        if 'ε' in produccion:
            anulables.add(no_terminal)

# Paso 2: Iterar hasta que no haya cambios en el conjunto de símbolos anulables
cambio = True
while cambio:
    cambio = False
    for no_terminal, producciones in grammar.items():
        for produccion in producciones:
            if all(simbolo in anulables for simbolo in produccion):
                if no_terminal not in anulables:
                    anulables.add(no_terminal)
                    cambio = True
                    
                    
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
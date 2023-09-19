from Gramatica import *

#Conjuntos primeros y siguientes
primeros = {}

# Función para calcular los primeros de un símbolo
def calcular_primeros(no_terminal):
    if no_terminal in primeros:
        return

    primeros[no_terminal] = set()
    
    for produccion in P[no_terminal]:
        for simbolo_en_produccion in produccion:
            if simbolo_en_produccion.islower() or simbolo_en_produccion == 'ε':
                primeros[no_terminal].add(simbolo_en_produccion)
                break  # Salir después de agregar el primer símbolo terminal o ε
            elif simbolo_en_produccion in P:
                calcular_primeros(simbolo_en_produccion)
                primeros[no_terminal] |= primeros[simbolo_en_produccion]
            else:
                break  # Salir si encontramos un símbolo terminal diferente de ε
            
            
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
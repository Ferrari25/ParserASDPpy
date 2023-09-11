from Gramtica import *
from SimboloInicial import *

alcanzables = set()

# Función para realizar una búsqueda en profundidad desde un símbolo no terminal
def buscar_alcanzables(no_terminal):
    alcanzables.add(no_terminal)
    for producciones in grammar.get(no_terminal, []):
        for simbolo_producido in producciones:
            if simbolo_producido in grammar and simbolo_producido not in alcanzables:
                buscar_alcanzables(simbolo_producido)

# Realizar la búsqueda en profundidad desde el símbolo inicial
buscar_alcanzables(simbolo_distinguido)


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

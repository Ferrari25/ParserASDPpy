grammar = {
    'S': [['A', 'B'], ['B', 'C']],
    'A': [['a', 'A'], []],
    'B': [['b', 'B'], []],
    'C': [['c', 'C'], []],
    'D': [['d','D'],['d']]
}

simbolo_inicial = 'S'
primeros = {}
siguientes = {}
activos = {}
alcanzables = {}
anulables = {}
todos_no_terminales = {grammar.keys()}

no_alcanzables = todos_no_terminales - alcanzables

#####################################################################################################################################################
# Función para calcular los primeros de un símbolo
def calcular_primeros(no_terminal):
    if no_terminal in primeros:
        return

    primeros[no_terminal] = set()
    
    for produccion in grammar[no_terminal]:
        for simbolo_en_produccion in produccion:
            if simbolo_en_produccion.islower() or simbolo_en_produccion == 'ε':
                primeros[no_terminal].add(simbolo_en_produccion)
                break  # Salir después de agregar el primer símbolo terminal o ε
            elif simbolo_en_produccion in grammar:
                calcular_primeros(simbolo_en_produccion)
                primeros[no_terminal] |= primeros[simbolo_en_produccion]
            else:
                break  # Salir si encontramos un símbolo terminal diferente de ε

#####################################################################################################################################################
# Función para calcular los siguientes de un símbolo
def calcular_siguientes(no_terminal):
    if no_terminal in siguientes:
        return

    siguientes[no_terminal] = set()

    if no_terminal == 'S':
        siguientes[no_terminal].add('$')  # Agrega el símbolo de fin de entrada al inicio

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

#####################################################################################################################################################
#Proceso por el cual calcula los anulables
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
                    
#####################################################################################################################################################
# Función para realizar una búsqueda en profundidad desde un símbolo no terminal
def buscar_alcanzables(no_terminal):
    alcanzables.add(no_terminal)
    for producciones in grammar.get(no_terminal, []):
        for simbolo_producido in producciones:
            if simbolo_producido in grammar and simbolo_producido not in alcanzables:
                buscar_alcanzables(simbolo_producido)

# Realizar la búsqueda en profundidad desde el símbolo inicial
buscar_alcanzables(simbolo_inicial)

#####################################################################################################################################################


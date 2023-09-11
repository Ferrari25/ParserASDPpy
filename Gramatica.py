# Definición de la gramática
# Diccionario = {key, value}

grammar = {
    'S': [['A', 'B'], ['B', 'C']],
    'A': [['a', 'A'], []],
    'B': [['b', 'B'], []],
    'C': [['c', 'C'], []],
    'D': [['d','D'],['d']]
}
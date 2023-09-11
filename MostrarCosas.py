from Primeros import * 
from Siguientes import *
from NoAlcanzables import * 
from Alcanzables import *
from SimbActivos import *
from Anulables import *



# Ahora el conjunto 'no_alcanzables' contiene los símbolos no terminales no alcanzables desde el símbolo inicial.
print("Símbolos no alcanzables:", no_alcanzables)

# Ahora el conjunto 'alcanzables' contiene los símbolos no terminales alcanzables desde el símbolo inicial.
print("Símbolos alcanzables:", alcanzables)

# Ahora el conjunto 'activos' contiene los símbolos terminales activos en la gramática.
print("Símbolos activos (terminales activos):", activos)


# Ahora el conjunto 'anulables' contiene los símbolos anulables
print("Símbolos anulables:", anulables)

# Imprimir los conjuntos primeros y siguientes
print("Conjuntos Primeros:")
for simbolo, conjunto in primeros.items():
    print(f"{simbolo}: {conjunto}")

print("\nConjuntos Siguientes:")
for simbolo, conjunto in siguientes.items():
    print(f"{simbolo}: {conjunto}")
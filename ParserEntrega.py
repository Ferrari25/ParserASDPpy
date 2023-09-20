from Automatas import *           #trae los automatas que utiliza el lexer
from Lexer import *               #trae el lexer
from Gramatica import *           #trae producciones, VT, VN
from GPSD import *                #no usa nada aun pero igual lo traigo para probar cosas xd


######### PROCEDIMIENTO PARA UN ASD con RETROCESO ############

def parser (lista_tokens):
    datos_parser = {
        'tokens' : TOKENS_POSIBLES,
        'posicion indice' : 0,
        'error' : False,
    }


def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['TOKENS_POSIBLES'][datos_locales['index']][0]
            #lexema_actual = datos_locales['lista_tokens'][datos_locales['index']][1]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                
  def pni(no_terminal):
        for cuerpo_produccion in P[no_terminal]:
            backtracking_index = datos_locales['index']
            procesar(cuerpo_produccion)
            if datos_locales['error']:
                datos_locales['index'] = backtracking_index
            else:
                break


def principal():
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != '#' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True

from Automatas import *
from Lexer import *

VN = ['Program', 'ListaSentencias', 'Sentencia', 'SentenciaSi',
                    'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                    'SentenciaFun','Proc', 'ListaPar', 'Expression', 'Expresion2', 'Factor',
                    'Termino'
                ]


VT = ["SI","FINSI","OPSUM","OPMULT","EQUAL","LEER","MOSTRAR","REPETIR",
              "HASTA","ENTONCES","MIENTRAS","FUNC","FINFUNC","OPEREL","PUNTO-COMA",
              "Parentensis Cerrado","Parentensis Abierto","NUM","ID"]



P = {
    'Program': [['ListaSentencias']],
    
    'ListaSentencias' : [
                          ['ListaSentencias','PUNTO-COMA','Sentencia'],
                          ['Sentencia']
                        ],
    
    'Sentencia' : [ 
                    ['SentenciaSi'],
                    ['SentenciaRepetir'],
                    ['SentenciaAsig'],
                    ['SentenciaLeer'],
                    ['SentenciaMostrar'],
                    ['SetenciaFun']
                   ],
    
    'SentenciaSi' : [
                     ['SI','Expression','ENTONCES','ListaSentencias','SINO','ListaSentencias','FINSI'],
                     ['SI','Expression','ENTONCES','ListaSentencias','FINSI']
                    ],
    
    'SentenciaRepetir': [  ['REPETIR','ListaSentencias','HASTA','Expression']  ],
    
    'SentenciaAsig': [  ['ID','EQUAL', 'Expression']  ],
    
    'SentenciaLeer' : [  ['LEER', 'ID']  ],
    
    'SentenciaMostrar': [  ['MOSTRAR', 'EXpression']  ],
    
    'SentenciaFun': [  ['FUNC', 'Proc', 'FINFUNC']  ],
    
    'Proc': [  ['ID', 'Parentensis Abierto' , 'ListaPar' , 'Parentensis Cerrado','ListaSentencias']  ],
    
    'ListaPar': [ ['ListaPar','PUNTO-COMA','ID'], 
                   ['ID']
                ],
    
    'Expression': [ ['Expresion2', 'OPEREL','Expresion2'],
                    ['Expresion2'] 
                  ],
    
    'Expresion2': [ ['Expresion2', 'OPEREL', 'Expresion2'], 
                    [ 'Termino' ]
                  ],
    
    'Termino': [ ['Termino','OPTMULT','Factor'],
                 ['Factor']
               ],
    
    'Factor': [ ['Parentesis Abierto', 'Expression', 'Parentesis Cerrado'],
                ['NUM'],
                ['ID']
              ]
}


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


def principal():
        pni('S')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != 'Eof' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    return principal()
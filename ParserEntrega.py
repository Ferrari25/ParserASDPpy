from Automatas import *
from Lexer import *

VN = ['Program', 'ListaSentencias', 'Sentencia', 'SentenciaSi',
                    'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                    'SentenciaFun','Proc', 'ListaPar', 'Expression', 'Expresion2', 'Factor',
                    'Termino','ListaSentencias2','ListaPar2','Expresion2','Termino2'
                ]


VT = ["SI","FINSI","OPSUM","OPMULT","EQUAL","LEER","MOSTRAR","REPETIR",
              "HASTA","ENTONCES","MIENTRAS","FUNC","FINFUNC","OPEREL","PUNTO-COMA",
              "Parentensis Cerrado","Parentensis Abierto","NUM","ID"]

###SIMBOLOS DIRECTRICES###
 ### RECORDAR QUE SE COPIAN LOS TOKEN ###
SD(Program->ListaSentencias) = {si,repetir,id,leer,mostrar,func}
SD(ListaSentencia -> Sentencia) = {si,repetir,id,leer,mostrar,func}
SD(ListaSentencia2 -> 'PUNTO-COMA','Sentencias','ListaSentencias2' ) = {PUNTO-COMA}
SD(Sentencia -> SentenciaSi) = {SI}
SD(SentenciaSi2 -> 
SD(Setencia -> SentenciaRepertir) = {REPETIR}
SD(Sentencia -> SentenciaAsig) = {ID}
SD(Sentencia -> SentenciaLeer) = {LEER}
SD(Sentencia -> SentenciaMostrar) = {MOSTRAR}
SD(Sentencia -> SentenciaFun) = {FUNC}


###OBERSERVACIONES##
COMO LA INTERSECCION DE TODAS LAS PRODUCCIONES CON SU MISMO NO-TERMINAL ES VACIA, LA GRAMATICA ES LL(1)


P = {
    'Program': [['ListaSentencias']],

    
    'ListaSentencias' : [
                         ['Sentencia','ListaSentencias2']
                        ] 
    'ListaSentencias2' : [['PUNTO-COMA','Sentencias','ListaSentencias2'], []]

    
    'Sentencia' : [ 
                    ['SentenciaSi'],
                    ['SentenciaRepetir'],
                    ['SentenciaAsig'],
                    ['SentenciaLeer'],
                    ['SentenciaMostrar'],
                    ['SetenciaFun']
                   ],
    
    'SentenciaSi' : [
                     ['SI','Expression','ENTONCES','ListaSentencias','SentenciaSi2']
                    ]
    'SentenciaSi2' : [['SINO','ListaSentencia','FIN-SI'],['FIN-SI]]
    
    'SentenciaRepetir': [  ['REPETIR','ListaSentencias','HASTA','Expression']  ],
    
    'SentenciaAsig': [  ['ID','EQUAL', 'Expression']  ],
    
    'SentenciaLeer' : [  ['LEER', 'ID']  ],
    
    'SentenciaMostrar': [  ['MOSTRAR', 'EXpression']  ],
    
    'SentenciaFun': [  ['FUNC', 'Proc', 'FINFUNC']  ],
    
    'Proc': [  ['ID', 'Parentensis Abierto' , 'ListaPar' , 'Parentensis Cerrado','ListaSentencias']  ],
    
    'ListaPar': [['ID','ListaPar2'] ]


    'ListaPar2': [['PUNTO-COMA', 'ID', 'ListaPar2'],[]]
  
                
    
    'Expression': [ ['Expresion2', 'OPEREL','Expresion2'],
                    ['Expresion2'] 
                  ],
    
    'Expresion2': [['Termino','Expresion22']] 

    'Expresion22': [['OPSUM', 'Termino', 'Expresion22'],[]]
    
    'Termino': [['Factor' , 'Termino2']] 

    'Termino2':[['OPMULT','Termino','Termino2'],[]]
    
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

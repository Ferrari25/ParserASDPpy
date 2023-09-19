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
SD(ListaSentencia2 -> λ )  = {#}
SD(Sentencia -> SentenciaSi) = {SI}
SD(Sentencia -> SentenciaRepertir) = {REPETIR}
SD(Sentencia -> SentenciaAsig) = {ID}
SD(Sentencia -> SentenciaLeer) = {LEER}
SD(Sentencia -> SentenciaMostrar) = {MOSTRAR}
SD(SentenciaRepetir -> 'REPETIR','ListaSentencias','HASTA','Expression') = {REPETIR}
SD(Sentencia -> SentenciaFun) = {FUNC}
SD(SentenciaSi ->'SI','Expression','ENTONCES','ListaSentencias','SentenciaSi2') = {SI}
SD(SentenciaSi2 -> 'SINO','ListaSentencia','FIN-SI') ={ SINO}
SD(SentenciaSi2 -> FINSI) = {FIN-SI}
SD(SentenciaRepetir -> ) = {REPETIR}
SD(SentenciaAsig -> ) = {ID}
SD(SentenciaLeer -> ) = {LEER}
SD(SentenciaMostrar ->) = {MOSTRAR}
SD(SentenciaFun -> ) = {FUNC}
SD(Proc -> ) = {ID}
SD(ListaPar ->  ) = {ID}
SD(ListaPar2 -> 'PUNTO-COMA', 'ID', 'ListaPar2') = {PUNTO-COMA}
SD(ListaPar2 -> λ)  = { ( }
SD(Expression -> 'Expresion2', 'ExpressionPrima') = {(,NUM,ID}
SD(ExpresionPrima -> 'OPEREL','Expression2') {OPEREL}
SD(ExpresionPrima -> Lamda) ={ ( }
SD(Exrepssion2 -> 'Termino','Expresion22') = {(, NUM,ID}
SD(Expression22 -> OPTSUMA Termno Expersion22) ={OPTSuma}
SD(Expression22 -> Lambda) ={}
SD(Termino -> Factor Termino2) = {( , NUM , ID}
SD(Termino -> OPTMULT Factor TErmino2) = {OPTMULT}
SD(Termino2 -> lambda) = {...............................................}
SD(Factor -> '(' 'Expresion' ')' )= { ( }
SD(Factor -> NUM)= {NUM}
SD(Factor -> ID) = {ID}

###OBERSERVACIONES##
###COMO LA INTERSECCION DE TODAS LAS PRODUCCIONES CON SU MISMO NO-TERMINAL ES VACIA, LA GRAMATICA ES LL(1)###


P = {
    'Program': [['ListaSentencias']],

    
    'ListaSentencias' : [['Sentencia','ListaSentencias2']] ,
    'ListaSentencias2' : [['PUNTO-COMA','Sentencias','ListaSentencias2'], []],

    
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
                    ],
    'SentenciaSi2' : [['SINO','ListaSentencia','FIN-SI'],['FIN-SI']],
    
    'SentenciaRepetir': [  ['REPETIR','ListaSentencias','HASTA','Expression']  ],
    
    'SentenciaAsig': [  ['ID','EQUAL', 'Expression']  ],
    
    'SentenciaLeer' : [  ['LEER', 'ID']  ],
    
    'SentenciaMostrar': [  ['MOSTRAR', 'Expression']  ],
    
    'SentenciaFun': [  ['FUNC', 'Proc', 'FINFUNC']  ],
    
    'Proc': [  ['ID', 'Parentensis Abierto' , 'ListaPar' , 'Parentensis Cerrado','ListaSentencias']  ],
    
    'ListaPar': [['ID','ListaPar2'] ],


    'ListaPar2': [['PUNTO-COMA', 'ID', 'ListaPar2'],[]],
    
    'Expression': [ ['Expresion2', 'ExpressionPrima']],
    'ExpressionPrima' : [[λ],['OPEREL','Expression2']],
    
    'Expresion2': [['Termino','Expresion22']] ,

    'Expresion22': [['OPSUM', 'Termino', 'Expresion22'],[]],
    
    'Termino': [['Factor' , 'Termino2']] ,

    'Termino2':[['OPMULT','Termino','Termino2'],[]],
    
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

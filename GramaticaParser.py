VN = ['Program', 'ListaSentencias', 'Sentencia', 'SentenciaSi',
                    'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                    'SentenciaFun','Proc', 'ListaPar', 'Expression', 'Expresion2', 'Factor',
                    'Termino','ListaSentencias2','ListaPar2','Expresion2','Termino2'
                ]


VT = ["SI","FINSI","OPSUM","OPMULT","EQUAL","LEER","MOSTRAR","REPETIR",
              "HASTA","ENTONCES","MIENTRAS","FUNC","FINFUNC","OPEREL","PUNTO-COMA",
              "Parentensis Cerrado","Parentensis Abierto","NUM","ID"]


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
    'ExpressionPrima' : [[],['OPEREL','Expression2']],
    
    'Expresion2': [['Termino','Expresion22']] ,

    'Expresion22': [['OPSUM', 'Termino', 'Expresion22'],[]],
    
    'Termino': [['Factor' , 'Termino2']] ,

    'Termino2':[['OPMULT','Termino','Termino2'],[]],
    
    'Factor': [ ['Parentesis Abierto', 'Expression', 'Parentesis Cerrado'],
                ['NUM'],
                ['ID']
              ]
}
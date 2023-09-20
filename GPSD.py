P_GPSD = {
    #'NOTERMINAL' : [{"produccion":['alfa1','alfa2',], "SD" :['beta1','beta2']}],
    'Program': [{"produccion": ['ListaSentencias'],"SD": ["a","b","c"],}], 
    
    'ListaSentencias' : [{"produccion" : ['Sentencia','ListaSentencias2'] , "SD" : ['SI','REPETIR','ID','LEER','MOSTRAR','FUNC']}],
    'ListaSentencias2' : [{"produccion":['PUNTO-COMA','Sentencias','ListaSentencias2'], "SD" :['PUNTO-COMA']}],
    'ListaSentencias2' : [{"produccion":[], "SD" :['#', 'FIN-FUNC',  'FIN-SI' ,'SINO' ,'HASTA']}],
    
    'Sentencia' : [{"produccion":['SentenciaSi'], "SD" :['SI']}],
    'Sentencia' : [{"produccion":['SentenciaRepetir'], "SD" :['REPETIR']}],
    'Sentencia' : [{"produccion":['SentenciaAsig'], "SD" :['ID']}], 
    'Sentencia' : [{"produccion":['SentenciaLeer'], "SD" :['LEER']}],
    'Sentencia' : [{"produccion":['SentenciaMostrar'], "SD" :['MOSTRAR']}],
    'Sentencia' : [{"produccion":['SetenciaFun'], "SD" :['FUNC']}],
    
    'SentenciaSi' : [{"produccion":['SI','Expression','ENTONCES','ListaSentencias','SentenciaSi2'], "SD" :['SI']}],
    'SentenciaSi2' : [{"produccion":['SINO','ListaSentencia','FIN-SI'], "SD" :['SINO']}],
    'SentenciaSi' : [{"produccion":['FIN-SI'], "SD" :['FIN-SI']}],
    
    'SentenciaRepetir' : [{"produccion":['REPETIR','ListaSentencias','HASTA','Expression'], "SD" :['REPETIR','ListaSentencias','HASTA','Expression']}],
    'SentenciaAsig' : [{"produccion":['ID','EQUAL', 'Expression'], "SD" :['ID']}],
    'SentenciaLeer' : [{"produccion":['LEER', 'ID'], "SD" :['LEER']}],
    'SentenciaMostrar' : [{"produccion":['MOSTRAR', 'Expression'], "SD" :['MOSTRAR']}],
    'SetenciaFun' : [{"produccion":['FUNC', 'Proc', 'FINFUNC'], "SD" :['FUNC']}],
    
    'Proc' : [{"produccion":['ID', 'Parentensis Abierto' , 'ListaPar' , 'Parentensis Cerrado','ListaSentencias'], "SD" :['ID']}],
    
    'ListaPar' : [{"produccion":['ID','ListaPar2'], "SD" :['ID']}],
    'ListaPar2' : [{"produccion":['PUNTO-COMA', 'ID', 'ListaPar2'], "SD" :['PUNTO-COMA']}],
    'ListaPar2' : [{"produccion":[], "SD" :['Parentensis Cerrado']}],
    
    'Expression' : [{"produccion":['Expresion2', 'ExpressionPrima'], "SD" :['Parentensis Cerrado','NUM','ID']}],
    
    'ExpressionPrima' : [{"produccion":['OPEREL','Expression2'], "SD" :['OPEREL']}],
    'ExpressionPrima' : [{"produccion":[], "SD" :['Parentensis Cerrado', '#' ,'PUNTO-COMA', 'FIN-FUNC' ,'FIN-SI' ,'SINO', 'HASTA', 'ENTONCES']}],
    
    'Expresion2' : [{"produccion":['Termino','Expresion22'], "SD" :['Parentensis Cerrado','NUM','ID']}],
    'Expresion22' : [{"produccion":['OPSUM', 'Termino', 'Expresion22'], "SD" :['OPSUM']}],
    'Expresion22' : [{"produccion":[], "SD" :['Parentensis Cerrado', '#' ,'PUNTO-COMA', 'FIN-FUNC' ,'FIN-SI' ,'SINO', 'HASTA', 'ENTONCES']}],
    
    'Termino' : [{"produccion":['Factor' , 'Termino2'], "SD" :['Parentesis Abierto', 'NUM' , 'ID']}],
    
    'Termino2' : [{"produccion":['OPMULT','Termino','Termino2'], "SD" :['OPMULT']}],
    'Termino2' : [{"produccion":[], "SD" :['Parentensis Cerrado', '#' ,'PUNTO-COMA', 'FIN-FUNC' ,'FIN-SI' ,'SINO', 'HASTA', 'ENTONCES']}],
    
    
    'Factor' : [{"produccion":['Parentesis Abierto', 'Expression', 'Parentesis Cerrado'], "SD" :['Parentesis Abierto']}],
    'Factor' : [{"produccion":['NUM'], "SD" :['NUM']}],
    'Factor' : [{"produccion":['ID'], "SD" :['ID']}],
    
    
    } 



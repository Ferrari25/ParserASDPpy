from Automatas import *

#Lexer
def lexer(codigo_fuente): 
    #codigo_fuente=codigo_fuente +" " #nose porque, pero sin esto se rompe 
    tokens = [] #es la lista donde estara el token devuelto por el lexer 
    posicion_actual = 0 #inicializa la posicion actual 
    
    while posicion_actual < len(codigo_fuente): #es un ciclo que hara una secuencia mientras la posicion actual sea menor a la long de la cadena de entrada
        
        #es un ciclo que pregunta si la posicion donde apunta, es una espacio vacio, aumenta en 1 la posicion actual para continuar con la cadena
        while codigo_fuente[posicion_actual].isspace(): 
            posicion_actual = posicion_actual + 1 
        
        #declara a comienzo_lexema igual a la posicion_actual   
        comienzo_lexema = posicion_actual 
        
        #inicializa variables 
        posibles_tokens = [] 
        posibles_tokens_con_un_caracter_mas = [] 
        lexema = "" 
        var_aux_todos_en_estado_trampa = False 
        
        #
        while not var_aux_todos_en_estado_trampa and posicion_actual < len (codigo_fuente)+1: 
            var_aux_todos_en_estado_trampa = True 
            lexema = codigo_fuente[comienzo_lexema:posicion_actual+1] 
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []
            
            
            # Revisa cada tupla de tokens en TOKENS_POSIBLES,
            # Realiza una simulacion del token,
                # Si ese token termina en estado final, lo añande a  posibles_tokens_con_un_caracter_mas y dice que no todos los token estan en estado trampa para seguir revisando los demas tokens 
                # Si ese token no termina en estado final, dice que no todos los token estan en estado trampa
            for (un_tipo_de_token, afd) in TOKENS_POSIBLES: 
                simulacion_afd = afd(lexema) 
                if simulacion_afd == ESTADO_FINAL: 
                    posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token) 
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    var_aux_todos_en_estado_trampa = False
            
            #aumenta la posicion actual en 1 
            posicion_actual = posicion_actual + 1
        
        if len(posibles_tokens) == 0:
            print("ERROR: TOKEN DESCONOCIDO - LEXER FALLO" + lexema)
        else:
            posicion_actual = posicion_actual - 1                                       #
            un_tipo_de_token = posibles_tokens[0]                                       #
            token= (un_tipo_de_token,codigo_fuente[comienzo_lexema:posicion_actual])    #
            tokens.append(token)                                                        #
        
    return tokens 


TOKENS_POSIBLES = [("SI", automata_si),
                   ("FINSI", automata_finsi),
                   ("OPSUM", automata_opsuma),
                   ("OPMULT", automata_opmult),
                   ("EQUAL", automata_equal),
                   ("LEER", automata_leer),
                   ("MOSTRAR", automata_mostrar),
                   ("REPETIR", automata_repetir),
                   ("HASTA", automata_hasta),
                   ("ENTONCES", automata_entonces),
                   ("MIENTRAS", automata_mientras),
                   ("FUNC", automata_func),
                   ("FINFUNC", automata_finfunc),
                   ("OPEREL", automata_oprel),
                   ("PUNTO-COMA",automataPuntoComa),
                   ("Parentensis Cerrado",automataParenClose),
                   ("Parentensis Abierto",automataParenOpen),
                   ("NUM",automata_num),
                    ("ID", automata_id)]
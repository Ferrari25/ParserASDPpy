ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"


#------- AUTOMATA ID
def automata_id(lexema):
    estadoactual=0
    estadosfinales=[1]
    for vcarac in lexema:
        if estadoactual == 0 and vcarac.isalpha():
            estadoactual = 1
        elif estadoactual == 0 and vcarac.isdigit():
            estadoactual = -1
        elif estadoactual == 1 and vcarac.isalpha() or vcarac.isdigit():
            estadoactual=1
        elif estadoactual == -1 and vcarac.isalpha() or vcarac.isdigit():
            estadoactual=-1
        else:
            estadoactual = -1
            break
    if estadoactual == -1:
        return  ESTADO_TRAMPA
    if estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

#------- AUTOMATA ENTONCES
def automata_entonces(lexema):
        estadoactual=0
        estadosfinales=[8]
        for vcarac in lexema:
            if estadoactual==0 and vcarac=='e':
                estadoactual= 1
            elif estadoactual==1 and vcarac=='n':
                estadoactual=2
            elif estadoactual==2 and vcarac=='t':
                estadoactual=3
            elif estadoactual==3 and vcarac=='o':
                estadoactual=4
            elif estadoactual==4 and vcarac=='n':
                estadoactual=5
            elif estadoactual==5 and vcarac=='c':
                estadoactual=6
            elif estadoactual==6 and vcarac=='e':
                estadoactual=7
            elif estadoactual==7 and vcarac=='s':
                estadoactual=8
            else:
                estadoactual=-1
                break
        if estadoactual == -1:
             return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL
            
#------- AUTOMATA MIENTRAS
def automata_mientras(lexema):
        estadoactual=0
        estadosfinales=[8]
        for vcarac in lexema:
            if estadoactual==0 and vcarac=='m':
                estadoactual= 1
            elif estadoactual==1 and vcarac=='i':
                estadoactual=2
            elif estadoactual==2 and vcarac=='e':
                estadoactual=3
            elif estadoactual==3 and vcarac=='n':
                estadoactual=4
            elif estadoactual==4 and vcarac=='t':
                estadoactual=5
            elif estadoactual==5 and vcarac=='r':
                estadoactual=6
            elif estadoactual==6 and vcarac=='a':
                estadoactual=7
            elif estadoactual==7 and vcarac=='s':
                estadoactual=8
            else:
                estadoactual=-1
                break
        if estadoactual == -1:
             return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL            
        
#------- AUTOMATA FINSI
def automata_finsi(lexema):
        estadoactual=0
        estadosfinales=[5]
        for vcarac in lexema:
            if estadoactual==0 and vcarac=='f':
                estadoactual=1
            elif estadoactual==1 and vcarac=='i':
                estadoactual=2
            elif estadoactual==2 and vcarac=='n':
                estadoactual=3
            elif estadoactual==3 and vcarac=='s':
                estadoactual=4
            elif estadoactual==4 and vcarac=='i':
                estadoactual=5
            else:
                estadoactual=-1
                break
        if estadoactual == -1:
             return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
            return ESTADO_FINAL  
        else:
            return ESTADO_NO_FINAL

#------- AUTOMATA HASTA
def automata_hasta(lexema):
    estadoactual = 0
    estadosfinales = [5]
    for vcarac in lexema:
        if estadoactual == 0 and vcarac == 'h':
           estadoactual = 1
        elif estadoactual == 1 and vcarac == 'a':
           estadoactual = 2
        elif estadoactual == 2 and vcarac == 's':
           estadoactual = 3
        elif estadoactual == 3 and vcarac == 't':
           estadoactual = 4
        elif estadoactual == 4 and vcarac == 'a' :
           estadoactual = 5
        else:
           estadoactual = -1
           break
    if estadoactual==-1:
       return ESTADO_TRAMPA
    if estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

#------- AUTOMATA LEER
def automata_leer(lexema):
    estadoactual = 0
    estadosfinales = [4]
    for vcarac in lexema:
        if estadoactual == 0 and vcarac == 'l':
           estadoactual = 1
        elif estadoactual == 1 and vcarac == 'e':
           estadoactual = 2 
        elif estadoactual == 2 and vcarac == 'e':
           estadoactual = 3 
        elif estadoactual == 3 and vcarac == 'r':
           estadoactual = 4 
        else:
           estadoactual = -1
           break 
    if estadoactual == -1:
       return ESTADO_TRAMPA 
    if estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL 

#------- AUTOMATA SINO
def automata_sino(lexema):
    estadoactual = 0
    estadosfinales = [4]
    for vcarac in lexema:
        if estadoactual == 0 and vcarac == 's':
           estadoactual = 1
        elif estadoactual == 1 and vcarac == 'i':
           estadoactual = 2 
        elif estadoactual == 2 and vcarac == 'n':
           estadoactual = 3 
        elif estadoactual == 3 and vcarac == 'o':
           estadoactual = 4 
        else:
           estadoactual = -1
           break 
    if estadoactual == -1:
       return ESTADO_TRAMPA 
    if estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

#------- AUTOMATA FUNC
def automata_func(lexema):
    estadoactual = 0
    estadosfinales = [4]
    for vcarac in lexema:
        if estadoactual == 0 and vcarac == 'f':
           estadoactual = 1
        elif estadoactual == 1 and vcarac == 'u':
           estadoactual = 2 
        elif estadoactual == 2 and vcarac == 'n':
           estadoactual = 3 
        elif estadoactual == 3 and vcarac == 'c':
           estadoactual = 4 
        else:
           estadoactual = -1
           break 
    if estadoactual == -1:
       return ESTADO_TRAMPA 
    if estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

#------- AUTOMATA EQUAL
def automata_equal(lexema):
    estadoactual = 0
    estadosfinales = [5]
    for vcarac in lexema:
        if estadoactual == 0 and vcarac == 'e':
           estadoactual = 1
        elif estadoactual == 1 and vcarac == 'q':
           estadoactual = 2 
        elif estadoactual == 2 and vcarac == 'u':
           estadoactual = 3 
        elif estadoactual == 3 and vcarac == 'a':
           estadoactual = 4 
        elif estadoactual == 4 and vcarac == 'l':
           estadoactual = 5 
        else:
           estadoactual = -1
           break 
    if estadoactual == -1:
       return ESTADO_TRAMPA 
    if estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

#------- AUTOMATA OPE-REL
def automata_oprel(lexema):
        estadoactual=0
        estadosfinales=[1]
        for vcarac in lexema:
            if estadoactual==0 and (vcarac=='<' or vcarac=='>' or vcarac=='='):
                estadoactual=1
            else:
                estadoactual=-1
                break
        if estadoactual==-1:
            return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
             return ESTADO_FINAL
        else:
             return ESTADO_NO_FINAL

#------- AUTOMATA OP-SUMA
def automata_opsuma(lexema):
        estadoactual=0
        estadosfinales=[1]
        for vcarac in lexema:
            if estadoactual==0 and (vcarac=='+' or vcarac=='-'):
                estadoactual=1
            else:
                estadoactual=-1
                break
        if estadoactual==-1:
            return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
             return ESTADO_FINAL
        else:
             return ESTADO_NO_FINAL
        
#------- AUTOMATA OP-MULT
def automata_opmult(lexema):
        estadoactual=0
        estadosfinales=[1]
        for vcarac in lexema:
            if estadoactual==0 and (vcarac=='*' or vcarac=='/'):
                estadoactual=1
            else:
                estadoactual=-1
                break
        if estadoactual==-1:
            return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
             return ESTADO_FINAL
        else:
             return ESTADO_NO_FINAL

#------- AUTOMATA REPETIR
def automata_repetir(lexema):
        estadoactual=0
        estadosfinales=[7]
        for vcarac in lexema:
            if estadoactual==0 and vcarac=='r':
                estadoactual= 1
            elif estadoactual==1 and vcarac=='e':
                estadoactual=2
            elif estadoactual==2 and vcarac=='p':
                estadoactual=3
            elif estadoactual==3 and vcarac=='e':
                estadoactual=4
            elif estadoactual==4 and vcarac=='t':
                estadoactual=5
            elif estadoactual==5 and vcarac=='i':
                estadoactual=6
            elif estadoactual==6 and vcarac=='r':
                estadoactual=7
            else:
                estadoactual=-1
                break
        if estadoactual == -1:
             return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
            return ESTADO_FINAL  
        else:
            return ESTADO_NO_FINAL

#------- AUTOMATA SI
def automata_si(lexema):
    estadoactual = 0
    estadosfinales = [2]
    for vcarac in lexema:
        if estadoactual == 0 and vcarac == 's':
           estadoactual = 1
        elif estadoactual == 1 and vcarac == 'i':
           estadoactual = 2 
        else:
           estadoactual = -1
           break 
    if estadoactual == -1:
       return ESTADO_TRAMPA 
    if estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

#------- AUTOMATA FIN-FUNC
def automata_finfunc(lexema):
        estadoactual=0
        estadosfinales=[7]
        for vcarac in lexema:
            if estadoactual==0 and vcarac=='f':
                estadoactual= 1
            elif estadoactual==1 and vcarac=='i':
                estadoactual=2
            elif estadoactual==2 and vcarac=='n':
                estadoactual=3
            elif estadoactual==3 and vcarac=='f':
                estadoactual=4
            elif estadoactual==4 and vcarac=='u':
                estadoactual=5
            elif estadoactual==5 and vcarac=='n':
                estadoactual=6
            elif estadoactual==6 and vcarac=='c':
                estadoactual=7
            else:
                estadoactual=-1
                break
        if estadoactual == -1:
             return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
            return ESTADO_FINAL  
        else:
            return ESTADO_NO_FINAL

#------- AUTOMATA PUNTO-COMA
def automata_puntoComa(lexema):
        estadoactual=0
        estadosfinales=[1]
        for vcarac in lexema:
            if estadoactual==0 and vcarac==';':
                estadoactual=1
            else:
                estadoactual=-1
                break
        if estadoactual==-1:
            return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
             return ESTADO_FINAL
        else:
             return ESTADO_NO_FINAL
        
#------- AUTOMATA MOSTRAR
def automata_mostrar(lexema):
        estadoactual=0
        estadosfinales=[7]
        for vcarac in lexema:
            if estadoactual==0 and vcarac=='m':
                estadoactual= 1
            elif estadoactual==1 and vcarac=='o':
                estadoactual=2
            elif estadoactual==2 and vcarac=='s':
                estadoactual=3
            elif estadoactual==3 and vcarac=='t':
                estadoactual=4
            elif estadoactual==4 and vcarac=='r':
                estadoactual=5
            elif estadoactual==5 and vcarac=='a':
                estadoactual=6
            elif estadoactual==6 and vcarac=='r':
                estadoactual=7
            else:
                estadoactual=-1
                break
        if estadoactual == -1:
             return ESTADO_TRAMPA + "automata"
        if estadoactual in estadosfinales:
            return ESTADO_FINAL  
        else:
            return ESTADO_NO_FINAL

#------- AUTOMATA NUM
def automata_num(lexema):
        estadoactual=0
        estadosfinales=[1]
        for vcarac in lexema:
            if estadoactual==0 and vcarac.isdigit():
                estadoactual=1
            elif estadoactual==1 and vcarac.isdigit():
                estadoactual=1
            else:
                estadoactual=-1
                break
        if estadoactual==-1:
            return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
             return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

#------- AUTOMATA PUNTO-COMA
def automataPuntoComa(lexema):
        estadoactual=0
        estadosfinales=[1]
        for vcarac in lexema:
            if estadoactual==0 and vcarac==';':
                estadoactual=1
            else:
                estadoactual=-1
                break
        if estadoactual==-1:
            return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
             return ESTADO_FINAL
        else:
             ESTADO_NO_FINAL
             
#------- AUTOMATA PUNTO-COMA
def automataParenOpen(lexema):
    estadoactual = 0
    estadosfinales = [1]
    
    for vcarac in lexema:
        if estadoactual == 0 and vcarac == '(':
            estadoactual = 1
        else:
            estadoactual = -1
            break
    
    if estadoactual == -1:
        return ESTADO_TRAMPA
    elif estadoactual in estadosfinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

#------- AUTOMATA PUNTO-COMA
def automataParenClose(lexema):
        estadoactual=0
        estadosfinales=[1]
        for vcarac in lexema:
            if estadoactual==0 and vcarac==')':
                estadoactual=1
            else:
                estadoactual=-1
                break
        if estadoactual==-1:
            return ESTADO_TRAMPA
        if estadoactual in estadosfinales:
             return ESTADO_FINAL
        else:
             ESTADO_NO_FINAL


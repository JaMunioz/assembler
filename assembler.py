MOV = {
"A,B":     "0000000", "B,A":     "0000001", "A,Lit":   "0000010",
"B,Lit":   "0000011", "A,(Dir)": "0100101", "B,(Dir)": "0100110",
"(Dir),A": "0100111", "(Dir),B": "0101000", "A,(B)":   "0101001",
"B,(B)":   "0101010", "(B),A":   "0101011"}
ADD = {  
"A,B":     "0000100", "B,A":     "0000101", "A,Lit":   "0000110",
"B,Lit":   "0000111", "A,(Dir)": "0101100", "B,(Dir)": "0101101",
"A,(B)":   "0101110", "(Dir)":   "0101111"}
SUB = { 
"A,B":     "0001000", "B,A":     "0001001", "A,Lit":   "0001010",
"B,Lit":   "0001011", "A,(Dir)": "0110000", "B,(Dir)": "0110001",
"A,(B)":   "0110010", "(Dir)":   "0110011"}
AND = {
"A,B":     "0001100", "B,A":     "0001101", "A,Lit":   "0001110",
"B,Lit":   "0001111", "A,(Dir)": "0110100", "B,(Dir)": "0110101",
"A,(B)":   "0110110", "(Dir)":   "0110111"}
OR = { 
"A,B":     "0010000", "B,A":     "0010001", "A,Lit":   "0010010",
"B,Lit":   "0010011", "A,(Dir)": "0111000", "B,(Dir)": "0111001",
"A,(B)":   "0111010", "(Dir)":   "0111011"}
NOT = {  
"A,A":     "0010100", "A,B":     "0010101", "B,A":     "0010110",
"B,B":     "0010111", "(Dir),A": "0111100", "(Dir),B": "0111101",
"(B)":     "0111110"}
XOR = { 
"A,B":     "0011000", "B,A":     "0011001", "A,Lit":   "0011010",
"B,Lit":   "0011011", "A,(Dir)": "0111111", "B,(Dir)": "1000000",
"A,(B)":   "1000001", "(Dir)":   "1000010"}
SHL = { 
"A,A":     "0011100", "A,B":     "0011101", "B,A":     "0011110",
"B,B":     "0011111", "(Dir),A": "1000011", "(Dir),B": "1000100", 
"(B)":     "1000101"}
SHR = { 
"A,A":     "0100000", "A,B":     "0100001", "B,A":     "0100010",
"B,B":     "0100011", "(Dir),A": "1000110", "(Dir),B": "1000111", 
"(B)":     "1001000" }
INC = { 
"B":       "0100100", "(Dir)":   "1001001", "(B)":     "1001010"}
RST = { 
"(Dir)":   "1001011", "(B)":     "1001100"}
CMP = { 
"A,B":     "1001101", "A,Lit":   "1001110", "B,Lit":   "1001111",
"A,(Dir)": "1010000", "B,(Dir)": "1010001", "A,(B)":   "1010010"}
JMP = {
"Dir":     "1010011"}
JEQ = {
"Dir":     "1010100"}
JNE = {
"Dir":     "1010101"}
JGT = {
"Dir":     "1010110"}
JLT = {
"Dir":     "1010111"}
JGE = {
"Dir":     "1011000"}
JLE = {
"Dir":     "1011001"}
JCR = {
"Dir":     "1011010"}
JOV = {
"Dir":     "1011011"}
CALL = {
"Dir":     "1011100"}
RET = {
"":        "1011101"}
PUSH = {
"A":       "1011111", "B":       "1100000"}
POP = {
"A":       "1100001", "B":       "1100010"}
opCodes = {
'MOV':0,'ADD':1,'SUB':2,'AND':3,'OR':4,'NOT':5,'XOR':6,'SHL':7,'SHR':8,'INC':9,
'RST':10,'CMP':11,'JMP':12,'JEQ':13,'JNE':14,'JGT':15,'JLT':16,'JGE':17,
'JLE':18,'JCR':19,'JOV':20,'CALL':21,'RET':22,'PUSH':23,'POP':24}
labels = {}
code_jumps = {}
variables = {}
instructions = []
lines_data = -2
lines_code = 0
check = 1
error = False
jumps = []
pos_jumps = []
error_lines = []
cond = 0
error_type = []

f = open("p3F_1.ass","r") #Lectura del .ass  #p3F_1   p3F_2i 
lines = f.readlines()

for i in range(len(lines)): #Limpiador de \n
    if check == 0:
        lines_data += 1
    else:
        lines_code += 1
    lines[i] = lines[i][:-1]
    if lines[i][-1] != ":": #Quitar espacios innecesarios
        if lines[i][0] == " ":
            lines[i] = lines[i][2:]
        lines[i] = lines[i].split(" ")
        if len(lines[i]) == 1:
            lines[i].append(0)
        if len(lines[i]) != 2:
            print(lines[i])
            error = True
            error_lines.append(i) #si falta la existencia de un valor
            error_type.append("Debe ir la instancia, junto al operador (ej: MOV A,B A es invalido, mientras que MOV A,B no lo es.)")
        else: 
            if lines[i][0] in opCodes: #checking the command.
                n = opCodes[lines[i][0]] #checking jumps.
                instructions.append([lines[i][0],lines[i][1]])
                if (n == 12 or n == 13 or n == 14 or n == 15 or n == 16 or
                    n == 17 or n == 18 or n == 19 or n == 20):
                    k = lines[i][1]
                    jumps.append(lines[i][1]+":")
                    pos_jumps.append(i)
                    try:
                        if k[0] == "#": #hexagesimal
                            H = 1
                            if int(k[1:],16) > 255:
                                error = True
                                error_lines.append(i)
                                error_type.append("El valor entregado en hexagesimal es mayor a 255 en decimal")
                                #Out of range in bits.

                        else: #decimal
                            int(k)
                            if int(k) > 255:
                                error = True
                                error_lines.append(i)
                                error_type.append("El numero en decimal no puede ser mayor a 255.")
                                #Out of range in bits.
                    except:
                        error = True
                        error_lines.append(i) #Valor acompañado del jump no existente.
                        error_type.append("Se debe ingresar un valor decimal o hexagesimal, perteneciente al intervalo de [0,255]")
                else:
                    #para el caso de los opcodes solo quedara lo de la derecha.
                    v1 = False
                    v2 = False
                    x = lines[i][1].replace("(","").replace(")","").split(",") 
                    y = ""
                    if lines[i][1][0] == "(":
                        v1 = True
                    if lines[i][1][-1] == ")":
                        v2 = True
                    p = 0
                    H = 0 
                    for k in x:
                        if p == 1:
                            y += ","
                        if k not in variables and k != "A" and k != "B":
                            try:
                                if k[0] == "#": #hexagesimal
                                    H = 1
                                    if int(k[1:],16) > 255:
                                        error = True
                                        error_lines.append(i)
                                        ("El valor entregado en hexagesimal supera el es mayor a 255 en decimal")
                                        #Out of range in bits.

                                else: #decimal
                                    int(k)
                                    if int(k) > 255:
                                        error = True
                                        error_lines.append(i)
                                        error_type.append("El numero en decimal no puede ser mayor a 255.")
                                        #Out of range in bits.

                                    if v1 == True and p==0:
                                        y += "(Dir)"
                                        v1 = False
                                    elif v2 == True and p==1:
                                        y += "(Dir)"
                                    else:
                                        y += "Lit"
                            except:
                                error = True
                                error_lines.append(i) #Variable no existente.
                                error_type.append("Se esta intentando utilizar una variable no existente.")
                        else:
                            if k == "A" or k == "B":
                                if v1 == True and p == 0:
                                    y += "("+str(k)+")"
                                elif v2 == True and p == 1:
                                    y += "("+str(k)+")"
                                else:
                                    y += str(k)
                            else:
                                if v1 == True and p == 0:
                                    y += "(Dir)"
                                elif v2 == True and p == 1:
                                    y += "(Dir)"
                                else:
                                    y += "Lit"
                        p += 1
                    x = 0
                    exec("if "+'"'+str(y)+'"'+" in "+str(lines[i][0])+":\n    x = 1")
                    if x == 0 and H == 0:
                        error = True
                        error_lines.append(i) #Existe la instrucion, pero no su llave.
                        error_type.append("Existe la instacia, pero no su operador. (ej: MOV A,A,A existiendo MOV, pero no el A,A,A).")
            else:
                if check == 1: #Se esta analizando codigo despues de 'CODE:'
                    error = True
                    error_lines.append(i) #Opcode inexistente.
                    error_type.append("No existe la instacia: "+str(lines[i][0])+".")
                else: #variables
                    variables[lines[i][0]] = i 
                    try:
                        int(lines[i][1])
                    except:
                        if lines[i][1][0] == "#": 
                            for k in range(1,len(lines[i][1])):
                                if lines[i][1][k] == "#":
                                    error = True
                                    #añade si esta mal escrito el hexagecimal.
                                    error_lines.append(i)
                        else:
                            error = True
                            #simplemente hay un simbolo extraño.
                            error_lines.append(i)

    else: 
        if i != 0 and cond == 0: #identificar posicion del "CODE".
            check = 1
            cond = 1
            index_code = i
            d = -index_code-1 #delay
        elif check != 0:
            #Se agregan llaves al diccionario, como clave la posicion.
                labels[lines[i]] = i 
                code_jumps[lines[i]] = i+d
                d -= 1
        word = lines[i][:]
        lines[i] = lines[i].split(" ")
        if len(lines[i]) != 1:
            error = True
            error_lines.append(i)
        lines[i] = word #Volviendo a formato de string.

if lines[0] == "DATA:":
    check += 1

#if check != 2:
    #error = True

"""
#revisar los jumps.
for i in range(len(jumps)):  #Existe pos para indicar la linea con error.
    if jumps[i] not in labels:
        error = True
        error_lines.append(pos_jumps[i])
"""

if error == True:
    error_lines.sort()
    print("\nEl documento '.ass' no esta bien formulado, a continuacion se "
    "mostraran las lineas las cuales estan con errores tipo 'syntax', "
    "indicandose el numero de linea y su respectivo contenido: ")
    for i in range(len(error_lines)):
        x = ""
        for k in range(len(lines[error_lines[i]])):
            x += str(lines[error_lines[i]][k])+" "
        print(str(error_lines[i]+1)+": "+x,error_type[i])
else:
    ### MEM mem MEM mem MEM mem MEM mem MEM mem MEM mem MEM mem MEM mem MEM ###
    new_file=open("newfile.mem",mode="w",encoding="utf-8")
    ks = list(variables.keys())
    for k in ks:
        try: #Si es decimal en DATA:
            x = int(lines[variables[k]][1])
            x = (str(bin(x)))[2:]
        except: #Si es hexagesimal en DATA:
            x = int(lines[variables[k]][1][1:],16)
            x = (str(bin(x)))[2:]
        while len(x) < 8:
            x = "0" + x
        new_file.write(x+"\n")
    new_file.close()

    #OUT out OUT out OUT out OUT out OUT out OUT out OUT out OUT out OUT out###
    a = [] #inst
    b = [] #oper
    c = [] #lit
    for i in range(len(instructions)):
        a.append(instructions[i][0])
        x = instructions[i][1].split(",")
        if (a[i] == "JMP" or a[i] == "JEQ" or a[i] == "JNE" or a[i] == "JGT" or 
        a[i] == "JLT" or a[i] == "JGE" or a[i] == "JLE" or a[i] == "JCR"
        or a[i] == "JOV"):
            y = x[0].replace("(","").replace(")","")
            lit = ""
            try: #si es un decimal en los jumps:
                int(y)
                lit = (str(bin(int(y))))[2:]
            except:
                if y[0] == "#": #si es hexagesimal en los jumps:
                    y = int(y[1:],16)
                    lit = (str(bin(int(y))))[2:]
                else: #posicion de los labels para los jumps:
                    lit = code_jumps[y+":"] 
                    lit = (str(bin(lit)))[2:]
            while len(lit) < 8:
                lit = "0" + lit
            c.append(lit)
            x[0] = "Dir"
        else:
            y = ""
            if x[0] == "A" or x[0] == "B" or x[0] == "(A)" or x[0] == "(B)": 
                ...
            else:
                y = x[0][:]
                if x[0][0] == "(":
                    x[0] = "(Dir)"
                else:
                    x[0] = "Lit"
            if len(x) == 2:
                if x[1] == "A" or x[1] == "B" or x[1] == "(A)" or x[1] =="(B)":
                    ...
                else:
                    y = x[1][:]
                    if x[1][0] == "(":
                        x[1] = "(Dir)"
                    else:
                        x[1] = "Lit"
            if y != "":
                y = y.replace("(","").replace(")","")
                try:
                    if y[0] == "#": #si es hexagesimal en CODE:
                        y = int(y[1:],16)
                        lit = (str(bin(int(y))))[2:]
                        while len(lit) < 8:
                            lit = "0" + lit
                        c.append(lit)
                    else: #si es decimal en CODE:
                        int(y)
                        lit = (str(bin(int(y))))[2:]
                        while len(lit) < 8:
                            lit = "0" + lit
                        c.append(lit)
                except:
                    lit = (str(bin(int(variables[y])-1)))[2:]
                    while len(lit) < 8:
                        lit = "0" + lit
                    c.append(lit)
            else:
                c.append("00000000") ##seguir aqui
        
        y = ""
        for k in x:
            y += k+","
        y = y[:-1]
        b.append(y)
    
    new_file=open("newfile.out",mode="w",encoding="utf-8")
    for i in range(len(a)):
        exec("x = "+str(a[i])+"["+'"'+str(b[i])+'"'+"]")
        new_file.write(x+c[i]+"\n")
    new_file.close()
    print("La cantidad de lineas de 'DATA' son: "+str(0))
    print("La cantidad de lineas de 'CODE' son: "+str(lines_code))
    print("Se han generado 'newfile.out' y 'newfile.mem'.\n")
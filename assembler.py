opCodes = {'MOV':0,'ADD':1,'SUB':2,'AND':3,'OR':4,'NOT':5,'XOR':6,'SHL':7,
'SHR':8,'INC':9,'RST':10,'CMP':11,'JMP':12,'JEQ':13,'JNE':14,'JGT':15,'JLE':16,
'JCR':17,'JOV':18}
labels = {}
check = 0
error = False

#p3F_1   p3F_2i 
f = open("p3F_1.ass","r") #Lectura del .ass 
lines = f.readlines()

for i in range(len(lines)): #Limpiador de \n
    lines[i] = lines[i][:-1]
    if lines[i][-1] != ":": #Quitar espacios innecesarios
        if lines[i][0] == " ":
            lines[i] = lines[i][2:]
        lines[i] = lines[i].split(" ")
        if len(lines[i]) != 2:
            error = True
            #print(lines[i])
            #print("error")
    else: 
        if lines[i] == "CODE:": #identificar posicion del "CODE"
            check += 1
            index_code = i
        elif check != 0:
                labels[lines[i]] = i #Se agregar llaves al diccionario, como clave la posicion.
        word = lines[i][:]
        lines[i] = lines[i].split(" ")
        if len(lines[i]) != 1:
            error = True
            #print("error")
            #print(lines[i])
        lines[i] = word #Volviendo a formato de string
if lines[0] == "DATA:":
    check += 1

if check != 2:
    error = True

#revisar los jumps.
#revisar las posibles instrucciones que se pueden recibir.
#revisar que los parametros de la derecha de cada lista doble, tenga sentido.

if error == True:
    print("El documento '.ass' no esta bien formulado.\n")
else:
    print("Ejecutando lectura.\n")
    print(lines)
"""
print(index_code)
print(check)
print(labels)
print(int("A0", 16)) #Conversor a decimal, de hexagecimal
"""
opCodes = {'MOV':0,'ADD':1,'SUB':2,'AND':3,'OR':4,'NOT':5,'XOR':6,'SHL':7,
'SHR':8,'INC':9,'RST':10,'CMP':11,'JMP':12,'JEQ':13,'JNE':14,'JGT':15,'JLT':16,
'JGE':17,'JLE':18,'JCR':19,'JOV':20}
labels = {}
check = 0
error = False
jumps = []
pos_jumps = []

#p3F_1   p3F_2i 
f = open("p3F_2i.ass","r") #Lectura del .ass 
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
            if lines[i][0] in opCodes: #checking the command.
                n = opCodes[lines[i][0]] #checking jumps.
                if n == 12 or n == 13 or n == 14 or n == 15 or n == 16 or n == 17 or n == 18 or n == 19 or n == 20:
                    jumps.append(lines[i][1]+":")
                    pos_jumps.append(i)
            else:
                if check == 1: #Se esta analizando codigo despues de 'CODE:'
                    print(lines[i])
                    error = True
                    #print("error")
                    #print(lines[i])
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

print(labels)
print(jumps)
for i in jumps:
    if i not in labels:
        error = True
        print("error")

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
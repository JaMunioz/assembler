lista_desordenada = [3,2,1]
lista_ordenada = []
i = 0
while len(lista_desordenada) > 0:
    if i == 0:
        v = lista_desordenada[0]
        p = i
    if v > lista_desordenada[i]:
        v = lista_desordenada[i]
        p = i
    if i+1 == len(lista_desordenada):
        lista_ordenada.append(v)
        lista_desordenada.pop(p)
        i = 0
    else:
        i += 1
print(lista_ordenada)
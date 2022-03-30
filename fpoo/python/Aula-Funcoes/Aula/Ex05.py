def dobra(lista):
    pos = 0
    while pos<len(lista):
        lista[pos] *= 2
        pos += 1
contador = [1,5,7,9,2,5,6,7]
dobra(contador)
print(contador)

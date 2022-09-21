numeros = list()
for c in range(0, 5):
    aux = int(input('Digite um número: '))
    if c == 0 or aux > numeros[-1]:
        numeros.append(aux)
        print(f'O valor {aux} foi adicionado na última posição')
    else:
        p = 0
        while p < len(numeros):
            if aux <= numeros[p]:
                numeros.insert(p, aux)
                print(f'O valor {aux} foi adicionado na posição {p}')
                break
            p += 1

print(f'Valores digitados: {numeros}')
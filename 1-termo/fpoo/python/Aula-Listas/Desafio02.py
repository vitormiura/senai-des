numeros = list()
while True:
    aux = int(input('Digite um número:(-1 para sair) '))
    if aux == -1:
        break
    if aux not in numeros:
        numeros.append(aux)
    else:
        print('Número duplicado. Não irei adicionar')
numeros.sort()
print(f'Valores digitados: {numeros}')
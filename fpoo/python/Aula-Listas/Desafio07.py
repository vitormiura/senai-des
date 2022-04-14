aux = []
pessoas = []
maior = menor = 0

while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]

        if aux[1] < menor:
            menor = aux[1]

    pessoas.append(aux[:])
    aux.clear()

    op = str(input('Continuar? [S/N]')).strip().upper()
    if op == 'N':
        break

print(f'''Quantidade: {len(pessoas)}
Maior Peso {maior}
Menor Peso: {menor}''')
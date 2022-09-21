valor = [[], []]
for i in range(1, 8):
    aux = int(input(f'Digite o {i}º Número: '))
    if aux % 2 == 0:
        valor[0].append(aux)
    else:
        valor[1].append(aux)
valor[0].sort()
valor[1].sort()
print(f'''Pares {valor[0]}
Impares {valor[1]}''')
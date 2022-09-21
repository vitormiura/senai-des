pessoas = []
while True:
    pessoa = []
    countage = 0
    countman = 0
    countwomenage = 0

    pessoa.append((input('Digite o nome:')))
    pessoa.append(int(input('Digite a idade:')))
    pessoa.append((input('Digite o sexo:(F/M)')).upper())
    pessoas.append(pessoa)
    loop = input('deseja cadastrar mais um?(S/N)')

    if loop.upper() == 'N':
        for i in pessoas:
            if i[1] > 18:
                countage +=1
            if i[2] == 'M':
                countman += 1
            else:
                if i[1] < 20 and i[2] == 'F':
                    countwomenage =+1
        print(pessoas)
        print(f'o numero de pessoas maiores de 18 eh de {countage}')
        print(f'o numero de homens eh de {countman}')
        print(f'o numero de mulheres menor de 20 anos eh de  {countwomenage}')
        break
    else:
        continue

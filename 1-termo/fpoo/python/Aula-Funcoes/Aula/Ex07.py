from time import sleep

def contagem(i, f, p):
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='')
            cont += p
            sleep(1)
        print('')
    else:
        cont = i
        while cont > f:
            print(f'{cont}', end='')
            cont -= p
            sleep(1)
        print('')
contagem(1, 10, 1)
contagem(10, 0, 2)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)


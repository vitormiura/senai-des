from time import sleep

def contagem(i, f, p):
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' | ')
            c += p
            sleep(0.3)
        print('')
    else:
        c = i
        while c > f:
            print(f'{c}', end=' | ')
            c -= p
            sleep(0.3)
        print('')

contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(0, 100, 10)


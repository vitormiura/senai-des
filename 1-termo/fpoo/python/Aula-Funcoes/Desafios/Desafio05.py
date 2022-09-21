import random
from time import sleep

list = []

def sort():

    print('Sorteando: ', end='')
    for i in range(5):
        num = random.randint(1, 100)
        list.append(num)
        sleep(0.5)
        print(f'{num}', end=' ')
    
def somaPar(lista_valores):
    par = 0
    for valor in lista_valores:
        if valor % 2 == 0:
            par += valor

    print(f'\nLista: {lista_valores}')
    print(f'Soma dos pares = {par}')

sort()
somaPar(list)















# randomlist = []
# for i in range(0,5):
#     n = random.randint(1,30)
#     randomlist.append(n)
#     sleep(0.5)
#     print(randomlist)



    


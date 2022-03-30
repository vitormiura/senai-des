import random

jogador = dict()
jogo = list()
result = dict()

for i in range(1,5):
    n = random.randint(1,5)
    jogador['jogador{i}'] = print(f"O jogador {i} sorteou {n}")
jogo.append(jogo.copy())

for j in jogo:
        print(f'{j}')

print("-------------------------------")

for o in jogo:
    print(f'O {i} lugar: jogador{i} com {n}')
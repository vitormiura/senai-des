from time import sleep

dicionario = {}
dicionario['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
gols = []
total_gols = 0

for partida in range(1, partidas + 1):
    gol = int(input(f'Quantos gols ele fez na {partida}ª partida? '))
    gols.append(gol)
    total_gols += gol
dicionario['gols'] = gols
dicionario['total_gols'] = total_gols

print('*' * 40)
print(dicionario)
print('*' * 40)

for chave, valor in dicionario.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('*' * 40)
contador = 1

for elemento in gols:
    print(f'Na {contador}ª partida, ele fez {elemento} gols.')
    contador += 1
    sleep(1)
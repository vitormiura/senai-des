import pandas as pd

p = pd.read_excel(r'pessoas.xlsx')

qtd = p['Nome'].count()
print(qtd)

# id = input("Digite o id: ")
# pessoa = p['ID'] == id
# print(pessoa)

x = int(input('Digite o ID: '))
ind = 0
for i in p['ID']:
    ind += 1
    if x == i:
        print('Nome:', p['Nome'][ind])
        print('Idade:', p['Idade'][ind])
        print('Peso:', p['Peso'][ind])


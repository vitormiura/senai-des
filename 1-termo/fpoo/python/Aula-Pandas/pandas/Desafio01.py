import pandas as pd

p = pd.read_excel('pessoas.xlsx')
qtd = p['Nome'].count()

id = int(input('ID: '))
nome = input('Nome: ')
idade = int(input('Idade: '))
peso = int(input('Peso: '))

p.loc[qtd+1, 'ID'] = id
p.loc[qtd+1, 'Nome'] = nome
p.loc[qtd+1, 'Idade'] = idade
p.loc[qtd+1, 'Peso'] = peso

p.to_excel('pessoas.xlsx', index=False)
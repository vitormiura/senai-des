import pandas as pd
#from openpyxl import load_workbook 

f = pd.read_excel('pessoas.xlsx')

id = int(input("Digite o id: "))
n = str(input("Digite o nome: "))
i = int(input("Digite a idade: "))
p = float(input("Digite o peso: "))

df2 = pd.DataFrame({'ID': [id],
                    'Nome' : [n],
                    'Idade' : [i],
                    'Peso' : [p]})

aa = pd.concat([f, df2], ignore_index = True, axis = 0)
print(aa)
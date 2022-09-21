import pandas as pd

d = {
    'Nome': ['Ícaro', 'Nathã', 'Naiury'],
    'Idade': [19, 18, 18],
    'Altura': [1.77, 1.80, 1.70]}


d = pd.DataFrame(data = d)

#d.to_excel('xlsxCreate.xlsx', 'index=False') CONVERTE DATAFRAME PRA XLSX
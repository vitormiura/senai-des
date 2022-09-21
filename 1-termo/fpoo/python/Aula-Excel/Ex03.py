import pandas as pd

planilha = pd.read_excel('pessoas.xlsx')

linha = len(planilha)+1

for i in range(4):
    planilha.loc[linha, planilha.columns[i]] = input(f'{planilha.columns[i]}:')
# planilha.to_excel('pessoas.xlsx', index=False)
print(len(planilha.columns))

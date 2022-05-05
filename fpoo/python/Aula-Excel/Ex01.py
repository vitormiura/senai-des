import pandas as pd
data = {
    'País': ['Brasil', 'Colombia', 'Índia'],
    'Capital':['Brasília', 'Bogotá', 'Nova Delhi']
}
df = pd.DataFrame(data, columns=['País','Capital'])
df['População'] = 2000000
df.to_excel('teste.xlsx', index=False)
print(df)

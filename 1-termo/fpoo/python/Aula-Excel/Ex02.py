import pandas as pd
data = {
    'País': ['Brasil', 'Colombia', 'Índia'],
    'Capital':['Brasília', 'Bogotá', 'Nova Delhi']
}
df = pd.DataFrame(data, columns=['País','Capital'])
df['População']=0
df = pd.DataFrame(data, columns=['País','Capital','População'])
qde = df['País'].count()
for i in range(qde):
    df['População'][i]=int(input(f'População de {df["País"][i]}:'))
df.to_excel('testehahaha.xlsx', index=False)

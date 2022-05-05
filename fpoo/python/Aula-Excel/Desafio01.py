from asyncore import write
from tkinter import N
import pandas as pd

file = pd.read_excel('teste.xlsx')
d = pd.DataFrame(data = file)

print(d)
 
k = str(input("Digite o pais: "))
n = input("Digite o tamanho da população: ")
d['População'][1] = n
cont = 0
for i in d['País'][0]:
    cont+=1
    if(i == k):
        d['População'][1] = n
    
    
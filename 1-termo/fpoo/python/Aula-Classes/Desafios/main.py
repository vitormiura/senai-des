from moeda import *

val = float(input("Valor R$: "))
tx = float(input("Taxa: "))


aum = aumentar(val,tx)
dim = diminuir(val,tx)
metade = metade(val)
dobro = dobro(val)
print(f"Valor aumentado em  \33[31m{str(tx).replace('.0','')}%\33[m: R${aum} ")
print(f"Valor diminuido em  \33[32m{str(tx).replace('.0','')}%\33[m: R${dim} ")
print(f"Dobro: {moeda(dobro,'R$')} ")
print(f"Metade: {moeda(metade,'R$')}")
print("------------------------------------------------------")

resumo(val,dobro,metade,aum,dim)
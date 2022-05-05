
def moeda(preco,moeda):
    return (moeda + str(preco).replace(".0",",00"))


def aumentar(moeda,tx):
    moeda += (moeda * tx)/100
    return moeda


def diminuir(coin,tx):
    coin -= (coin * tx) / 100
    return coin

def dobro(moeda):
    return moeda * 2

def metade(moeda):
    return moeda / 2


def resumo(moeda,dobro,met,aum,red):
    print("                       Resumo                          ")
    print("------------------------------------------------------")
    principal = print(f"Valor principal:                      {str(moeda).replace('.0',',00')}")
    dobro = print(f"Dobro:                                {str(dobro).replace('.0',',00')}")
    metade = print(f"Metade:                                {str(met).replace('.0',',00')}")
    aumento = print(f"Aumento:                              {str(aum).replace('.0',',00')}")
    redux = print(f"Reduzido:                              {str(red).replace('.0',',00')}")
    print("------------------------------------------------------")










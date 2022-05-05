class Pessoa:
    def __init__(self,nome,idade,escrever=False,jogando=False):
        self.nome = nome
        self.idade = idade
        self.escrever = escrever
        self.falando = jogando
        print(nome)





    def falar(self):
        print("pessoa esta falando...")


    def escrevendo(self,livro):
        self.livro = livro
        if self.escrever:
            print(f'{self.nome} esta escrevendo {livro}')

            return
        self.escrever = True



    def jogador(self,jogo):
        if self.escrever:
            print(f"O {self.nome} não pode jogar")
            return

        print(f"O {self.nome} esta jogando {jogo}")
        self.jogando = True
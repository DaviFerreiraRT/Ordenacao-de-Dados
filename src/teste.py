class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Teste(self):
        print("Meu nome é "+ self.nome+", tenho" ,self.idade ,"anos")

p1 = Pessoa("Davi",20)
p1.Teste()

#Declaração Class
class Gafanhoto:
    def __init__(self): #Método Construtor
        #Atributos de Instância
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'Hammud'
g1.idade = 24
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Kakuxa'
g2.idade = 22
g2.aniversario()
print(g2.mensagem())
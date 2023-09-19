#Polimorfismo

class Pagamentos:
    def pagar(self):
        print("Pagamento realizado!")

#Classe dinheiro herdando os métodos da classe pagamentos
class Dinheiro(Pagamentos):
    def pagar(self):
        print("Pagamentos em dinheiro!")

#Classe cartão herdando os métodos da classe pagamentos
class Cartao(Pagamentos):
    def pagar(self):
        print("Pagamentos em cartao!")

#Classe pix herdando os métodos da classe pagamentos
class Pix(Pagamentos):
    def pagar(self):
        print("Pagamento com Pix!")

#Instanciando os objetos
obj1 = Dinheiro()
obj2 = Cartao()
obj3 = Pix()

#Chamando as funções
obj1.pagar()
obj2.pagar()
obj3.pagar()


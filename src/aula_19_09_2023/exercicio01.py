#Polimorfismo

class Pagamentos:
    def pagar(self):
        print("Pagamento realizado!")

class Dinheiro(Pagamentos):
    def pagar(self):
        print("Pagamentos em dinheiro!")

class Cartao(Pagamentos):
    def pagar(self):
        print("Pagamentos em cartao!")


obj1 = Pagamentos
obj1.pagar()
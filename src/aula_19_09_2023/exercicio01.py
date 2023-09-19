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
class Pix(Pagamentos):
    def pagar(self):
        print("Pagamento com Pix!")

obj1 = Pix()
obj1.pagar()


#Conceito de herança
#-------------------

class Pessoas:
    def __init__(self):
        self.nome = "Alberto Niriz"
        self.cpf = "4544546551684351"
        self.celular = "94965464365"
class Alunos:
    def __init__(self):
        self.ra = "545454545"
        Pessoas.__init__(self)

class Professores:  
    def __init__(self):
        self.func = "222222"
        Pessoas.__init__(self)

a1 = Alunos()
print(a1.ra)

p1 = Professores()
print(p1.nome)

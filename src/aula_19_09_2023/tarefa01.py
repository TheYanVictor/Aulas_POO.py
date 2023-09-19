#Tarefa de polimorfismo - WIP

#Classe primaria
class Locacao:
    def __init__(self):
        self.prazo = 0
        
    def locar(self, prazo):
        self.prazo = prazo
        
    def exibir(self):
        return(self.prazo)
    
#Classes polimorficas
class Localuno(Locacao):
    def locar(self):
        self.prazo = 10
        
class Locprof(Locacao):
    def locar(self):
        self.prazo = 20
        
aluno = Localuno()
aluno.locar()
print("Aluno - " , aluno.exibir())

professor = Locprof()
professor.locar()
print("Professor - ", professor.exibir())



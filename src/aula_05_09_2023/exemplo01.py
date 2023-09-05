# Classes, Atributos e Métodos
#-----------------------------

class Alunos:
    def __init__(self, ra, nome) :
        self.__ra = ra
        self.__nome = nome
        
    def exibe_dados(self):
        return f"RA: {self.__ra} - Aluno: {self.__nome}"
    
# Objetos - Instâncias 
a1 = Alunos (123456, "Tanaka")
print(a1.exibe_dados()) #os atributos da classe só são acessados pelos métodos da classe

        
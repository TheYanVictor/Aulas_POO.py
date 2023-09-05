#Encapsulamento
#--------------

class Alunos:
    def __init__(self):
        self.ra = ""
        self.nome = ""
    
    #Métodos para inserir dados nos atributos da classe    
    def set_ra(self, ra):
        self.__ra = ra
    
    def set_nome(self, nome):
        self.__nome = nome
    
    #Métodos para exibir dados dos atributos da classe
    def get_ra(self):
        return self.__ra
    def get_nome(self):
        return self.__nome
    
    #Métodos de exibir dados
    def exibir_dados(self):
        print("RA: " + self.__ra + " Aluno: " + self.__nome)
        
a1 = Alunos()
a1.set_ra("23151368")
a1.set_nome("Jose Alencar")
a1.exibir_dados()
    
    
    
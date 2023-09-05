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
    
    
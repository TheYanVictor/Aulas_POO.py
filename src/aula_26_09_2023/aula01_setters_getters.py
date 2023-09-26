#POO


class Pessoas:
    def __init__(self):
        self.__nome = " "
        self.__cpf = " "
        self.__rg = " " 
    
    #getter a setter
    def get_nome(self): 
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
   
    def set_cpf(self, cpf):
        self.__cpf = cpf
    
    def get_cpf(self):
        return self.__cpf
    
    def set_rg(self, rg):
        self.__rg = rg    

    def get_rg(self):
        return self.__rg

#objeto
p1 = Pessoas()
p1.set_nome("Maria")
p1.set_cpf("123685135136")
p1.set_rg("45555555")
print(p1.get_cpf())
print(p1.get_rg())
print(p1.get_nome())


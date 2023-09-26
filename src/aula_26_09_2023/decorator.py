##POO - Decorator @property

 

##26/09/2023

 

class Pessoas:
   def __init__(self):
      self.__nome = ""
      self.__cpf = ""
      self.__rg = ""
   @property
   def nome(self):
      return self.__nome
   @nome.setter
   def nome(self, nome):
      self.__nome = nome
   @property
   def cpf(self):
      return self.__cpf
   @cpf.setter
   def cpf(self, cpf):
      self.__cpf = cpf
   @property
   def rg(self):
      return self.__rg
   @rg.setter
   def rg(self, rg):
      self.__rg = rg

#Objeto
p1 = Pessoas()
p1.nome = "Maria"
p1.cpf = "115487984"
p1.rg = "21659876"
print(p1.nome)
print(p1.cpf)
print(p1.rg)

#Objeto2
p2 = Pessoas()
p2.nome = "Fulano"
p2.cpf = "11111111111"
p2.rg = "22222222222"
print(p2.nome)
print(p2.cpf)
print(p2.rg)
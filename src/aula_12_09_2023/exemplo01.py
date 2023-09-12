# Herança
# 12/09/2023

class Pessoas:
   def __init__(self):
      self.__nome = ""
      self.__cpf = ""
      
   # Métodos para inserir dados
   def set_nome(self, nome):
      self.__nome = nome
   
   def set_cpf(self, cpf):
      self.__cpf = cpf
      
   # Métodos para recuperar dados
   def get_nome(self):
      return self.__nome
   
   def get_cpf(self):
      return self.__cpf
      
   # Método para exibir dados
   def exibe_dados(self):
      print("Olá " + self.__nome + " seu CPF é " + self.__cpf)
      
class Alunos(Pessoas):
   def __init__(self):
      Pessoas.__init__(self)
      #super().__init__()
      self.__ra = ""
   
   def set_ra(self, ra):
      self.__ra = ra
   def set_curso(self, curso):
      self.__curso = curso
   
   def get_ra(self):
      return self.__ra
   def get_curso(self):
      return self.__curso
      

class Professores(Pessoas):
   def __init__(self):
      Pessoas.__init__(self)
      self.__funcional = ""
   
   def set_funcional(self, funcional):
      self.__funcional = funcional
   
   def get_funcional(self):
      return self.__funcional

#Separa linha 
print("---------------------------------------------------------------")
     
a1 = Alunos()
a1.set_nome("Augusto")
a1.set_cpf("33322211145")
a1.set_ra("2332455")
a1.set_curso("ADS")
a1.exibe_dados()
print("RA: " + a1.get_ra())
print("Curso: " + a1.get_curso())

#Separa linha 
print("---------------------------------------------------------------")

p1 = Professores()
#p1.set_ra("999999") Não é possível acessar métodos de outra classe, nesse caso, da classe Alunos
p1.set_nome("Fujitora")
p1.set_cpf("77788855574")
p1.set_funcional("6565656565")
p1.exibe_dados()
print("Professor: " + p1.get_nome())
print("CPF: " + p1.get_cpf())
print("Funcional: " + p1.get_funcional()) 

#Separa linha 
print("---------------------------------------------------------------")

a2 = Alunos()
a2.set_nome("Borsalino")
a2.set_cpf("6666666645")
a2.set_ra("783254658435")
a2.set_curso("SBM")
a2.exibe_dados()
print("RA: " + a2.get_ra())
print("Curso: " + a2.get_curso())

#Separa linha 
print("---------------------------------------------------------------")

p2 = Professores()
#p2.set_ra("999999") Não é possível acessar métodos de outra classe, nesse caso, da classe Alunos
p2.set_nome("Kizaru")
p2.set_cpf("87888888896")
p2.set_funcional("3653943216")
p2.exibe_dados()
print("Professor: " + p2.get_nome())
print("CPF: " + p2.get_cpf())
print("Funcional: " + p2.get_funcional()) 

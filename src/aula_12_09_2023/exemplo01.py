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
      
a1 = Alunos()
a1.set_nome("Fulno de Tal")
a1.set_cpf("888888888")
a1.set_ra("1234")
a1.set_curso("ADS")
a1.exibe_dados()
print("RA: " + a1.get_ra())
print("Curso: " + a1.get_curso())

p1 = Professores()
#p1.set_ra("999999") Não é possível acessar métodos de outra classe, nesse caso, da classe Alunos
p1.set_nome("professor Tanaka")
p1.set_cpf("444444444")
p1.set_funcional("22222")
p1.exibe_dados()
print("Professor: " + p1.get_nome())
print("CPF: " + p1.get_cpf())
print("Funcional: " + p1.get_funcional()) 

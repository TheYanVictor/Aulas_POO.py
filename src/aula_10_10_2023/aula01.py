# Classe abstrata e Interface
from abc import ABC, abstractmethod

class Media(ABC):
    notas = []
    
    @abstractmethod
    def calcula(self):
        pass
    
class MediaBemestre(Media):
    def __init__(self, notas):
        self.notas = notas 
    def calcula(self):
        calc = sum(self.notas)/len(self.notas)
        return (calc)
    

p1 = 7
p2 = 2
obj1 = MediaBemestre([p1,p2])
print(obj1.calcula())
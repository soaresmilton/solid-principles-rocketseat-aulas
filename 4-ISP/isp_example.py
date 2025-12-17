# pdf, txt, excel

from abc import ABC, abstractmethod

class Loadable(ABC):
  @abstractmethod
  def load(self): pass

class Viewable(ABC):
  @abstractmethod
  def view(self): pass

class Formatable(ABC):
  @abstractmethod
  def format(self): pass

class Calculable(ABC):
  @abstractmethod
  def calculate(self): pass


class PDF(Loadable, Viewable):
  def load(self):
    print("carregando PDF")
  
  def view(self):
    print("vendo PDF")

class TXT(Loadable, Formatable):
  def load(self):
    print("carregando TXT")

  def format(self):
    print("formatando TXT")
  
class Excel(Loadable, Calculable):
    def load(self):
      print("Carregando excel")
    
    def calculate(self):
      print("calculando excel")


doc1 = PDF()
doc2 = TXT()
doc3 = Excel()


doc1.load()
doc1.view()
doc2.load()
doc2.format()
doc3.load()
doc3.calculate()
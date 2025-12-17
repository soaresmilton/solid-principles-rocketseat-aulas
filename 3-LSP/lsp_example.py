class Animal:
  def comer(self):
    print("Animal está comendo")
  
  def andar(self):
    print("O Animal esta andando na jaula")


class Felino(Animal):
  def lamber(self):
    print("O felino está se limpando")

class Leao(Felino):
  def rugir(self):
    print("Leao rugindo")


class Pessoa:
  def observa(self, animal: Animal):
    animal.comer()

animal = Animal()
felino = Felino()
leao = Leao()


miltinho = Pessoa()
# Mesmo output para os três. Ou seja, aderente ao princípio de Liskov
miltinho.observa(animal)
miltinho.observa(felino)
miltinho.observa(leao)



  # Exemplo ruim
class BirdRuim:
  def fly(self) -> None:
    print("Flying")

class SparrowRuim(BirdRuim):
  pass

class OstrichRuim(BirdRuim):
  def fly(self) -> None:
    raise Exception("Ostriches can't fly")

def make_bird_fly(bird: BirdRuim) -> None:
  bird.fly()

sparrow = SparrowRuim()
ostrich = OstrichRuim()

make_bird_fly(sparrow)  # Funciona bem
make_bird_fly(ostrich)  # Levanta uma exceção

# Aplicando conceitos LSP:
from abc import ABC, abstractmethod

class Bird(ABC):
  @abstractmethod
  def move(self) -> None:
    pass

class FlyingBird(Bird):
  def move(self) -> None:
    print("Flying")

class NonFlyingBird(Bird):
  def move(self) -> None:
    print("Walking")

class Sparrow(FlyingBird):
  pass

class Ostrich(NonFlyingBird):
  pass

def make_bird_move(bird: Bird) -> None:
  bird.move()

sparrow = Sparrow()
ostrich = Ostrich()

make_bird_move(sparrow)  # Funciona bem
make_bird_move(ostrich)  # Funciona bem
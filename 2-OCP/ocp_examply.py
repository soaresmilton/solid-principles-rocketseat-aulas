from typing import Any
from abc import ABC, abstractmethod
# Exemplo ruim
class Company:
  def do_work(self, worker: int) -> None:
    if worker == 1:
      print("Programmer creating code")
    elif worker == 2:
      print("Seller selling the product")
    elif worker == 3:
      print("Human Resourcces hiring new devs")
    else:
      print("Error, no Worker!")


# Aplicando conceitos OCP:
class Worker(ABC):
  @abstractmethod
  def make(self):
    pass

class Programmer(Worker):
  def make(self):
    print("Programmer creating code")

class Seller(Worker):
  def make(self):
    print("Seller selling the product")

class HumanResources(Worker):
  def make(self):
    print("Human Resourcces hiring new devs")


class CompanyMelhorada:
  def do_work(self, worker: Any) -> None:
    worker.make()


programmer = Programmer()
seller = Seller()
hr = HumanResources()
company = CompanyMelhorada()
company.do_work(worker=programmer)
company.do_work(worker=seller)
company.do_work(worker=hr)

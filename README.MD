# Princípios SOLID

Os princípios SOLID são um conjunto de cinco diretrizes para o design de software orientado a objetos, que visam tornar os sistemas mais compreensíveis, flexíveis e fáceis de manter. Esses princípios foram popularizados por Robert C. Martin (também conhecido como Uncle Bob) e são amplamente adotados na engenharia de software.

1. **Single Responsibility Principle (SRP) - Princípio da Responsabilidade Única**  
   Cada classe deve ter apenas uma razão para mudar, ou seja, deve ter apenas uma responsabilidade. Isso ajuda a manter o código mais organizado e facilita a manutenção.

   ```python
      # Exemplo da aula:

      class Process:
        def handle(self, username: str, password: str) -> None:
          if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
          
          else:
            self.__raise_errors("Dados inválidos")
          
        def __verify_input_data(self, username: str, password: str) -> bool:
          return isinstance(username, str)  and isinstance(password, str)
        
        def __verify_input_in_database(self, username: str) -> None:
          print('Acessando o banco de dados')
          print('Verificando a existencia do usuario')
        
        def __insert_new_user(self, username: str, password: str) -> None:
          print('Cadastro de usuarios realizado com sucesso')
        
        def __raise_errors(self, message: str) -> Exception:
          raise Exception(message)

   ```

2. **Open/Closed Principle (OCP) - Princípio Aberto/Fechado**  
   As entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação. Isso significa que você deve ser capaz de adicionar novas funcionalidades sem alterar o código existente.

   ```python
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
              print("Human Resources hiring new devs")
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
            print("Human Resources hiring new devs")


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

   ```

3. **Liskov Substitution Principle (LSP) - Princípio da Substituição de Liskov**  
   Objetos de uma classe derivada devem poder substituir objetos da classe base sem alterar o comportamento esperado do programa. Isso garante que as subclasses sejam substituíveis pelas suas superclasses.  

    ```python
        # Exemplo ruim
        class Bird:
          def fly(self) -> None:
            print("Flying")

        class Sparrow(Bird):
          pass

        class Ostrich(Bird):
          def fly(self) -> None:
            raise Exception("Ostriches can't fly")

        def make_bird_fly(bird: Bird) -> None:
          bird.fly()

        sparrow = Sparrow()
        ostrich = Ostrich()

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
    
    ```

4. **Interface Segregation Principle (ISP) - Princípio da Segregação de Interfaces**  
   Muitas interfaces específicas são melhores do que uma interface única e geral. Isso significa que os clientes não devem ser forçados a depender de interfaces que não utilizam.

5. **Dependency Inversion Principle (DIP) - Princípio da Inversão de Dependência**  
   Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes; detalhes devem depender de abstrações. Isso ajuda a reduzir o acoplamento entre os componentes do sistema.


---

![Imagem retirada do blog Byte Byte Go - https://blog.bytebytego.com/p/ep175-what-is-the-solid-principle](image.png)
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

3. **Liskov Substitution Principle (LSP) - Princípio da Substituição de Liskov**  
   Objetos de uma classe derivada devem poder substituir objetos da classe base sem alterar o comportamento esperado do programa. Isso garante que as subclasses  sejam substituíveis pelas suas superclasses.  

4. **Interface Segregation Principle (ISP) - Princípio da Segregação de Interfaces**  
   Muitas interfaces específicas são melhores do que uma interface única e geral. Isso significa que os clientes não devem ser forçados a depender de interfaces que não utilizam.

5. **Dependency Inversion Principle (DIP) - Princípio da Inversão de Dependência**  
   Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes; detalhes devem depender de abstrações. Isso ajuda a reduzir o acoplamento entre os componentes do sistema.


---

![Imagem retirada do blog Byte Byte Go - https://blog.bytebytego.com/p/ep175-what-is-the-solid-principle](image.png)
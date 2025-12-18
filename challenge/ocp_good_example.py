'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''
from typing import List
from abc import ABC, abstractmethod
class Exam(ABC):
    @abstractmethod
    def exam_verification(self):
        pass
    
    @abstractmethod
    def exam_name(self):
        pass
    
class BloodExam(Exam):
    def exam_verification(self):
        print("Verificando as condicoes do exame de sangue")
    
    def exam_name(self):
        return "Exame de sangue"

class XRayExam(Exam):
    def exam_verification(self):
        print("Verificando as condicoes do exame de raio-x")
    
    def exam_name(self):
        return "Raio-x"

class ExameFezes(Exam):
  def exam_verification(self):
          print("Verificando as condicoes do exame de fezes")
      
  def exam_name(self):
      return "Exame de Fezes"

class Approver:
    def verify_exam(self, exam: Exam) -> bool:
        exam.exam_verification()
        return True
    
    def approve_exam(self, exams: List[Exam]):
        for exam in exams:
            result = self.verify_exam(exam)
            if result:
                print(f"Exame {exam.exam_name()} foi aprovado")


raio_x = XRayExam()
sangue = BloodExam()
fezes = ExameFezes()
exams = [raio_x, sangue, fezes]
aprovador = Approver()

aprovador.approve_exam(exams)


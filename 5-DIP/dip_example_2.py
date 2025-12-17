from abc import ABC, abstractmethod
from typing import List

class Notificator(ABC):
  @abstractmethod
  def send_notification(self, message: str) -> None: pass 

class NotificatonEmail(Notificator):
  def send_notification(self, message: str) -> None:
    print (f"Sending email: {message}")

class NotificationSMS(Notificator):
  def send_notification(self, message: str) -> None:
    print (f"Sending SMS: {message}")

class NotificationWhatsApp(Notificator):
  def send_notification(self, message: str) -> None:
    print(f"Send WhatsApp: {message} ")

class MultiNotificatior(Notificator):
  def __init__(self, notificators: List[Notificator]) -> None:
    self.__notificators = notificators
  
  def send_notification(self, message: str) -> None:
    for notificator  in self.__notificators:
      notificator.send_notification(message)

class ClientService:
  def __init__(self, notificator: Notificator) -> None:
    self.notificator = notificator
  
  def send(self, message: str) -> None:
    self.notificator.send_notification(message)

email = NotificatonEmail()
sms = NotificationSMS()
whatsapp = NotificationWhatsApp()

multi_notificator = MultiNotificatior(notificators=[email, sms, whatsapp])

servico = ClientService(multi_notificator)
servico.send("Pedido processado com sucesso!")

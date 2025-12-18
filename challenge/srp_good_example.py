from abc import ABC, abstractmethod

class TaskHandler:
    def create_task(self, name: str, description: str) -> None:
        pass

    def update_task(self, id: int, name: str, description: str) -> None:
        task = self.__search_task(id)
        pass

    def remove_task(self, id: int) -> None:
        pass
    
    def __search_task(self, id: int) -> None:
        pass


class Notificator(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotificator(Notificator):
    def send_notification(self, message):
        print(f"EMAIL: {message}")


class WhatsAppNotificator(Notificator):
    def send_notification(self, message):
        print(f"WhatsApp: {message}")



class ReportHandler:
  def handle(self):
    self.__generate_report()
    self.__send_report()

  def __generate_report(self):
      pass

  def __send_report(self):
      pass


class ConnectApi:
  def conect_api(self):
      pass
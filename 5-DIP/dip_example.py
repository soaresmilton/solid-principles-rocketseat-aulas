# Exemplo ruim
class MySQLDatabaseRuim:
  def connect(self) -> None:
    print("Connecting to MySQL Database")

class UserRepositoryRuim:
  def __init__(self) -> None:
    self.database = MySQLDatabaseRuim()

  def get_user(self, user_id: int) -> None:
    self.database.connect()
    print(f"Getting user {user_id}")

# Aplicando conceitos DIP:
from abc import ABC, abstractmethod

class Database(ABC):
  @abstractmethod
  def connect(self) -> None:
    pass

class MySQLDatabase(Database):
  def connect(self) -> None:
    print("Connecting to MySQL Database")
  
class PostgreSQLDatabase(Database):
  def connect(self) -> None:
    print("Connecting to PostgreSQL")

class UserRepository:
  def __init__(self, database: Database) -> None:
    self.database = database

  def get_user(self, user_id: int) -> None:
    self.database.connect()
    print(f"Getting user {user_id}")

mysql_db = MySQLDatabase()
postgre_db = PostgreSQLDatabase()
user_repo = UserRepository(postgre_db)
user_repo.get_user(123)

user_repo = UserRepository(mysql_db)
user_repo.get_user(1)

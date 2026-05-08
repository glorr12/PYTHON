class User:
    """Класс для представления пользователя системы.
        Хранит учетные данные и ведет глобальный счетчик успешно
        созданных экземпляров"""
    total_users = 0
    def __init__(self, username: str, password:str) -> None:
        """Инициализирует новый экземпляр пользователя"""
        self.username = username
        self.password = password
        User.total_users += 1
    @classmethod
    def get_total(cls) -> int:
        """Возвращает общее количество созданных пользователей"""
        return User.total_users

user1 = User("user1", "")
user2 = User("user2", "")
user3 = User("user3", "")
print(f"total users: {user3.get_total()}")


# -------------------------------------------------

class User:
    """Класс для представления пользователя системы.
       Хранит учетные данные и ведет глобальный счетчик успешно
       созданных экземпляров"""
    total_users = 0
    def __init__(self, username: str, password:str) -> None:
        """Инициализирует новый экземпляр пользователя"""
        if username == "":
            raise ValueError("Username cannot be empty")

        if len(password) < 5:
            raise ValueError("Password must be at least 5 characters")
        self.username = username
        self.password = password

        User.total_users += 1


    def __str__(self):
        """Возвращает строковое представление объекта пользователя"""
        return f"User: {self.username}\nPassword: {self.password}"

    @classmethod

    def get_total(cls) -> int:
        """Возвращает общее количество созданных пользователей"""
        return User.total_users

try:
    user1 = User("user1", "qwe")
except ValueError as e:
    print(e)
try:
    user2 = User("", "qwerty123")
except ValueError as e:
    print(e)

try:
    user3 = User("user3", "qwerty123")
except ValueError as e:
    print(e)
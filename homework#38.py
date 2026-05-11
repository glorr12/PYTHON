class BankAccount:
    def __init__(self, name_holder: str, current_balance: float):
        self.__name_holder = name_holder
        self.__current_balance = current_balance
        self.__history_story = []

    @property
    def history(self) -> list:
        return self.__history_story


    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError('Error: Amount must be positive.')
        self.__current_balance += amount
        self.__history_story.append(f"Deposit:{amount}")

    def withdraw(self, amount:float ):
        if amount <= 0:
            raise ValueError("Error: Not enough funds.")
        if amount > self.__current_balance:
            raise ValueError("You cannot withdraw more than you have")
        self.__current_balance -= amount
        self.__history_story.append(f"Withdraw:{amount}")


    def balance(self) -> float:
        return self.__current_balance

account = BankAccount("Nikita", 100000)
print(account.balance())
account.deposit(2000)
account.deposit(1000)
print(account.balance())
account.withdraw(4000)
account.withdraw(800)
print(account.balance())

try:
    account.withdraw(100000000000)
except ValueError as e:
    print(e)

try:
    account.deposit(-3)
except ValueError as e:
    print(e)

print(account.balance())
print(f"Operation history:")
for i in account.history:
    print(f"\t\t{i}")
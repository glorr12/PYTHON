from datetime import datetime

class Email:
    def __init__(self,sender,recipient,subject,body: str,date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date


    def __len__(self) -> int:
        return len(self.body)

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\nBody: - {self.body} -"

    def __bool__(self) -> bool:
        return bool(self.body.strip())

    def __gt__(self, other):
        if not isinstance(other,Email):
            return False
        return self.date > other.date


e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
print(e1)
print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)



# ---------------------------------------------------------



class Money:
    def __init__(self, amount: int | float):
        self.amount = amount

    def __add__(self, other:"Money")->"Money":
        return Money(self.amount + other.amount)

    def __sub__(self, other:"Money")->"Money":
        if self.amount - other.amount < 0:
            return Money(0)
        return Money(self.amount - other.amount)

    def __str__(self):
        return f"${self.amount}"


money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)
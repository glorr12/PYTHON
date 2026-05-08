class Person:
    def __init__(self, name:str)-> None:
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def __init__(self, name:str, course:int)-> None:
        super().__init__(name)
        self.course = course
    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}")

class Teacher(Person):
    def __init__(self, name:str, subject:str)-> None:
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}. My subject is {self.subject}")

group1 = [Student("Alice", 2), Teacher("Bob", "Mathematics")]

for g in group1:
    g.introduce()
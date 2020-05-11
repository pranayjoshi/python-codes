class subject:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grade = grades

class science(subject):
    def __init__(self, name, age, grades, colour):
        super().__init__(name, age, grades)
        self.colour = colour
        self.sub = "science"
    def using_super(self):
        print(f"your age is {self.age} and your name is {self.name} you are studying {self.sub}")
    def functi(self):
        if self.grade < 33:
            print(f"you are pass in {self.sub}")
        else: print(f"you are pass in {self.sub}")
class maths(subject):
    def functi(self):
        if self.grade > 33:
            print(self.grade)
        else: print("fail")
    
a = maths("pranay", 14, 45)
a.functi()
b = science("pranay", 14, 23, "red")
b.functi()
b.using_super()



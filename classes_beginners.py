class sm:
    def __init__(self, name, age, constant):
        self.name = name
        self.age = age
        self.constant = constant
    def res(self):
        print(f"your age is {self.age} and your name is {self.name}")
    def const(self, na):
        if self.name == na:
            return self.constant
class dm:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def ret(self, j):
        constant = sm.const(j, self.name)
        if self.age >= constant:
            return True
        else: return False

a = sm("pr", 12, 11)
a2 = dm("pr", 12)
print(a2.ret(a))


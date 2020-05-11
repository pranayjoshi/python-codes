class ace:
    first = 10
    second = 5
    def __init__(self):
        ace.add()
    @classmethod
    def add(cls):
        print(cls.first + cls.second)
ace()

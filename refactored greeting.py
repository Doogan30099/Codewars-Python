class Person():
    def __init__(self, name):
        self.name = name
        
        
    def greet(self, Person):
        return f"Hello {Person}, my name is {self.name}"
        
joe = Person("Joe")
print(joe.greet("Kate"))

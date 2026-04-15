class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18
    
    def introduce(self):
        status = "Adult" if self.is_adult() else "Not Adult"
        return f"My name is {self.name} and I'm {self.age} years old.I'm {status}"

p1 = Person("Rajesh",14)
print(p1.introduce())
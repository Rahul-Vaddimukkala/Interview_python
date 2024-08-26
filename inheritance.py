class Person():
    def __init__(self, name):
        self.name = name

    def Hello(self):
        print("Hello is from Person class")
    
class Employee(Person):
    def Hi(self):
        print("Hi is from Employee Class")

emp = Person("Rahul")
emp.Hello()

emp = Employee("Ravi") 
emp.Hi()
emp.Hello()



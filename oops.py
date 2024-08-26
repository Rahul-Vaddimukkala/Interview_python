class Master():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def greetings(self):
        print("Hello "+ self.name)
        
name="Rahul"
age=26
gender="male"
m= Master(name,age,gender)
print(m)
print(m.name)
print(m.age)
print(m.gender)
m.greetings()




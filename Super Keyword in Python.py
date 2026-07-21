# Super Varaiable()
class Person:
    def __init__(self):
        self.name="Prasanna"
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.parent_name=self.name
        self.name="Rana"
    def Display(self):
        print("Parent Name:",self.parent_name)
        print("Child Name:",self.name)
c=Customer()
c.Display()

class Person:
    def __init__(self,pid,name):
        self.pid=pid
        self.name=name
class customer(Person):
    def __init__(self,pid,name,age,gender):
        super().__init__(pid,name)
        self.age=age
        self.gender=gender
    def display(self):
        print(self.pid,self.name,self.age,self.gender)
x=customer(524,"Prasanna",21,"Female")
y=customer(421,"Lahari",22,"Female")
x.display()
y.display()

# Super Method()
class Person:
    def display(self):
        print("This is Super Class Method")
class Customer(Person):
    def display(self):
        super().display()
        print("This is Sub Class Method")
c1 = Customer()
c1.display()

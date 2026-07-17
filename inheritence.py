#single inheritence
class Animal:
    def eat(self):
        print("Animal Are Eating")
class Tiger(Animal):
    def hunt(self):
        print("Tiger hunting")
a1=Animal()
a1.eat()
t1=Tiger()
t1.eat()
t1.hunt()

#program for student marks result
class Student:
    def getdata(self):
        self.name = input("Enter Student Name: ")
        self.marks = int(input("Enter Marks: "))
class Result(Student):
    def showresult(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
r = Result()
r.getdata()
r.showresult()

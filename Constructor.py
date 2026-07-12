# default Constructor:
class Student:
    def __init__(self):
        print("Default constructor executed")
        self.sid=None
    def printStudent(self):
        print(self.sid)
s1=Student()
s1.printStudent()

# parameterized constructor
class Student:
    def __init__(self):
        self.sid=int(input("Enter Your SID:"))
        self.sname=input("Enter Your Name:")
        self.age=int(input("Enter Your Age:"))
    def printStudent(self):
        print(self.sid,self.sname,self.age)
s1=Student()
s1.printStudent()

# Static Variable
class Student:
    coursename="python"
    def __init__(self,sid,name):
        self.sid=sid
        self.name=name
    def printStudent(self):
        print(self.sid,self.name)
s1=Student(24,"Rana")
s2=Student(67,"Riya")
s1.printStudent()
s2.printStudent()

# Static Method
class Student:
    coursename="python"
    def __init__(self,sid,name):
        self.sid=sid
        self.name=name
    @staticmethod
    def change():
        Student.coursename="Java"
    def printStudent(self):
        print(self.sid,self.name,self.coursename)
Student.change()
s1=Student(24,"Rana")
s2=Student(67,"Riya")
s1.printStudent()
s2.printStudent()

#class
class student:
    def __init__(self):
        self.sid = 524
        self.name = "Rana"
        self.fee = 654.97
    def printstudent(self):
        print(self.sid, self.name, self.fee)
s = student()        # Create object
s.printstudent()     # Call method

# object
class student:
    def insert(self, sid, name, fee):
        self.sid = sid
        self.name = name
        self.fee = fee
    def printstudent(self):
        print(f"{self.sid}, {self.name} and {self.fee}")
s1 = student()
s1.insert(899, "Riya", 9887.09)
s1.printstudent()
s2 = student()
s2.insert(987, "Ishika", 8976.00)
s2.printstudent()

#WAPP for class and object using with constructor
class student:
    def __init__(self, sid, name, fee):
        self.sid = sid
        self.name = name
        self.fee = fee
    def printstudent(self):
        print(f"{self.sid}, {self.name} and {self.fee}")
s1 = student(532, "Priya", 765)
s1.printstudent()
s2 = student(524, "Kavya", 145)
s2.printstudent()

#WAPP to find the biggest of 3 numbers with class and object
class BigThreeNumber:
    def __init__(self):
        self.n1=int(input("Enter your n1 Value:"))
        self.n2=int(input("Enter your n2 Value:"))
        self.n3=int(input("Enter your n3 Value:"))
    def printResult(self):
        if self.n1>self.n2 and self.n1>self.n3:
            print(self.n1,"Is Biggest")
        elif self.n2>self.n1 and self.n2>self.n3:
            print(self.n2,"Is Biggest")
        else:
            print(self.n3,"Is Biggest")
b1=BigThreeNumber()
b1.printResult()

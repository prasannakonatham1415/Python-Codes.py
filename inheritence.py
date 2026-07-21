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


# Multi-Level inhertience
class vivo1:
    def call(self):
        print("Making Call")
    def sms(self):
        print("Send Msg")
class vivo2(vivo1):
    def radio(self):
        print("Play Music with Radio")
    def mp3(self):
        print("Play Mp3 Music")
class vivo3(vivo2):
    def youtube(self):
        print("Play Audio And Videos with Youtube")
    def word_doc(self):
        print("Read a Word Document")
v1 = vivo1()
v1.call()
v1.sms()
print("Vivo2")
v2 = vivo2()
v2.call()
v2.sms()
v2.radio()
v2.mp3()
print("Vivo3")
v3 = vivo3()
v3.call()
v3.sms()
v3.radio()
v3.mp3()
v3.youtube()
v3.word_doc()

# Hierarchial inheritence
class Mi:
    def call(self):
        print("Make a call")
class Mi1(Mi):
    def sms(self):
        print("Sms For Creating Messages")
class Mi2(Mi1):
    def radio(self):
        print("Play Music")
class Mi3(Mi):
    def mp3(self):
        print("Play Audio For Music")
class Mi4(Mi3):
    def youtube(self):
        print("Play Audio And Video")
m1=Mi2()
m1.call()
m1.sms()
m1.radio()
m2=Mi4()
m2.call()
m2.mp3()
m2.youtube()

# Mutilple Inheritence
class Father:
    def Phone(self):
        print("Father Have Phone")
class Mother:
    def Tab(self):
        print("Mother Have Tab")
class Child(Father,Mother):
    def Watch(self):
        print("child Has Watch")
x=Child()
x.Phone()
x.Tab()
x.Watch()

# hybrid inhheritence
class vivo1:
    def call(self):
        print("Making Call")
class vivo2:
    def sms(self):
        print("Send SMS")
class vivo3(vivo1):
    def radio(self):
        print("Play Audio Music")
class vivo4(vivo2,vivo3):
    def mp3(self):
        print("Play MP3 Music")
v2=vivo2()
v2.sms()
v3=vivo3()
v3.call()
v3.radio()
v4=vivo4()
v4.call()
v4.sms()
v4.radio()
v4.mp3()


# abstract method
from abc import ABC, abstractmethod
class A(ABC):
    def m1(self):
        print("Hello A Class")
    @abstractmethod
    def m2(self):
        pass
class B(A):
    def m2(self):
        print("This is abstract class")
b1 = B()
b1.m1()
b1.m2()

# abstract class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def welcome(self):
        print("Welcome to APSRTC")
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Bus started")
c1 = Car()
c1.welcome()
c1.start()

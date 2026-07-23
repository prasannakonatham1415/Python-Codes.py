from threading import Thread
def run():
    print("Thread is running")
    for i in range(10):
        print(i)
t1 = Thread(target=run)
t1.start()
t1.join()

from threading import Thread
class MyThread(Thread):
    def run(self):
        print("Thread is running")
t1 = MyThread()
t1.start()
t1.join()

#single tasking
from threading import Thread
import time
class SingleThread(Thread):
    def run(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print("Preparing tea")
        time.sleep(2)
    def task2(self):
        print("Boiling milk")
        time.sleep(2)
    def task3(self):
        print("Tea is ready!")
        time.sleep(2)
t1 = SingleThread()
t1.start()
t1.join()
print("All tasks completed.")

#multi tasking
from threading import Thread
import time
def cooking():
    for i in range(5):
        print("Cooking")
        time.sleep(1)
def washing():
    for i in range(5):
        print("Washing Clothes")
        time.sleep(1)
t1 = Thread(target=cooking)
t2 = Thread(target=washing)
t1.start()
t2.start()
t1.join()
t2.join()
print("Both Tasks Completed")

#without synchorinzation
from threading import Thread
class Movie:
    def book(self, name):
        print(name,"Booking Ticket")
m = Movie()
t1 = Thread(target=m.book, args=("Rana",))
t2 = Thread(target=m.book, args=("Riya",))
t1.start()
t2.start()
t1.join()
t2.join()
print("Booking Completed")

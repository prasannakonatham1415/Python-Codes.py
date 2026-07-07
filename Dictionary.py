a = {"id":24, "Name":"Rana", "Salary":27500}
a.pop("Salary")
a.popitem()
a.clear()
print(a)

students={}
n=int(input("Enter the no.of students:"))
for i in range(n):
  names=input("Enter the name of students:")
  marks=int(input("Enter the marks of student:"))
  students.update({names:marks})
print(students)

#display student names only
for name in students.keys():
  print(name)

#display student marks only
for mark in students.values():
     print(mark)
print("Enter student name:",end="")
name=input()
marks=students.get(name,-1)
if (marks==-1):
    print("Student not found")
else:
    print("{} made marks = {}".format(name, marks))

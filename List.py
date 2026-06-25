list=[]
nums=[10,20,30,60]
print(type(nums))
print(nums)

prices=[12.00,45.87,98.77,98.56,78.99]
student=["Rana",524,"Python","A+"]
print(prices)
print(student)

names=eval(input("Enter your names:"))
print(names)

even_nums=list(range(2,30,2))
print(even_nums)
print(type(even_nums))
print(even_nums[1])

list=[11,22,33,44,55,99,88,67]
print(list[6])
print(list[-8])
print(list[1:5:2])

nums=[1,2,3,4,5,6,7,8,9,10]
print(len(nums))
print(nums[::])
print(nums[0:6])
print(nums[0:10:2])
print(nums[-1:-11:-1])
print(nums[-1:-11:-3])

animals=['tiger','lion','fox','rabbit','dog','cat','rat','elephant']
print(animals[::])
print(animals[0:9:2])
print(animals[-1:-8:-4])

animals=['tiger','lion','fox','rabbit','dog','cat','rat','elephant']
for animal in animals:
    print(animal,end=" ")

animals=['tiger','lion','fox','rabbit','dog','cat','rat','elephant']
length=len(animals)
for animal in animals[-1:-length:-1]:
    print(animal,end=" ")

animals = ['tiger', 'lion', 'fox', 'rabbit', 'dog', 'cat', 'rat', 'elephant']
for animal in animals:
    print(animal.upper(), end=" ")

animals = ['tiger', 'lion', 'fox', 'rabbit', 'dog', 'cat', 'rat', 'elephant']
for animal in animals:
    if animal.startswith ("r"):
        print(animal,end=" ")

num=[15,4,31,14]
print(num)
print(type(num))
print(num[0])

num=[15,4,31,14,61]
print(num[-1:-5])

arr=[3,7,8,2,5,6,4]
sum=(arr[0]+arr[6])
print(sum)

arr=[3,7,8,2,5,6,4]
if arr[0]==2:
    print("First element of array is even")
else:
    print("Not Even")

arr = [3, 7, 8, 2, 5, 6, 9]
num = arr[-1]
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

arr = [3, 7, 8, 2, 5, 6, 4]
print(arr[len(arr)//2])

arr = [10, 20, 30, 40, 50, 60]
print(arr[2] + arr[3])







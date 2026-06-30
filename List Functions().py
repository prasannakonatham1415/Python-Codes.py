nums=[100,200,300,400,100,200,100,600,900]
print(len(nums))
print(nums.count(100))
print(nums.count(900))
print(nums.count(200))

names=["lakshmi Narayana","Lakshmi","Lahari"]
print(names)
names.append("Rana")
print(names)

names=["lakshmi Narayana","Lakshmi","Lahari"]
print(names)
animal_names=["tiger","lion","fox"]
names.extend(animal_names)
print(names)

animals=["tiger","lion","fox"]
animals.insert(0,"Rabbit")
print(animals)
animals.insert(4,"cat")
print(animals)

x = ["A", "B", "C", "D", "R"]
x.pop()
print(x)
x.pop(3)
print(x)

x = ["A", "B", "C", "D", "R"]
x.remove("R")
print(x)

x = ["A", "B", "C", "D", "R"]
x.clear()
print(x)

i=["L","P","R","A","M","O"]
print(i)
i.sort()
print(i)

i=["L","P","R","A","M","O"]
i.sort(reverse=True)
print(i)

nums=[1,2,3,4,5,6]
print(nums)
new_nums=nums.copy()
print(new_nums)

nums = [15, 4, 31, 14]
minimum = min(nums)
maximum = max(nums)
total = sum(nums)
print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)

lst=[2,4,6,8,10,12]
print(lst)
new_lst=[]
for i in lst:
    new_lst.append(i**3)
print(new_lst)

lst=[
    [11,22,33],
    [17,41,73],
    [15,4,31]
]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[0][1])
print(lst[1][0])
print(lst[2][1])

lst=[
    [11,22,33],
    [17,41,73],
    [15,4,31]
]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j],end=" ")
    print()

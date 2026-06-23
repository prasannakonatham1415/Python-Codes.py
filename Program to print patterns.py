for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,end="")
    print()

for i in range(5):
    for j in range(5):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()

for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()

for i in range(5):
  for j in range(5):
    print(chr(65+i),end="")
  print()

for i in range(5):
  for j in range(5):
    print(chr(65+j),end="")
  print()

for i in range(5):
  for j in range(5):
    print(chr(69-j),end="")
  print()

for i in range(5):
  for j in range(5):
    print(chr(69-i),end="")
  print()

for i in range(5):
  for j in range(5):
    if i%2==0:
      print("$",end="")
    else:
      print("#",end="")
  print()

for i in range(5):
  for j in range(5):
    if j%2==0:
      print("$",end="")
    else:
      print("#",end="")
  print()

for i in range(5):
    for j in range(5):
        num=(i+j-1)%9+1
        print(num,end="")
    print()

num = 1
for i in range(5):
    for j in range(5):
        print(num, end="")
        num = num + 1
        if num == 10:
            num = 1
    print()

for i in range(1,6):
    for j in range(1,6):
        if i%2==0:
            print(i,end="")
        else:
            print(j,end="")
        print()

for i in range(1, 6):
    for j in range(1, 6):
        if i % 2 != 0:
            print(i, end="")
        else:
            print(j, end="")
    print()

for i in range(5,0,-1):
    for j in range(5,0,-1):
        if i % 2 != 0:
            print(i, end="")
        else:
            print(j, end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()

for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()

for i in range(1, 6):
    for j in range(1, j + 1):
        print(i, end="")
    print()

for i in range(1, 6):
    for j in range(6, i, -1):
        print(i, end="")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print(i, end="")
    print()

for i in range(5, 0, -1):
    for j in range(6 - i):
        print(i, end="")
    print()


num=1
for i in range(1, 6):
    for j in range(i):
        print(num, end="")
        num = num + 1
        if num == 10:
            num = 1
    print()

num = 1
for i in range(5, 0, -1):
    for j in range(i):
        print(num, end="")
        num = num + 1
        if num == 10:
            num = 1
    print()

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,6):
    for s in range(1,6-i):
        print(" ",end="")
    for j in range(1,1+i):
        print("*",end="")
    print()

for i in range(5,0,-1):
    for s in range(1,6-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

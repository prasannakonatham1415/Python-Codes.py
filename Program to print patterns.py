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




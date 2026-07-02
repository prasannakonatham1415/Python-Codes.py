n=(1,2,7,4,5)
print(n[0])

n=(1,2,7,4,5)
print(n[::2])

n=(1,2,7,4,5)
for i in n:
  print(i)

val=(1,2,3,4,5,6,1,3,4)
print(val.count(1))

n=(1,2,7,4,5)
print(len(n))

val=(900,20,300,400,100,600,6,100)
print(len(val))
c=val.count(100)
print(c)
print(min(val))
print(max(val))
print(val.index(400))
print(sorted(val))
print(sorted(val, reverse=True))

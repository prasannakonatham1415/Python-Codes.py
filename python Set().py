# Static typed Creation
s1={10,20,30,40,10}
print(s1)

# with eval() function
s1=eval(input("Enter Your Value:"))
print(s1,type(s1))

# with set() and range() function
x=set(range(2,31,2))
print(x)

# with list() and set() function
lst={1,2,3,4,5,1,2}
c=set(lst)
print(c)

# Accessing With for loop
nums={2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
for num in nums:
  print(num,end=" ")


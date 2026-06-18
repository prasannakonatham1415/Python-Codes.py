n=int(input("Enter a Number:"))
temp=n
sum=0
while n>0:
  rem=n%10
  sum=sum+rem**3
  n=n//10
if sum==temp:
  print("It is armstrong Number")
else:
  print("Not a armstrong Number")

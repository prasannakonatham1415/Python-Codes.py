n=int(input("Enter a Number:"))
temp=n
rev=0
while n>0:
  rem=n%10
  rev=rev*10+rem
  n=n//10
if rev==temp:
  print(" It is palindrome Number")
else:
  print("Not a palindrome Number")

# program to find the square root value for the given number without library method
n = int(input("Enter a Number: "))
i = 1
while i <= n:
    if i * i == n:
        print("Square Root =", i)
        print()
    i = i + 1

# check Number is Postive or Negative or Zero
x=int(input("Enter the Number:"))
if x>0:
    print("Postive Values")
elif x<0:
    print("Negitive Values")
else:
    print("The Value is Zero")

# Check The Character is alphabet or digit or symbol
a = input("Enter a Character: ")
if a.isalpha():
    print("The Given Character is Alphabet")
elif a.isdigit():
    print("The Given Character is Digit")
else:
    print("The Given Character is Symbol")

# Chech to find biggest of three numbers
a=int(input("Enter the a Value:"))
b=int(input("Enter the b Value:"))
c=int(input("Enter the c Value:"))
if a>b and a<c:
   print("a is Big")
elif b>a and b>c:
   print("b is Big")
else:
    print("c is Big")

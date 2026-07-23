# try block
try:
    a=57
    b=0
    print(a/b)
except:
    print("cannot divide")

# except block
try:
    num=98
    print(num/0)
except:
    print("invalid input")

#try-finally block
try:
    x = 45
    y = 0
    result = x / y
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError handled")
finally:
    print("The code executed successfully")

# default except block
try:
    x = 45
    y = 0
    result = x / y
    print(result)
except:
    print("ZeroDivisionError handled")
finally:
    print("The code executed successfully")

# assert keyword
x=88
print("Valid for vote")
assert x>=18,"not valid for vote"
print("voted successfully")

age=6
if age<0:
  raise ValueError("Age can't be negavtive")
print("Vaild Age")

try:
  a=int(input("Enter a value:"))
  b=int(input("Enter b value:"))
  div=a/b
  print(div)
except:
  print("Error handled successfully")
finally:
  print("This is last statement")

def add_num():
  n1=100
  n2=200
  add=n1+n2
  print(add)
add_num()

def sub_num():
  n1=100
  n2=200
  sub=n1-n2
  print(sub)
sub_num()

def even_num(n):
  if n%2==0:
    print("Even")
  else:
    print("Odd")
even_num(75)

def big_num(x,y,z):
  if x>y and x>z:
    print(x)
  elif y>x and y>z:
    print(y)
  else:
    print(z)
big_num(15,4,14)

def simple_interest(p,r,t):
    a=(p*r*t)/100
    print(a)
simple_interest(17,16,15)

def avg_num(a,b,c,d):
    x=(a+b+c+d)/4
    print(x)
avg_num(15,4,31,14)

def vote_valid(n):
    if n>=18:
        print("Valid for voting")
    else:
        print("Invalid")
vote_valid(37)

# with parameter with return type
def simple_interest(p,r,t):
    a=(p*r*t)/100
    return a
result=simple_interest(17,16,15)
print(result)

# without parameter with return type
def simple_interest(p,r,t):
    p=int(input("Enter the principal value:"))
    r=int(input("Enter the rate value:"))
    t=int(input("Enter the time value:"))
    x=(p*r*t)/100
    return x
result=simple_interest(17,16,15)
print(result)

# with parameter without return type
def simple_interest(p,r,t):
    a=(p*r*t)/100
    print(a)
simple_interest(17,16,15)

# without parameter without return type
def simple_interest():
    p=int(input("Enter the principal value:"))
    r=int(input("Enter the rate value:"))
    t=int(input("Enter the time value:"))
    x=(p*r*t)/100
    print(x)
simple_interest()

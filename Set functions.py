# program to print common element from give list
n={10,20,30,40}
s={50,60,10,20}
print(n & s)

# program for print different values from given list
a={2,3,4,5,7}
b={9,6,1,2,3}
print(a.symmetric_difference(b))

# program to print all elements from given set according to index and arrange that element in ascending and descending order
s = {15, 4, 31, 14, 7}
lst = list(s)
print(lst)
lst.sort()
print("Ascending:", lst)
lst.sort(reverse=True)
print("Descending:", lst)

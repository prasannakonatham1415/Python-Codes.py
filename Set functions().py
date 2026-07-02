s={10,20,30,40,50}
print(s)
s.add(200)
print(s)

s1={100,400,600,800}
s.update(s1)
print(s)

d={800,100,40,10,300,400,50,20}
print(d)
d.pop()
print(d)
d.remove(100)
print(d)
d.discard(100)
print(d)
d.clear()
print(d)

b={8,7,3,2,1,5}
print(b)
new_set=b.copy()
print(new_set)
print(min(b))
print(max(b))
print(sum(b))

# mathematical operators used in set
s={1,2,3,4,5}
s1={6,7,8,9,1,3}
print(s.union(s1))
print(s|s1)
print("Intersection ele")
print(s&s1)
print("differences ele")
print(s.difference(s1))
print(s-s1)
print("symmetric_difference ele")
print(s.symmetric_difference(s1))
print(s^s1)

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

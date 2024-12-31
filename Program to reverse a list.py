#Using reverse() method
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)


#Using list Slicing
a = [1, 2, 3, 4, 5]
rev = a[::-1]
print(rev)



#Using a loop 
a = [1, 2, 3, 4, 5]
rev = []
for val in a:
    rev.insert(0, val)
print(rev)
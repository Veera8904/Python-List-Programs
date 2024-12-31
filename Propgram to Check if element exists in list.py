#Check if element exists in list 

a = [10, 20, 30, 40, 50]
if 30 in a:
    print("Element exists in the list")
else:
    print("Element does not exist")





#using for loop

a = [10, 20, 30, 40, 50]
key = 30
list = False

for val in a:
    if val == key:
        list = True
        break

if list:
    print("Element exists in the list")
else:
    print("Element does not exist")




#using count()

a = [10, 20, 30, 40, 50]
if a.count(30) > 0:
    print("Element exists in the list")
else:
    print("Element does not exist")
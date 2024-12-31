#using Multiple assignment

a = [10, 20, 30, 40, 50]

a[1], a[3] = a[3], a[1]

print(a)



# Using a temporary variable

a = [10, 20, 30, 40, 50]
temp = a[2]
a[2] = a[4]
a[4] = temp

print(a)
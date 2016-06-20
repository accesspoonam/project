a = 5
b = 5
c = 5

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
print a
print b
print c
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


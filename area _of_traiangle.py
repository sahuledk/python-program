# Program to find the area of a triangle.

# Store the length of three numbers.
a = float(input("enter the length of side1 "))
b = float(input("enter the length of side2 "))
c = float(input("enter the length of side3 "))

# Finds the semi perimeter.
s = (a + b + c) / 2

# Display semi perimeter.
print('Semi perimeter is %0.3f' % s)

# Finds the area.
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Display the area.
print('The area of triangle is :%0.3f' % area)

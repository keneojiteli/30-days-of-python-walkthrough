import math

#1
age = 30

#2
height = 1.75  # in meters
print(type(height))

#3
complex_number = 3 + 4j

#4
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
print(f"The area of the triangle with base {base} and height {height} is {0.5 * base * height:.2f}")

#5
a = int(input("Enter the value of side a: "))
b = int(input("Enter the value of side b: "))
c = int(input("Enter the value of side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle with sides {a}, {b}, and {c} is {perimeter}")

#6
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area_of_rectangle = length * width
print(f"The area of the rectangle with length {length} and width {width} is {area_of_rectangle}")
perimeter_of_rectangle = 2 * (length + width)
print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter_of_rectangle}")

#7
pi = 3.14
radius = int(input("Enter the radius of the circle: "))
area_of_circle = pi * radius ** 2

circumference_of_circle = 2 * pi * radius
print(f"The circumference of the circle with radius {radius} is {circumference_of_circle:.2f}")

#8

#9 
x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
print(f"Slope = {slope:.2f}, Euclidean distance = {euclidean_distance:.2f}")

#10
#11

#12
a, b = "python", "dragon"
print(len(a) == len(b)) 

#13
print("on" in a and "on" in b )  

#14
word = "I hope this course is not full of jargon"
print("jargon" in word)

#15
print("on" not in a and "on" not in b )  

#16
length_of_python = len(a)
print(length_of_python, type(length_of_python))

python_to_float = float(length_of_python)
print(python_to_float, type(python_to_float))

python_to_str = str(python_to_float)
print(python_to_str, type(python_to_str))

#17
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

#alternatively, print(number % 2 == 0)

#18
print(7 // 3 == int(2.7))

#19
print(type(10) == type("10"))  # False, int is not the same as float

#20
#when converting from one data type to another, the format of the data must be compatible like the example below
print(type(int(float("9.8"))) == type(10))  

#21
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
salary = hours * rate
print(f"Your weekly earning is {salary}")

#22
number_of_years = int(input("Enter the number of years you have lived: "))
num_sec_per_year = 365 *24 * 60 * 60  # seconds in a year
print(f"You have lived for {number_of_years * num_sec_per_year} seconds")

#23
for i in range(1, 6):
    print(f"{i} {1} {i} {i ** 2} {i ** 3}")
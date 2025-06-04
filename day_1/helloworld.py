import sys #use a built in module to get the Python version
import math #use a built in module to get the square root

#level 2

#2.1
print(f"Python version: {sys.version}")
print()

#2.2
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(3 ** 4)
print(3 // 4)
print()

#2.3
fname = "Kene"
lname = "Ojiteli"
country = "Nigeria"
print(fname)
print(lname)
print(country)
print("I am enjoying 30 days of python")
print()

#2.4
num1 = 10
num2 = 9.8
num3 = 3.14
num4 = 4 - 4j

print(type(num1), type(num2), type(num3), type(num4))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(fname), type(lname), type(country))
print()

#level 3
#3.1
print(type(num1), type(num3), type(num4))
print(type("learning data types"))
print("True is of type", type(True))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(('Asabeneh', 'Python', 'Finland')))
print(type({'Asabeneh', 'Python', 'Finland'}))
print(type({"role": "Devops Engineer", "country": "Germany", "age": 30}))
print()

#3.2
x1, y1 = 2, 3
x2, y2 = 10, 8
Euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {Euclidean_distance}")
# print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {Euclidean_distance:.2f}")

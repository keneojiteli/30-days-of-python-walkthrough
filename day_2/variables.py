import math
#level 1

#1.1 create a folder called day_2. Inside this folder create a file named variables.py

#1.2
# Day 2: 30 Days of python programming

#1.3
f_name = "Kene"

#1.4
l_name = "Ojiteli"

#1.5
full_name = f"{f_name} {l_name}"

#1.6
country = "Germany"

#1.7
city = "Berlin"

#1.8
age = 30

#1.9
year = 2025

#1.10
is_married = False

#1.11
is_true = True

#1.12
is_light_on = True

#1.13
role, level, company = "Devops Engineer", 2, "Google"

#level 2
#2.1
print(type(f_name), type(l_name), type(full_name), type(country), type(city), type(age), type(year), type(is_married), type(is_true), type(is_light_on), type(role), type(level), type(company))

#2.2
print(len(f_name))

#2.3
check = len(f_name) == len(l_name)
print(f"Is the length of f_name equal to the length of l_name? {check}")

#alternative way to compare length
check1 =  len(f_name) is len(l_name)
print(f"Is the length of f_name equal to the length of l_name? {check1}")

#2.4 Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

#2.4.1
total = num_one + num_two
print(f"The sum of {num_one} and {num_two} is {total}")

#2.4.2
diff = num_one - num_two
print(f"The difference between {num_one} and {num_two} is {diff}")

#2.4.3
product = num_one * num_two
print(f"The product of {num_one} and {num_two} is {product}")

#2.4.4
division = num_one / num_two
print(f"The quotient of {num_one} and {num_two} is {division}")

#2.4.5
remainder = num_one % num_two
print(f"The modulus of {num_one} and {num_two} is {remainder}")

#2.4.6
exp = num_one ** num_two
print(f"The exponent of {num_one} to the power of {num_two} is {exp}")

#2.4.7
floor_division = num_one // num_two
print(f"The floor division of {num_one} by {num_two} is {floor_division}")

#2.5.1
radius = 30
area_of_circle = math.pi * radius ** 2
print(f"The area of a circle with radius {radius} is {area_of_circle:.2f}")

#2.5.2
circum_of_circle = 2 * math.pi * radius
print(f"The circumference of a circle with radius {radius} is {circum_of_circle:.2f}")

#2.5.3
radius = int(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius ** 2
print(f"The area of a circle with radius {radius} is {area_of_circle:.2f}")

#2.6
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
print(f"Your name is {f_name} {l_name}, you are {age} years old, and you live in {country}.")

#2.7
print(help('keywords'))
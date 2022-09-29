
print("basic print")
print("Hello, World")
print("=====================")
# Arithmetic Operators

print("Arithmetic Operators")
print("Addition: 2 + 2 = ", 2+2)
print("Subtraction: 2 - 2 = ", 2-2)
print("Multiplication: 2 * 2 = ", 2*2)
print("Division: 2 / 2 = ", 2/2)
print("Modulus: 2 % 2 = ", 2 % 2)
print("=====================")

# ** raises to the power of
print("Exponent: 2 ** 2 = ", 2**2)

# // returns the integer part of the quotient
print("Floor Division: 2 // 2 = ", 2//2)

# variables

print("Variables")
x = 2
y = 2
print("x + y = ", x+y)
print("=====================")

# lists

print("Lists")
my_list = [1, 2, 3, 4, 5]
your_list = my_list
print("Your List", your_list)
print("=====================")

# deep copy V shallow copy

print("Deep Copy V Shallow Copy")
my_list = [1, 2, 3, 4, 5]
your_list = my_list.copy()
print("Your List", your_list)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [a, b]
d = c.copy()
a[0] = 100
c[0][1] = -3
print("d = ", d)
print("=====================")

# Equality

print("Equality")
a = [1, 2, 3, 4, 5]
c = b
print("a == b", a == b)
print("=====================")

# collections
# list

print("List")
names = ["Alice", "Bob", "Charlie", "Debbie", "Eve", "Frank"]
print(names[0])
print(names[1])
print(names[-1])
print("=====================")

# boolean

print("boolean")
this_course_is_easy = True
print("=====================")

# and, or, not

print("and, or, not")
print((2 > 1) and (3 > 1))
print((2 > 1) or (3 > 1))
print(not (2 > 1))
print("=====================")

# region methods

print("Methods")
movie_title = "Spider-Man: Into the spiderverse"
print(movie_title.upper())
print(movie_title.lower())
print(movie_title.title())
print(movie_title.lower().count("e"))
print("=====================")

# region lists

print("lists")
names = ["Tim", "Kyle", "KevinS", "KevinD"]
print(names)
print(names[0])
names.append("Bob")
print(names)
names.insert(0, "Alice")
print(names)
names.remove("Bob")
print(names)

random_variable = [True, 1, "Hello", 3.14]
print(random_variable)

ordered_list = list(range(1, 1001))
print(ordered_list)
print("=====================")

# region tuples

print("Tuples")
traits = ("Tim", 35, "tall")
name = traits[0]
age = traits[1]
height = traits[2]
print(name, age, height)
trait = ("Kyle", 30, "short")
name, age, height = trait
print(name, age, height)
print("=====================")
# region sets

print("Sets")
dupilcate_numbers = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]
unique_numbers = set(dupilcate_numbers)
print(unique_numbers)
unique_numbers.add(11)
print(unique_numbers)
print (2 in unique_numbers)
print ("=====================")
# region dictionaries

print("Dictionaries")
student = {"name": "Tim", "age": 25, "courses": ["Math", "CompSci"]}
print(student)
print(student["name"])
print(student["courses"])
print(student.get("phone"))
print(student.get("phone", "Not Found"))
student["phone"] = "555-5555"
print(student)
print("=====================")

# region loops

print("Loops")
for i in range(1, 11):
    print(i)
print("=====================")

# Question

print("Question")

def flow_rate(Rn):

    if Rn < 0:
        print("Invalid number")
    elif Rn < 2000 and Rn > 0:
        print("Flow is Laminar")
    elif Rn > 10000 and Rn > 2000:
        print("Flow is Transitional")
    else:
        print("Flow is Turbulent")
    print("=====================")

flow_rate(100)
flow_rate(3000)
flow_rate(15000)
flow_rate(-1)

# region interation

print("Iteration")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for name in names:
    print(name)
print("=====================")

print("Iteration 2")

names = ["Tim", "Kyle", "KevinS", "KevinD"]
for i in range(len(names)):
    print(names[i])
print("=====================")

# region while loops

print("While Loops")
i = 1
while i <= 10:
    print(i)
    i += 1
print("=====================")

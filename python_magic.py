# creating a list
list1 = [x + 5 for x in [2, 3, 4]]    # list comprehension
print(list1)

# unary operator
x = 11
print(x+5 if x > 10 else 1)     # ternary operator with if condition

# operator overloading in list
a = [1, 3, 5, 7]
b = [6, 7, 8]
c = a + b     # operator overloading
print(c)
d = a * 2     # operator overloading
print(d)
#
#
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):      # position in for loop using enumerate
    print(position, surname)
for x, y in enumerate(surnames):      # position in for loop using enumerate
    print(x, y)                       # enumreate returns (posistion, surname)
#
#
# multiple.sequences
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for person, age in zip(people, ages):    # using zip as an example in for loop. This is efficient way of retriving from 2 list
 print(person, age)
 #
 #
 # multiple.sequences.implicit.py
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
nationalities = ['Poland', 'India', 'South Africa', 'England']
for data in zip(people, ages, nationalities):
 person, age, nationality = data            # here, the three-tuple data that comes from zip(...)
 print(person, age, nationality)
#
#
# for.else.py
class DriverException(Exception):
    pass
people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
    else:
        raise DriverException('Driver not found.')    # raise exception




"""
   Basis of python 
   from: 
       https://www.codecademy.com/learn/python
       https://www.datacamp.com/courses/intro-to-python-for-data-science
       https://www.datacamp.com/courses/intermediate-python-for-data-science
"""

### 1. Basic syntax.
"""
    Basic syntax of python is consistent with other popular programming languages
    such as C/C++/Java. And it's case sensitive.
"""
#   Get the current date
from datetime import datetime
now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#   Get the input and save it into a variable
pw = raw_input('enter your password: ')
print(pw)

### 2. As math calculator
#   numbers: integer and float
calc = [2 + 3, 4 * 7, 8 / 5, 8.0 / 5, 3 ** 2, 9 ** .5, 9 % 5]
calc

for x in calc :
    print(type(x))

### 3. Basic data type
#   int, float, bool, str
#   use type() to check the type of variable
myint = 1
myfloat = 1.3
print(int(myfloat), type(myint), type(myfloat))

#   True -> 1, False -> 0
mybool = True
print(mybool, mybool + 1)

myname = 'bangda sun'
myschool = 'columbia university'
myname + " " + myschool

#   convert to str type
str(2996)

#   escaping characters
mydeclare = 'This\'s my house'
print(mydeclare)

#   indexing characters in string
'bangda'[0]

#   string methods
myname.upper()
myname.lower()
len(myname) # len() function is very useful!

#   string print (also can be applied on other data types)
print("My name is %s and I\'m from %s" % (myname, myschool))
print('My name is %s and I\'m %d years old' % ('bangda', 23))

### 4. Control flow and loop
#   boolean operator / expression
1 < 2 and 2 < 3
1 == 3 or 2 > 3
not 1 != 0

#   apply in list
temperature = [17, 16, 18, 23, 24, 22, 21]
high_tem = temperature > 20  # doesn't return the expected result like in r.
high_tem = [entry > 20 for entry in temperature]
high_tem
#temperature[high_tem]  # doesn't work: list indices must be integers

#   control flow and loop
for x in range(100):
    if x % 2 == 0 and x < 50:
        print('%d is small even' % x)
    elif x % 2 == 0 and x >= 50:
        print('%d is large even' % x)
    else:
        print('%d is odd' % x)

i   = 0
sum = 0
while (i <= 100):
    sum += i
    i += 1
print(sum)

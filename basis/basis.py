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

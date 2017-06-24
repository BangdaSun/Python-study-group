"""
    List in python (build-in)
    Actually, using numpy will be more efficient
"""
### Create list
mylist = [6, 3, 3, 4, 1.5]
type(mylist)

### Index
#   start from zero
#   use negative integer to index backward
mylist[0]  # first element
mylist[-1]  # last element
mylist.index(6)  # element want to index

### Slicing
#   using : operator
#   list[start (included) : end (excluded)]
mylist[0:3] # select 1st to 3rd (index 0, 1, 2)
mylist[:4]  # select until 4th (index 0, 1, 2, 3)
mylist[3:]  # select start from 4th (index 3, 4, ...)

### Manipluation on list
#   expend
mylist_expd = [3] + mylist + [0.25]
print(mylist_expd)
mylist.append(5)  # add element at end
print(mylist)
mylist.insert(3, 4) # add element before specific index position

#   copy
mylist_copy = mylist[:] # IMPORTANT!
mylist_copy = list(mylist)

#   remove
mylist.remove(3)  # specify element want to remove
mylist.pop(0)     # specify index want to remove and return the removed element
del(mylist[0])    # delete directly

#   rearrange
#   keep in mind this will change list directly with no undo operations...
mylist.reverse
mylist.sort

### List comprehension
#   where we can creaet list using for loop but within one line
#   [output expr for iterator.var in iterable object]
#   [output expr + cond on output for iterator.var in iterable object + cond on iterable]

#   extract even numbers
import numpy as np
num  = np.random.randint(0, 100, 50)
even = [entry for entry in num if entry % 2 == 0]
even

#   if the number is odd, print 'odd', else print 'even'
even_odd = ['even' if entry % 2 == 0 else 'odd' for entry in num]
even_odd

### Iterator in list
#   list, dictionary, string are all iterable
#   python has iterator object, use iter() method
#   apply iter() to iterable object, create iterator
num_iter = iter(num)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))

#   iter over file conn
import os
os.getcwd()
file = open('file.txt')
file_iter = iter(file)

next(file_iter)
next(file_iter)
next(file_iter)

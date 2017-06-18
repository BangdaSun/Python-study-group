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
mylist[-1] # last  element

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
mylist_copy = mylist[:]
mylist_copy = list(mylist)

#   remove
mylist.remove(3)  # specify element want to remove
mylist.pop(0)     # specify index want to remove and return the removed element
del(mylist[0])    # delete directly

#   rearrange
#   keep in mind this will change list directly with no undo operations...
mylist.reverse
mylist.sort

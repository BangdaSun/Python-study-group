""" Basic python exercise """

"""
Problem 1
There are two ascending list:
    list1 = [3, 7, 8, 9, 12]
    list2 = [5, 6, 10, 13, 25, 30]

merge them into a new list --> list3 = [3, 5, 6, 7, 8, 9, 10, 12, 13, 25, 30]
use loop and .append()

@2017-07-08
Self analysis: idea of iterator. Also can relate to merge sort algorithm
"""

def merge(list1, list2):
    
    it1 = iter(list1)
    it2 = iter(list2)
    
    init1 = it1.next()
    init2 = it2.next()
    
    list3 = []
    
    # use iterator compare one by on
    for i in range(min(len(list1), len(list2)) + 2):
        if init1 < init2:
            list3.append(init1)
            init1 = it1.next()
        elif init1 > init2:
            list3.append(init2)
            init2 = it2.next()
        else:
            list3.append(init1)
            init1 = it1.next()
            init2 = it2.next()
    
    # rest of the list
    # ...  STILL NEED THINKING
    
    return list3

list1 = [3, 7, 8, 9, 12]
list2 = [5, 6, 10, 13, 25, 30]
merge(list1, list2)

def merge2(list1, list2):
    
    list3 = []
    
    # create two idx pointer and compare the elements at two idx
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            list3.append(list2[j])
            j += 1
        else:
            list3.append(list1[i])
            i += 1
            j += 1
            
    # all of elements in one of the list already in list3, move all of the rest elements of another list into list3 
    if (i + 1) < len(list1):
        for z in range(i, len(list1)):
            list3.append(list1[z])
    else:
        for z in range(j, len(list2)):
            list3.append(list2[z])
    
    return(list3)

list1 = [3, 7, 8, 9, 12]
list2 = [5, 6, 10, 13, 25, 30]
merge2(list1, list2)    
    
# -----------------------------------------------------------------------------

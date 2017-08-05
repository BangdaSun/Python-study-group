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
"""
Problem 2
Design the game of "rock, scissor, cloth"

@2017-07-15
"""
import random as rnd
choice_lst = ['rock', 'scissor', 'cloth']
winner_lst = [['rock', 'scissor'], ['scissor', 'cloth'], ['cloth', 'rock']]


while True:
    people_guess = input('Make your choice: ')
    computer_guess = rnd.choice(choice_lst)
    
    if people_guess not in choice_lst:
        people_guess = input('Please select from rock, scissor or cloth: ')
        continue
    
    if computer_guess == people_guess:
        print('Tie game, go overtime')
    elif [computer_guess, people_guess] in winner_lst:
        print('You lose, try again...')
    else:
        print('You win!')
        break

# -----------------------------------------------------------------------------
"""
Problem 3
Split the list by same adjacent elements
    [0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0] -->
    [0, 0, 0], [1, 1], [2], [3, 3, 3], [2], [3, 3, 3], [0, 0]

@2017-07-15
"""

# need to be revised, get error if all elements are identical, temporarily use set()
def splitLst(lst):
    
    returnLst = [] 
    lst_copy = lst[:]
    idx = 1
    
    # get return directly if there is only one element
    if len(lst_copy) == 1:
        returnLst.append(lst_copy)
    
    # while the lst_copy has at least one element
    while len(lst_copy) > 1:
        # cut point
        cutoff = 0
        
        # not a good choice here...
        if len(set(lst_copy)) == 1: 
            returnLst.append(lst_copy)
            break
        
        if lst_copy[idx] != lst_copy[idx - 1]:
            cutoff = idx 
            # cut off the prev part and append it into return list
            returnLst.append(lst_copy[:cutoff])
            del lst_copy[:cutoff]
            # start from beginning
            idx = 0
        
        idx += 1        
    
    return returnLst
            
splitLst([0])
splitLst([0, 0, 0])
splitLst([0, 1])
splitLst([0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0])            
    
    
def splitLst2(lst):
    returnLst = []
    lst_copy = lst[:]
    last_cut = 0

    for idx, element in enumerate(lst_copy):
        # if idx is not at the last position
        if idx < (len(lst_copy) - 1):
            
            if lst_copy[idx] != lst_copy[idx + 1]:
                returnLst.append(lst_copy[last_cut:(idx + 1)])
                last_cut = idx + 1
        # idx at last position
        else:
            returnLst.append(lst_copy[last_cut:])
        
    return returnLst

# test
splitLst2([0])
splitLst2([0, 0, 0, 0])
splitLst2([0, 0, 1, 1])
splitLst2([0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1, 1, 1, 1, 2]) 

"""
    other methods
    use a 2D list, see if the adjacent elements are equal, if yes:
        append it to result[-1]
    if not:
        append an empty list to result
"""
def splitLst3(lst):
    result = [[ ]]
    length = len(lst)
    
    for i in range(length):
        if i < (length - 1):
            if lst[i] == lst[i + 1]:
                result[-1].append(lst[i])
            else:
                result[-1].append(lst[i])
                # just like insert a 'marker' between two different elements
                result[-1].append([])
                
    result[-1].append(lst[i])
    return result

splitLst3([0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1, 1, 1, 1, 2]) 


"""
    Motivated by the above idea:
"""

def splitLst4(lst):
    result = ''
    str_lst = ''.join(str(x) for x in lst)
    length = len(str_lst)
    
    for idx, string in enumerate(str_lst):
        if idx < (length - 1):
            if str_lst[idx] == str_lst[idx + 1]:   
                result += str_lst[idx]
            else:
                result += str_lst[idx]
                result += '|'
    
    result += str_lst[idx]
    return result

result = splitLst4([0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1, 1, 1, 1, 2]) 
# get '000|11|2|333|2|333|00|1111|2'
[int(i) for i in result.split('|')]

# -----------------------------------------------------------------------------
"""
Problem 4
Maze game - using recursion

@08/05/2017
"""

def valid(grid, row, column):
    # check if it can go through
    # for 2D array, len(arr) --> number of rows, len(arr[0]) --> number of columns
    return (row >= 0 and row < len(grid) and column >= 0 and column < len(grid[0]) and grid[row][column] == 1)
    
def walk(grid, x, y):
    # this means it goes to the exit, 2 <-- path
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        print('We make it...')
        print(grid)
        grid[x][y] = 2
        return True
    
    if valid(grid, x, y):
        grid[x][y] = 2
        
        # recursive
        # if there is a path in all four directions...
        # if there it is, set the value at grid to 2, otherwise set it to 1
        if walk(grid, x, y + 1) or walk(grid, x - 1, y) or walk(grid, x, y - 1) or walk(grid, x + 1, y):
            return True
        else:
            grid[x][y] = 1
            return False
    else:
        return False

def main():
    # 1 <-- connect, 0 <-- wall
    grid = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    print(walk(grid, 0, 0))
    
if __name__ == "__main__":
    main()

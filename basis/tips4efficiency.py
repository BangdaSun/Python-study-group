### Efficient way to improve python code

#   1. exchange value of two, without temporary variable
x = 1
y = 4
x, y = y, x

#   2. get index when iterate list
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, '===>', colors)

#   3. concatenate strings
info = ['bangda', 'is', 'student', 'of', 'columbia university']

print(' '.join(info))

### 4. using list/dictionary comprehension rather than for loop

### 5. list: like array list in java - search is more efficient than update
#   in data structure we have doubly linked list
from collections import deque
names = deque(['one', 'two', 'three', 'four', 'five', 'six'])
names.popleft()  # removeFirst
names.appendleft('zero')  # addFirst

### 6. iterate dictionary (for large dictionary)
mydict = {'monday' : 17, 'tuesday' : 18, 'wednesday' : 16, 'thursday' : 20}
for k, v in mydict.iteritems():
    print(k, '==>', v)
    
### 7. concatenate boolean operator
n = 10
result = 1 < n < 20
print(result)

### 8. cond-assgin
num = 20
result = 'even' if num % 2 == 0 else 'odd'
result    

### 9. multiple line of string
myquery = ("select * "
           "from optContract "
           "where opraRoot = 'AAPL'")  # notice the whitespace at the end of each line
myquery

### 10. check object
lst = [1, 2, 3]
print(dir(lst))

### 11. check the memory usage of object
import sys
x = 1
print(sys.getsizeof(x))

y = 'bangda'
print(sys.getsizeof(y))

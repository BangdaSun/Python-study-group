"""
    Dictionary in python
    with key => value
"""
### Create dictionary
#   1. direct way
temperature = {
    'monday'    : 17,
    'tuesday'   : 16,
    'wednesday' : 18,
    'thursday'  : 23,
    'friday'    : 24,
    'saturday'  : 22,
    'sunday'    : 21
}

#   2. using tuple
label = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday',
        'sunday']
tem = [17, 16, 18, 23, 24, 22, 21]
temperature = dict(zip(label, tem))

### Access element
temperature.keys()  # get the keys
temperature.values()  # get the values
temperature.items()  # get the key - value pairs
temperature.get('monday') # access using .get() method
temperature['friday']  # access using key

### Manipulation
#   expand
temperature['monday'] = 18  # add new key and value

#   remove
temperature.pop('monday')  # remove specified element (removed element will be returned)
temperature.popitem()  # remove one by one
del temperature['monday']

#   update
temperature['monday'] = 19

### List comprehension
[key + ' => '+ str(value) for key, value in temperature.items()]

# A Python program to show different
# ways to create Counter
from collections import Counter
from copy import copy

# With sequence of items copy Module
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
               'B', 'A', 'C']))

print(copy(10))

# With pprint Module
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)


pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)


tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)


# with enum module
from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4

# printing enum member as string
print(Season.SPRING)

# printing name of enum member using "name" keyword
print(Season.SPRING.name)

# printing value of enum member using "value" keyword
print(Season.SPRING.value)

# printing the type of enum member using type()
print(type(Season.SPRING))

# printing enum member as repr
print(repr(Season.SPRING))

# printing all enum member using "list" keyword
print(list(Season))


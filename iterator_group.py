from sys import argv
from itertools import cycle

_, *number = argv

c = cycle(number)
[print(next(c)) for x in range(3*len(number))]

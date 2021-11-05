from sys import argv

_, number = argv

start = int(number)
[print(x) for x in range(start, start + 10)]

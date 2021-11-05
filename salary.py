from sys import argv

_, hours, rate, prize = argv

print((float(hours) * float(rate)) + float(prize))

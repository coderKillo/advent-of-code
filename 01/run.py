import re
import math

print("Begin")

#read file

with open('input', 'r') as reader:
    x = map(int, reader.readlines())
    x = map(lambda x: math.floor(x/3) - 2, x)
    x = map(int, x)
    x = sum(x)

print("End")
f = open("output", "w")
f.write("Answer part 1: {}".format(x))

def part2Calc(x):
    res = math.floor(x/3) - 2
    if(res <= 0):
        return 0
    else:
        res += part2Calc(res)
        return res

with open('input', 'r') as reader:
    x = map(int, reader.readlines())
    x = map(part2Calc, x)
    x = map(int, x)
    x = sum(x)

f = open("output", "a")
f.write("Answer part 2: {}".format(x))



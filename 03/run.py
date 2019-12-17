
import math
from itertools import product

#function
def part1Calc(x):
    pass

def part2Calc(x):
    pass

def message(x):
    print(">>>> {}".format(x))

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:{} y:{}".format(self.x, self.y)

class WirePlan:
    def __init__(self, w, h):
        self.plan = [[0 for x in range(w)] for y in range(h)]
        self.mid = Point(int(w/2), int(h/2))
        self.ptr = self.mid
        self.intersections = []

    def add_wire(self, wire):
        for c in wire:
            if c[0] == 'R':
                self.moveRightBy(int(c[1:]))
            elif c[0] == 'L':
                self.moveLeftBy(int(c[1:]))
            elif c[0] == 'D':
                self.moveDownBy(int(c[1:]))
            elif c[0] == 'U':
                self.moveUpBy(int(c[1:]))

    def moveLeftBy(self, x):
        for i in range(x):
            self.move(-1, 0)

    def moveRightBy(self, x):
        for i in range(x):
            self.move(1, 0)

    def moveUpBy(self, x):
        for i in range(x):
            self.move(0, 1)

    def moveDownBy(self, x):
        for i in range(x):
            self.move(0, -1)

    def move(self, x, y):
        self.ptr.x += x
        self.ptr.y += y
        self.markSpot()

    def markSpot(self):
        if self.checkIntersection():
            self.intersections.append(self.ptr)
        self.plan[self.ptr.x][self.ptr.y] = 1

    def checkIntersection(self):
        return self.plan[self.ptr.x][self.ptr.y] >= 1


#read input and format
print("Read Input")
with open('input', 'r') as reader:
    in1 = reader.read()
    in1 = in1.split('\n')
    in1 = map(lambda x: x.split(','), in1)
    del in1[2]

#init variable
out1 = 0
out2 = 0

#test
print("Test Begin")

p = WirePlan(11,10)
p.ptr.x = 1
p.ptr.y = 1

print(p.ptr)
p.move(1,0)
print(p.ptr)


print("Test End")

#do the math

wireplan = WirePlan(5000, 5000)

# write output
output = """
Answer part 1: {}
Answer part 2: {}
""".format(out1, out2)

print("Output is:")
print(output)
f = open("output", "w")
f.write(output)




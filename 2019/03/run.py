import copy
import math

#function
def message(x):
    print(">>>> {}".format(x))

def command(str):
    return str[0], int(str[1:])

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:{} y:{}".format(self.x, self.y)
    
    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return self.__add__(-other)
    
    def manhatten(self, other):
        diff = self - other
        return abs(diff.x) + abs(diff.y)

class WirePlan:
    def __init__(self, wires):
        self.ptr = Point(0, 0)
        self.c_port = Point(0, 0)
        w, h = self.calculatePlanSize(wires)

        message("create_plan {}x{}".format(w,h))
        self.plan = WirePlan.create_plan(w,h)
        self.intersections = []
        self.wire_idx = 0
        self.wire_count = 0

        for wire in wires:
            self.ptr = copy.copy(self.c_port)
            self.add_wire(wire)

    def __str__(self):
        plan = ""
        for row in reversed(self.plan):
            for p in row:
                plan += '.' if p.id == 0 else str(p)
                plan += ' '
            plan += '\n'
        return plan
    
    @staticmethod
    def create_plan(w, h):
        return [[0 for x in range(w + 1)] for y in range(h + 1)]
    
    def get_field_id(self, point):
        return self.plan[point.y][point.x] >> 56
    
    def get_field_count(self, point):
        return self.plan[point.y][point.x] & (int("00ffffffffffffff", 16))


    def set_field(self, point, id, count):
        old_count = self.get_field_count(point)
        value = id << 56
        value += old_count
        value += count
        self.plan[point.y][point.x] = value


    def add_wire(self, wire):
        self.wire_idx += 1
        self.wire_count = 0
        for c, v in map(command, wire):
            direction = Point()
            if c == 'R':
                direction.x = 1
            elif c == 'L':
                direction.x = -1
            elif c == 'D':
                direction.y = -1
            elif c == 'U':
                direction.y = 1
            
            for i in range(v):
                self.wire_count += 1
                self.move(direction)

    def move(self, abs_pos):
        self.ptr += abs_pos

        if self.checkIntersection():
            self.intersections.append(copy.copy(self.ptr))
        self.set_field(self.ptr, self.wire_idx, self.wire_count)

    def checkIntersection(self):
        value = self.get_field_id(self.ptr)
        return value > 0 and value != self.wire_idx

    def calculatePlanSize(self, wires):
        max_x = min_x = max_y = min_y = 0
        for wire in wires:
            x = y = 0
            for c, v in map(command, wire):
                if c == 'R':
                    x += v
                elif c == 'L':
                    x -= v
                elif c == 'U':
                    y += v
                elif c == 'D':
                    y -= v
            
                max_x = max(max_x,x)
                min_x = min(min_x,x)
                max_y = max(max_y,y)
                min_y = min(min_y,y)
        
        self.c_port = Point(-min_x, -min_y)
        return max_x - min_x, max_y - min_y


def load():
    #read input and format
    with open('input', 'r') as reader:
        in1 = reader.read()
        in1 = in1.split('\n')
        in1 = list(map(lambda x: x.split(','), in1))
        del in1[2]
    return in1

def test():
    print("Test Begin")

    wire = ['R20', 'U20', 'L40', 'D10']
    wire2 = ['D10', 'R5', 'U15', 'L10']
    p = WirePlan([wire, wire2])
    print(p)
    print("intersects: {}".format([str(i) for i in p.intersections]))
    print("Test End")


def process1(data):
    plan = WirePlan(data)
    x_ptr = copy.copy(plan.intersections)
    x_ptr = list(map(lambda p: p.manhatten(plan.c_port), x_ptr))

    return min(x_ptr) 

def process2(data):
    plan = WirePlan(data)
    x_ptr = copy.copy(plan.intersections)
    x_ptr = list(map(plan.get_field_count, x_ptr))

    return min(x_ptr)

def result(r1, r2):
    output = """
    Answer part 1: {}
    Answer part 2: {}
    """.format(r1, r2)

    # to console
    print("Output is:")
    print(output)

    # to file
    f = open("output", "w")
    f.write(output)

if __name__ == "__main__":
    message("Read Input")
    data = load()
    message("Read Input DONE")

    message("Calculate Answer 1")
    out1 = process1(data)
    message("Calculate Answer 1 DONE")

    message("Calculate Answer 2")
    out2 = process2(data)
    message("Calculate Answer 2 DONE")

    message("Print Ouput")
    result(out1, out2)
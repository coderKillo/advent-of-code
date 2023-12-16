import re
import math

#function
def part1Calc(x):
    pass

def part2Calc(x):
    pass

class Computer:
    def __init__(self, c):
         self.code = list(c)
         self.head = 0

    def start(self):
        while self.execute(self.readNext()) == 0:
            pass

    def execute(self, instruct):
        if Computer.optType(instruct) == 1:
            self.addFunc(instruct)
            self.head += 4
            return 0

        elif Computer.optType(instruct) == 2:
            self.multiFunc(instruct)
            self.head += 4
            return 0

        elif Computer.optType(instruct) == 99:
            return 1

        elif Computer.optType(instruct) == 98:
            print("Error Out of Memory")
            return 1

        else:
            print("Unkown Instruction")
            return 1

    @staticmethod
    def optType(instruction):
        return instruction[0]


    def addFunc(self, ins):
        p_sum1 = ins[1]
        p_sum2 = ins[2]
        p_out = ins[3]
        self.code[p_out] = self.code[p_sum1] + self.code[p_sum2]

    def multiFunc(self, ins):
        p_fac1 = ins[1]
        p_fac2 = ins[2]
        p_out = ins[3]
        self.code[p_out] = self.code[p_fac1] * self.code[p_fac2]

    def readNext(self):
        return self.code[self.head:self.head+4] if self.head < len(self.code) else [98]

def message(x):
    print(">>>> {}".format(x))

#read input and format
print("Read Input")
with open('input', 'r') as reader:
    in1 = reader.read()
    in1 = in1.split(',')
    in1 = map(int, in1)

#init variable
out1 = 0
out2 = 0

#test
print("Test Begin")
test = [10, 20, 30, 40, 50, 60, 70, 80]
c = Computer([1,0,0,0])
c.addFunc(c.readNext())
print(c.code)
for r in range(10):
    print(r)
print("Test End")

#do the math
pos = 0
com = Computer(in1)
com.code[1] = 12
com.code[2] = 2
com.start()

out1 = com.code[0]

for noun in range(100):
    for verb in range(100):
        com2 = Computer(in1)
        com2.code[1] = noun
        com2.code[2] = verb
        com2.start()
        if com2.code[0] == 19690720:
            print("found at noun:{} and verb:{}".format(noun, verb))
            out2 = 100 * noun + verb
            break



# write output
output = """
Answer part 1: {}
Answer part 2: {}
""".format(out1, out2)

print("Output is:")
print(output)
f = open("output", "w")
f.write(output)




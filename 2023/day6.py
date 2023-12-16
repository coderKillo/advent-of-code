import math
import cmath

def calculate_ways_to_win(time, distance):

    p = time
    q = distance

    # find two solutions
    sol1 = p/2 + math.sqrt(p**2/4 - q)
    sol2 = p/2 - math.sqrt(p**2/4 - q)

    # transform the solutions to real numbers
    # we want a travel distance greater then the track distance

    # because of that we take the next lower number vom the maximum
    # we also subtract a small amount to prevent cases where sol1 is already a real number
    max = int(sol1 - 0.0001)
    # and the next greater number from the minimum
    min = int(sol2) + 1

    print(min, max)

    # to get the number of possible wins we count how many hole numbers are between the min and max
    # in other words the diff and add +1 because it is inclusive
    return (max - min) + 1



# input = [(52 ,426),(94, 1374),(75,1279),(94,1216)]
input = [(52947594, 426137412791216)]
# input = [(7,9),(15, 40),(30,200)]
result = 1

for time, distance in input:
    result *= calculate_ways_to_win(time, distance)

print(result)
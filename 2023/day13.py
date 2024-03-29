from collections import Counter
from itertools import chain

T1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

T2 = """#....#.
#....##
.####..
.####..
#....##
#.##.#.
.####.#

.#...####.##..#
..#.###...#.##.
..#.###...#.##.
.#...####.##..#
.####..##.##..#
.####.#.###.##.
####..#.#######
#.......####..#
####.#.#.......
..#....##.#####
.##.##...##.###
..#.#.#.##.....
.....##.#..####
##..#.###..####
.##..#...######

..#..#.
#....#.
...##..
.##.#..
.####..
..#.#.#
....###
#..#.#.
#..#.#.
....###
..#.#.#
.####..
.##.#..

##.###...#.##
##.###...#.##
###.#####..##
##....#.##.##
#....#.#.####
.#....###....
#....#...####
.##.##.####..
..#.##.###.#.

#.#...#...##...##
#.#...#...##...##
#....##....#.....
##...##...##.##..
#..##..####....##
.....#.##..#.###.
#.......###..#...
..####.#.#.###..#
#..###.#.#.#####.
.....#.###....###
.....#.####...###

##....##.
##.##.###
.#.##.#.#
..#..#..#
........#
........#
..#..#..#
.#.##.#.#
##.##.###
##....##.
.##..#...

##..#..
...####
..#...#
..###..
##.####
##.#.#.
......#
....#.#
##.#.#.

##.#.##.#
...#..#..
.##...#..
.##...#..
.#.#..#..
##.#.##.#
.#...####
..#.#..##
...#...##
.#....#.#
.#....#.#

#.######.#..###
.#..##....#..##
####..####.##..
###.##.####....
####..#######..
.#......#.#.#..
.#......#..#...
#..#..#..#...##
#.#.##.#.##.###

.......##
#####.#..
#..##.#..
#######.#
....#####
.##......
####.#...
######.##
.....####
#..#.#...
.##.#..##

#.######.#.#.
##.##.###...#
#.....#....##
.#.......###.
.#.......###.
##....#....##
##.##.###...#
#.######.#.#.
#.#.##.#.#.##
..#.########.
..#.########.
#.#.##.#.#.##
#.######.#.#.

#.#.##.
..##..#
.#.##..
#..##.#
#...#.#
....##.
.#..##.
..#.#.#
..#.#.#
.#..##.
....##.
#...#.#
#..##.#

...#..#.##..#
..#.#..#.####
..#.#..#.####
...#..#.##..#
###..#..###..
...##....####
##..#..####..
##..#.##....#
#..#..#.#.#.#
##...#..#...#
...###..#.###

.##..#.##
##.###.##
##.###...
##..#.###
..#.#..##
##.###...
...######
###..####
..#...#..
..#....##
..####.##

......###..##
###.######.#.
..###...#..##
...##..#.....
...##.##.####
###..#.##.#.#
###..#.##.#.#
...##.##.####
...##..#....#
..###...#..##
###.######.#.

#..#.####
.#.#.###.
.###.###.
#..#.####
#...#...#
#...#...#
#..#.####

#.#...##.
##.##....
..#.##..#
..#.#.##.
#.##.#.##
###.##..#
####.....
##..#....
##.##....
##.##....
##..#....
####.....
###.##..#

#.#.#.##.
...#.#.##
...###.##
#.#.#.##.
#####..##
.#..##..#
####.#.##
....#.##.
.#...#.#.
.####.#.#
#..#.#.#.
..######.
..#..#...
#.#.#####
#.#.#####

.#.######
#...#....
#....####
#....####
#...#....
.#.######
##...#..#
###..#...
#.#.#####
..#.#....
.#.#..##.
.##.#....
.####.##.
#.##.####
#..######

###....###...
...#..#....#.
..........###
.###..###.#.#
...#..#...###
###.##.####..
###.##.###..#
#.#....#.#.#.
...####.....#
##......####.
##......##.#.
#.#.##.#.##..
#.##..##.#.##
#.#....#.#.##
#.#.##.#.##..
##......##.#.
##......####.

#...#.##..###
.#.#####.####
#..#..#######
#....##..#.##
.#.###..##.##
.##...##.....
.##.####.####
.##.####.####
.##...##.....
.#.###..##.##
##...##..#.##
#..#..#######
.#.#####.####

..#..####
#...#..#.
..#.##.#.
.#####...
#.##....#
#.##....#
.#####...
..#.##.#.
#...#..#.
..#..####
..##.####

.#.#.#..##.##
.#.####.....#
..##......#..
###.#..##..##
###.#..##..##
..##.#....#..
.#.####.....#
.#.#.#..##.##
.#.#.#..##.##

....#...###....##
.#.#..##..##..###
.#.#..##..##..###
....#...####...##
####.#..#...##...
......#.#..##...#
#....##.#.##...##
#..####.#....##.#
#..####.#....##.#
#....##.#.##...##
......#.#..##...#

#.#.#.#.##.##
#.#.#.#.##.##
.#..#.#.##.##
####.##.#...#
.###.##..###.
.###.#.#.##.#
#......##.##.
.##.#..###.##
####....####.
####....####.
.##....###.##
#......##.##.
.###.#.#.##.#

######.......
######.......
......#######
#####.##.#..#
####..#..#.##
##..##..#####
##..#####.###
#..#...##.#..
.###.##..#.##

#....##..
#######.#
#....#.##
.#..#..#.
##..##.#.
##..###..
##..###..
#....###.
......#.#
##..##...
##..##...
......#.#
#....#.#.

.........####
#..##..#.#...
.........#...
........##...
.#.##.#..####
#......######
#.####.#.####
.#....#.#.#..
...##....##..
#.#..#.##..##
#..##..#.....
.........#...
..#..#.......
.######.##.##
##....#.#....

....########.....
#..##......##..#.
#..##......##..#.
....########.....
..#.#..##..#.#..#
###.#......#.###.
#..#.##..##.#..#.
.....#...##......
#...###..###...#.
...##########...#
......####.......
...#...##...#....
##..########..##.

#..#####..#
###.#######
######.....
....#.#####
........##.
#..#..#.##.
######.#..#

###.###
##.#.#.
##.###.
..##.#.
...#...
####.#.
..#...#
######.
##....#
..####.
##.#...
##.###.
..#####
..##.#.
###..##
###..#.
..##.#.

.#.##.#.#
...#.....
...#.....
.#.##.#.#
.#.#.#..#
..#..#.#.
#..##.##.
.#.#..##.
##.....#.
###.#...#
###.#...#
##.#...#.
.#.#..##.
#..##.##.
..#..#.#.

...#.#..#
###.#####
.#.#.....
###.##..#
.##.#.##.
.#.#.#..#
.#...#..#
###..####
###.#....
###.#....
###..####
.#...#..#
.#.#.#..#
.#..#.##.
###.##..#

..#..#...#.
##....##...
.##..##.#.#
#......#.#.
##....###.#
#.#..#.##.#
.#.##.#..#.
#.####.#..#
#.####.#.##

#.##.##
.#..#..
#.##.##
.####..
..##.##
.####..
##..###
.####..
#....##
.#..#..
..##...

..#.#.#..
#...#..#.
#...#..#.
..#.#.#.#
..#.#.#.#
#...#..#.
#...#..#.
..#.#.#..
.###.....
.####.###
..#.###..
...#.#...
#.##....#
..####...
#####..#.
.#.##.#..
##..##.#.

.###.###..##...##
...####..#.##..#.
..#.#..##...###.#
#..#.##..####...#
.#..###...#.##.#.
.##..##.#.##.#.##
.##..##.#.##.#.##
.#..###...#.##.#.
#..#.##..####...#
..#.#..##...###.#
...####..#..#..#.
.###.###..##...##
..####...#..####.
..####...#..####.
.###.###..##...##

..##..###
##..##.#.
#######..
......#..
..##...##
#.##.##.#
......###

#######.#.###.##.
..##....##..#.#..
..##....##..#.#..
#########.###.##.
#..#####........#
.#....###.####...
.....####.##..#..
#..#.#.##...#....
#..#.#.##...#....

########.####..
#......#.#..###
#......#.#..###
########.####..
#.#.#.####..#..
..#...##...####
##...#.#..#.###
#.#.#.#......##
.##....##...###
####..#.##.###.
.#..###.#..#.##

.####....
.#...#.#.
.#...#.#.
.####....
##.#...##
#.##....#
#..#..#..
###..###.
###.###..
#.###.#.#
#.###.#..

##..##.#.
.####.###
#....###.
.......##
#.##.#..#
##..###..
......##.
.####.###
##..##...
#....###.
##..###..
#.##.#..#
#.##.#.##

#.....#..##
#.....#..##
.#.#..###..
..#.#..##.#
..##.######
#...#...#..
#.##.#.....
...###.#...
#.#...#.###
..#.##.#...
#..#.###.##
.##...##...
#.#..##..##
###.#######
..###...#..
..#.##.##..
##..##...##

#..##..
..#.##.
#.#.#..
#.#.#.#
..#.##.
#..##..
.#...#.
.###..#
.###..#

..##....#..##.###
.####....#.##..#.
.####....#.#...#.
..##....#..##.###
.......#.##.#####
.####....#####.##
##..##.###...##..
.......##...#.#.#
##..##..####....#
.####..##.##.####
########......###
.#..#...#.#.###.#
#.##.###.##......
..##...#.##.##...
#.##.##.#.#...#.#

#.#.#.###
..##....#
..#..#...
###.#.##.
.####....
#.####.#.
##.####..
..###.###
..##..###
#..####..
#..####..
..##..###
..###.###

.#.....
#..####
.##.##.
###.###
.....##
.....##
###.###
.##.##.
#..####
.#...#.
.#...#.
#..####
.##.##.

....##....#.##...
#........##......
..#.##.#...#...##
##......##.###.##
##.####.##...####
..##..##......#..
##.#..#..#..#..##
..#....#..###.###
.#......#..##.#..

#..#..###...#
#.#.##.######
#.#.##.######
#..#..###...#
####..#..##..
...#.#.#..##.
#...#.##...##
###.###.##..#
#..##.#...#..
#..##.#...#..
###.###.##..#
#...#.##...##
.#.#.#.#..##.

###.#.####.
####.#####.
##########.
###.#.####.
....#.#.#.#
...#.......
....#.#####
#####.#.##.
##.....###.
....#...#.#
##.#.##.#..
##.....####
..#.#...#.#
##......#..
.....#.#.#.

###....#..##.
####...#..##.
###.......#..
#..##....##..
##.##...#..#.
.#...#.##..#.
.#...####..#.
#...#..##.###
##..######.##
#.##.........
####..##.##.#
###...##.###.
###...##.###.

.#..###..##..
.#..###..##..
###....#....#
...#.####.#..
#.#..###...#.
..#.##.#.##..
..#.#..#.##..
#.#..###...#.
...#.####.#..
###....#....#
.#..###..##..

#..####..##
.########..
.#..##..#..
####..#####
..#....#...
.#.####.#..
#..####..##
#...##...##
.###..###..
.#.#..#.###
.#.####.#..

.#..##.
.#..##.
##.#.##
##.##.#
.....##
#.#.#.#
.#.###.
.#.###.
###.#.#
.....##
##.##.#
##.#.##
.#..##.

#.....#..#.
####.#....#
.##...#..#.
#...#.#..#.
#.###..##..
##.#...##..
###.#..##..
#.#.###..##
###...#..#.
.##.#......
.####......

###.###..##
###.###..##
##.#..##.#.
.#.#.#.#..#
..#....#.##
###.##..#.#
......#####
..###....#.
#.......#..
#.#.#.###..
.#.##.###..
..#.#....##
###..###...
#...##.##.#
#...##..#.#

####..######..#
.###..#.##.#..#
....##..##..##.
#.#....#..#....
..##..#.##.#..#
#.##..#.##.#..#
#...#..#..#..#.
####..##..##..#
.###..######..#

.#.####.#..
.########..
.##.#..##..
#.#....#.##
#..#..#..##
#.#.##.#.##
.###..###..
#.#.##.#.##
..##..##...
.#.#..#.#..
.###..###..

####.##
.#....#
##.#.#.
..##.##
...#.##
#####..
.#.####
.#.####
#####..
...#.##
..##.##

#..####
.###.##
#..##..
#..####
.#...##
.###.##
####.##

.........##....
###..####..####
.#....#..##..#.
.##..##.####.##
.##..##......##
..####...##...#
.######......##
##.##.###..###.
.##..##.#..#.##
#..#...######..
..####........#
.##..##.####.##
.######..##..##

....#.##.##..
#.##.#.......
#..##.#.#.###
.##....###.##
#..###..#...#
....###.#####
#..##....##.#
####.#...####
.##.##...##.#
.##.##...##.#
####.#...####

#......##
.#.######
##.#.#...
#.###.###
..#####..
#......##
#......##
..#####..
#.###.###
##.#.#...
.#.######
#....#.##
##.#.####

###....#.
#..####.#
....##.##
.##.##.#.
.##.#...#
.##....##
.......#.
.......##
.##.##...
####...#.
.##.#.#..
.##..###.
.##..###.

#.##..#..#.
....###..##
#.#....##..
##.##..##..
##.#.#....#
..#...####.
..#...####.
##.#.#....#
##.##..##..
#.#....##..
....###..##
#.##..#..#.
.#.##.#####
#....##..##
..#.###..##

..#..##.#
....####.
...#...#.
#..##..#.
.#.##...#
#.#.#....
#...#.###
#..##.###
#.#.#....
..##.##..
....#####
....#####
..##.##..
#.#.#....
#..##.###
#...#.###
#.#.#....

##########...
###...#..#...
###.#.#..#...
##########...
##.#######.##
##.....#...#.
#####..#..##.
##.###.......
...#..##.#..#
..##...##.##.
####.#.#.##..

####.###..#
####.##.#.#
....###..##
##...#.#.#.
###.#..#..#
###.#..#..#
##...#.###.

..###...##...
...##.######.
##..###....##
...#.#......#
...###......#
##.###.####.#
.#....######.
.....#..##..#
..###########
###.#.######.
###..#......#

###.###.###...##.
##.##.######..##.
.#####..#.#.##..#
.##.#..##.##.####
..##..##.#...####
.###..##.#...####
.##.#..##.##.####
.#####..#.#.##..#
##.##.######..##.

....##.
#.#.#.#
..##...
.#.#.##
.#.#.##
..##...
#.#.#.#
....##.
##..#..
.#..#..
....##.

..###......
.#.##...##.
##.#..###..
##.#..###..
.#.##...##.
..###..#...
..####..#.#
.##...#...#
.##...#...#
..####..#.#
..###..#...
.#.##...##.
##.#..###..

..##..#.#..#.#.
##..#####..####
##..####....###
.#..#..######..
##..####....###
.#..#.########.
##..##........#
..##....####...
#.##.#.#.##.#.#
######.#....#.#
.####....##..#.
.......#....#..
.####.#.#..#.#.

..#...#######
.#..##..####.
....#..#.##.#
.....##.####.
#...##.......
##..##.######
#.#.#....##..
.###.##.#..#.
.##..#.#.##.#
.##..###.##.#
.###.##.#..#.

.###..#...##..###
##...#.#.#....#..
##...#.#.#....#..
.###..#...##..###
#.###..##....#..#
#..##.#######.#.#
..####..#.####...
.#...#.##...##.#.
.#...#.##...##.#.
..####....####...
#..##.#######.#.#
#.###..##....#..#
.###..#...##..###

####.#...
.....####
#######.#
....#...#
.....#.##
....##.##
####.#..#
....#.#.#
.....#...
.....###.
......###
.##...#.#
....#..##

##.#.######.#
....#..#..##.
..#####.###.#
###.###..#.##
###.####.####
..#.##.#..#.#
#####...#..##
####.#....#.#
###..#....#.#
#####...#..##
..#.##.#..#.#
###.####.####
###.###..#.##

.#.#..##..#.#..
..###.....##...
...###..###....
#.##......##.##
.##........##..
.#...#..#...#..
####.#..#.#####
##.###..###.###
.#.#.#..#.#.#..
.#.#.####.#.#..
....######.....
.###..##..###..
##..#.##.#..###
.##.######.##..
.#..........#..
##..######..###
.#..........#..

#.....#.###..
..##..##...#.
###.##.#..#..
.#.###.####.#
.#.###.######
.#.###.######
.#.###.####.#

##.##....##
##.##....##
#.###....##
##..#.##.#.
#.###.#####
.#.#.#..#.#
#.##.####.#
..##.#..#.#
###.##..##.
#...######.
##..#.##.#.
#....####..
....#....#.
.#.#..##..#
#...#....#.

#..####
#...###
.#..#..
#....##
.#.....
.##..##
..#.#..
.....##
#.##.##
.#.##..
.#.####
#....##
#..#...

##...#...
.###.##.#
#.###.#.#
###..####
###..####
#.###.#.#
.###.##.#
###..#...
###..#...
.###.##.#
#.###.#.#

....####..###
...#####..###
.#.#..######.
...##..#..#..
#.#####....##
#.....##..##.
#....########
.#.#....##...
....##..##..#
.##...######.
#.##.#.#..#.#
......######.
#...#...##...

##.#.#.#...
..#.###..##
##....#..##
#.#.##.##..
#.#.##.##..
##....#..##
..#.###..##
##.#.#.#...
.......###.
.......###.
.#.#.#.#...
..#.###..##
##....#..##

##.#..#
###...#
#...##.
##.....
..#....
.##....
##.####
##.####
.##....
..#....
##.....

#..##..##..#..#..
#.########.#..#.#
.#...##...#.##.#.
..###..###......#
.###.##.###.##.##
.#.######.#.##.#.
##..#..#..######.
.###.##.###.##.##
.#..#..#..#.##.#.
.#..####..#.##.#.
...#....#........
....#..#.........
....#..#.........
..##.....#......#
.#.#.##.#.#.##.#.
#.#..##..#.####.#
###..##..###..###

##.##.#######
..#.....#..#.
#.###....##.#
.##.###......
..#.###.#..#.
..#.###.#..#.
.##.###......

##..#..##..
###.#.#..#.
#.####....#
.....##..##
#####..##..
....#.#..#.
..##.######
##.##.####.
#.#.#..##..
.####.####.
#.....####.
#...#.####.
.####.####.
#.#.#..##..
##.##.####.

##.###....####.
####.#.###.##.#
.##.###....##..
.##.#.###.#..#.
.....###.######
......#.###..##
.##.##.#.......
#####..####..##
#..#...########
####.######..##
....#..########

..#..#.###..#
.###.#...#..#
..#.###.#####
.##..##.#.##.
.##..##.#.##.
..#.###.#####
.###.....#..#
..#..#.###..#
.#..##....##.
##.##.#...##.
#.##.#...####

..###.#####
.#.########
.#####..#.#
.#....##.#.
.#....##.#.
.#####..#.#
.#.########
#.###.#####
#.###.#####
.#.########
.#####..#.#

.#..#.#.#
......##.
##..##.#.
##..##...
......##.
.#..#.#.#
##..##..#
##..###..
######.##
#######..
#.##.###.

.######
#......
#......
.##..##
.##..##
#......
#.#..#.

.#.....
#.....#
..##.#.
#.##...
..####.
#.#.#..
#.#.#..
..####.
#.##...
..##.#.
#.....#
.#.....
...#...
...##..
#......
#......
.#.##..

.....#.
#.##...
#.##...
..#..#.
..#..#.
#.##...
#.##...
.....#.
##..#.#

...##....
#.#..##..
#..###.##
###......
.#..#..##
#....#...
.##.#####
..#......
.#.....##
#.#..#.##
..##.####
..###.###
..#.#.###

.##..#.###.##
.##..#.###.##
.#...#..##.##
...#.#.#.##..
#..####.#...#
#.##.#...##..
.##.#.#..#.#.
....#.#####..
#.##.###...#.
..###.#####.#
..###.#####.#
#.##.###...#.
....#.#####.#

.##.##.#.###.
#..##.##..#.#
#.#######.##.
.....#..###..
.#######.#.#.
.#####.#.#.#.
.....#..###..
#.#######.##.
#..##.##..#.#
.##.##.#.###.
##.#.###.####
##.#.###.####
.##.##.#.###.

###..###.
.#....#..
.#....#.#
.#....#.#
.#....#..
###..###.
.#....#..
##.##.###
...##....
########.
#.####.##
#.####.##
.######.#
..####...
.#.##.#.#
#......#.
..#####..

..#..#..###
#.#.#...###
#.#.#...###
..#..#..###
#...#..##..
#..##.#....
.#.###.#.##
#.....#....
##.##.##..#
#..##.##..#
#.....#...."""


def equal_list(a: list, b: list) -> bool:
    return a[:len(b)] == b[:len(a)]

# return a list of possible symmetries per row
def find_vertical_symmetry(pattern) -> list[list[int]]:
    result = []
    for row in pattern:
        possible_symmetry = []
        for symmetry_axis in range(1,len(pattern[0])):
            left_side = list(reversed(row[:symmetry_axis]))
            right_side = row[symmetry_axis:]
            if equal_list(left_side, right_side):
                    possible_symmetry.append(symmetry_axis)
        result.append(possible_symmetry)
    
    return result

def find_horizontal_symmetry(pattern) -> int:
    # swap pattern col and row
    swapped_pattern = [list(x) for x in zip(*pattern)]
    return find_vertical_symmetry(swapped_pattern)

def read_input(input: str):
    patterns = []
    pattern = []
    for line in input.splitlines():
        if line == "":
            patterns.append(pattern)
            pattern = []
            continue
        pattern.append([1 if char == "#" else 0 for char in line])
    patterns.append(pattern)
    return patterns

def main(patterns):
    result = 0
    for pattern in patterns:
        v_symmetry = find_vertical_symmetry(pattern)
        h_symmetry = find_horizontal_symmetry(pattern)

        width = len(pattern)
        height = len(pattern[0])

        v_counter = Counter(list(chain.from_iterable(v_symmetry)))
        h_counter = Counter(list(chain.from_iterable(h_symmetry)))

        v_common = v_counter.most_common(2)
        h_common = h_counter.most_common(2)

        if v_common[0][1] == width:
            v_common = [v_common[1]]
        if h_common[0][1] == height:
            h_common = [h_common[1]]

        if v_common[0][1] == (width -1):
            result += v_common[0][0]
        if h_common[0][1] == (height -1):
            result += 100 * h_common[0][0]

    print(result)


main(read_input(T2))
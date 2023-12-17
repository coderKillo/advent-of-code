from typing import List
from util.Matix import Matrix
import numpy as np

platform = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

platform2 = """...###.#OO..#.O......#...#...O..#.....#...O#..O#........O.#O#O..O.....O.......#O.............O#.O###
O.OOO..##O....#O.O.OO#......O...#O.........O....O..OO....#OOO.#..#..........O.O...##...#........O..#
.#..O..O.#.....O...O.....#O.OOOO..O.#.O#OO.........O.#.O#O.O.#...O#..........OOO.#...#..O#..####O.OO
.#..O....#.#..O.....O..O......O......O.O.O.#..O..#.OO.O.OOO..O#.O.##...OO.#.#.O..#...####O..#..#O...
.##.O......#.OO.O.O...O.....##O.#.#.......##.O....O...O.O.####...#.....O#.O....#O.#..O......O.......
O.###.#.#.O.O........#O.#.#..O#.#.OO....#O....O..##.#O.#.O.###.#..#..#.#.O....#..O......OO.#OO#...O#
.....O..O#..O.O...O....#O#.O.#O...O##OO.O.#O....#.#.....#..O#...#..##....#.OOO..#O.....#..#O#OO.O...
#............O#O.#.#.....O.O..OO....#....#..OO#.#O.OOO..#O...O#.....#.O....O.O..#....O..#...#OO#....
..#.#O#..OO.O...##..#......#OO.....#.#.#.....#.O.....O.......#.##.......#O..OOO...........O.....O.O.
......O#O......OO#..O.#O..O..#....O..O.........O...#.#.##.O....O..O..O..O#.O.O.OOOOO....O#.O.......#
O##...O#...#..#.O.....#.O.###.O......#..#..O.#.O..........O..#.O.......#O......#.O.##....#.#.#...#..
#..#.O..#..........#.O.#.O....#O#...OOOO......#...#.O.....O.OO.O....#.......O.O....O.O#.#O.###O.OO.#
OO.O#.O.......#.OO##....#O.#.O...O..#O.OO.....O..O#..##.O#...O...O.#.#O..O..O#........OO#.....O#..##
......O....O...#O##....OOO..O.O..O.......OO#O....###..O..##...O#.#.O.O..O.OO##....O.O#..O.#.#O#.#...
..O....#.....O..O.OO#..#.##..........#OO...#..#.O...O.O#...#....O.O..O...O....OO...O..OO#O....O..#O.
O....OO............O#.#........#..O.O...#OOO#.............#...OO......O#......O..O....OO...O..O...O.
...O##O.#..........O.O..##....O.##....O...#......O.O...O..O.O..O.##.#..#..O.O#.O.##..O..OO...OO.....
#.O#.#....#....O..O.O.O.###..O.O......O...OO#..........OO.....#O..#........#..#..O.#...##OO.#O#.#.#.
.##OO#...#O....O.O.#.#O....O.#...OO.....O...O.#.....O.OO.O..OO.....O...#..#.....#..#.....#..OOO..O##
.O#.........O.#..O.O.....O#.O##.##......OO.O.#......#...O##.O..#.....O...................#...O..O.#.
..###...#O...O#..#......OO#...##.#.O....#.##OO.....O..O......O#.O....O.#..O#.O#O.#.#O..##.O...O..O.#
.........#O...#..O.##.OO.....#...#.....O.O.O....O..##.O.....##OOO..#..O.#....#.##..O..##.O..#...#.#O
.O..#.#.O#..#OOOO#...#.O..#O#....OO....O..O..#...O..#...#........#O.O...#....O.#...#..#....O..OOOO.O
....#.#O#.O.O.O.OO.#....OO.....O.#....#...#..........#.##...##.OO#..OO.....O.....O#..O.#.....OO..#..
.....OOOOO...O.........#.#....#..OO##.##.....#O....O..##..O.......#.....#.O.....#..O..OO.........O..
...#.#.O###..#...O....OO....O.#.O.....##OO.O#..#.##....O.....OO##...O#OO..O.OO...O.OO..O#..O#.O..#.#
..OOO.OO...##O.O.O#.O...O..O#..OOO...##.#..#.#.#...O.#O#...O#O.OOO.O.OO.O..#.OOOO#.........#..OO...O
O...O#.O.OO#.OO.##.....#....#...#.........###.O.#.........O......#OO..O...OO.#O..#..#..O..O..##....#
O.OOO#....O..O#O....O...O.#......##O...OO..O.............#.#....O#..#O.#OO.O...OO...OOO...O.O.....O.
..#..O.OOO.....O#....#.#..O.......O...#.......#.OO..O.....#.#.#..O....#.#...O.O....O.#.......#.O##..
.#..O.....#.#..#.#.#..OO.O...O........OO#.O..O..#..O#.##O..#....#....OO.....#..#O.........#.O..O.O.O
...O.##OO.#.......O...O.O.#.O.O..#.O...O.O..OO..O..#..OO..##....##.#.....#.O.#..........O.#.OOO#O...
...O..O....##...#...O#.O....O.O...#OO..O.#OO#........#O...OO.#..OO.#O.O..#....O#.O....O#......O#...#
..OO#O.O...#..#.#.......O.O...##....O..#.##..#...#...O...#.O#O.O....O......#....#...O..##..#O..O....
.O...##O.#O.....O........O...O#....##......##....O.....##.....##......O....O..#..#O.#.O.OO#O#O....##
.........#O.O.O.OO..#.O#.##.....#.#O.O..O#.O........O....#O#.##O.#.O....#..OO.O.#...OO.#.O.##O...O##
..O##O.O......#O.O.#..O.#.........O...#..#..#..##OO....O..OO.#.#...OO...#O..#...O.###...O#.#......O.
......O..#O....O##...O##..........O...O....O........O..#OOO...OO..#.....##O.#.O..#....OO....O...#O..
O..#.O..#.O..OOO..O.O.#.O...#O..#.O..#O......O.OO..O.#..O..##.....##....O#OOO..#.#O...O##...OO.#O#.O
O##.O...O.O.....O.#O..O..#.....#O.#.....###..OOO.OO#...#.O..O...........O.....O..#...O.#...#..O....O
...O.OO.....#O..O..#O..#O....OO....O....#O..#OO...O.#...O..#....#....#..OO.O.##.O#O...O.#O...O#.....
.....#...OO.........##OO.#.#........#..O..O.#.#.OO.#..#..#....#.O#..........#..O.O...O.#OO.....##...
#...#.....OO.....OOOO...#..#O.#..##.#..#..O.O##.O#.O#.O.O...#........#...O#......O.O#O..#..#..O...#.
.....O..#.OO.#O.O...#...#..#.......O#.##..OOOO.........OO.O.#O#...OO.#...O....###O..OO#.O.....#.##.O
#O..O#O.#..O#.O.O.O...O...OO...#.##....O#.......OO.O...#.....###.......O..#.O..O...OO#.O.#O.O.O.O.O.
OO.....O.............#.O...OO..##O.O#.#O.#....O..........O..O#.........#.........O#.#....#O#..#..##O
#..#..#........O.OO....O.....O..#O..O#.#O#O...#.##O..O...O.#O.#OOOO#.OO.#..OO##..#O.#.O.O...O..O#...
...#........O...O.O..O.O#.....#....O.#.#OO.#...#..O#O.##..#.##...O#.#.....O..O.....#..O#.....O......
..O.O.O###..#..O.#..#........O..O#..##O#....#...#.....O.......OO...O....##......#.O..O..O.O.O.O..#O.
..O..O..OOO.O##..O..O#..OO###.#....O..O...##..OOO...O.......#..#..OO..O...OO#.O.....O.O..O.OO.#....O
O....O...#.O#O#....#.O....##...O.........O...#.#.#O.OO..O#....O.##.....#.#..#..#....#.#O..O.O.#..O..
O................O#O.O......##..#O...O....O#.O..#....O......O.#..O....O.#...O.....O##.#.O....OOO.#.#
...O#....#..O.O........O#.O#.#O.#.....#....O#....#..#......O.....#.....O#O..O..OO.#.#OOO#O.O.O#.....
.#.#O..##.O.O.O#...O...#...#....O..OO..O..#..#....###.O#.OO.O....O....OOO...O....OOO#..#..O.....#.OO
...OOO..O.O.....O#.##O#.#.#.O..#O.....#O....O#O...O....O#.O#..O#.O..#.#.#O..O..O.#....O.....#O.....#
.O#...#...O.....O..#.O.#.....O...O#..#.....O.O#O..O.....#.#.O..O..#.OO..#O...O......#OOO..#.O..O..#.
O.#.OO.#.O#O#...O....#...###OO..OOO.#O..O.O..O........##...O#...#...O##OO.O#....O.#O.O..O#.O..O.#..O
...#...O.O.###.O#O......#.OOOO...O...##..#O.#.O.#O.###.#O....#.OO....O......#..OO.O.#.O...O.O....O..
...O#.O..#......#...O#...O......O..........O..#..##...O.O....OO.O.#..#....#...#.#O.....#O.#O.....#.#
....#........O#.O..##OO.O....##.O...OOO.....OOO#O.#..#.#.....#.O.#......##..........OO.O#..O....#.O.
#.....O...OOO..##....OO..OO.##......O.O#...#...O...O.....O.OO.O.......OOO....#...O.##.....OO..O.....
.#.O....O..OO....O.O#O...#OO#.#....#....OOO....#O#...#...................O.#O#.O.#....O...#...#O.#.#
O...##O.#.O#....O....#O#.#.#.OO#...............#.##O...#.OO....OO...O....O#O...#.O...O..O.#.O.#...O#
.O.#........O.#..O.O#...#.....#.......#O..OO...O..O....#....O..#..O#.O....#OOO#O....#.#.#O......O.O#
.O.OOO.#O.#......O..#...........#.O.##OOOO##O.OOO#.......#....#...O..#..#..O...##.O.O.....O..#.O....
.O..#..O..OO.#O.#O.OOO...#....#.#.O.#....OO...O....O..##...O#####O....#......O.#.#...O.#O.#O....O..O
O..#OO#....O.....O..#O..O....#O.#OOO.#..#.O#.#.O....O.#...O....O.#.O..#O.OO....#.O.#..#OO...O.O.O#.O
....#.#OO.....O...OO.#O.OO......#..###O#.#.........#O...#..O#..O.OO#OO#O.O..O#..#.#..O#.##...OOO....
............OOO.O..#OO..O#......#..O...#....#O.....#O.....O.....OO#..OO#..O..#..O...O.O..#.##..#.#..
..#.O.#.O.#.OO#...O.O.#O#O...OO.O..#O....O.OOO.#O.#.#.###.O...OO...........O......O..O.OO.O..#....O.
......O.#O#..................OOO..##.O#.....O.O...#.O#....OOO.#.....O.#O...O.#OO.#..OOO.............
O...O................O.....OO.O.#...#..OO....O.OO.O##O.....O...O..#....O...OOO#O......O........#O...
.#O..###.O.##O......#.....#....O....#O..#......#.#O#O..O...O#.......#O....##..##OO.O.O#...OO.O##.O..
.#..#.......O.....#O........O.#..O....O#...........O...#....O.#O#....O..#..OO..O##....OO...#.O....OO
...O#.......OO#....#...O....O..#...##OO..O#..#O#.O.O.OO.OO....O#..##...#.##O..##OO#...#..O..O...O..#
..#..##....O.#.O...O.#.O...##........#...O####...#O...##OO.........O.O..OO#O#.###...O.O....O...OO...
##.#OO.O....#.OOO..O.....O....#O...O...OOO...O#...#....O.#O...#...O.O.#.#OO..O..#.....#O.#....##..#.
......O.O..#.#.O...#........#..O........#O......O....OO.....O.OOO##....O.O..#.#..O#.O.......#.O..#..
O..##.....O........#.#..#.....O....#.##...O.#.....O.OO##...#OO.#...O..O##.OO.#..O..O#.O.O...O..#....
.O....O.##O....O#OOO.#.O..#..O.O....O.O#..##..O#O#.OO....##.O#.....##.....O..##OOO..#.......O...#O..
O...#.O........O.##.....O...OO##....##..O#...O#.O#.#..#.#O..#........#O..#O.O.O.O.O.O....##...#O#.##
.........###OO..O..#....#...............#..O..O.O.###..#OO......O.OO...#...#....O..O..#.#...OO......
.OO.O.O..O...O......O...#...#..O.#...O.#.......O..O.......#.OOO...O..#.....#............O.....OO....
O.OOO.O.#..#...#O...O.#.O#...#.#.#.OO...##...OO.O.O.#......O....O..O..OO....O..##..#.OO...O.#O.#O.##
O..#......#.........#...#O..O.........O#.###..OO.O..OO.O.O.....#O....#O..#...O..O..OO.....O#OOO...#O
....OO...O.#........#......#O#....O.O#....#OO#O.#.O...#........#....OO.........OO.....O.#.......O...
..##..#..O#.....#.O....O..OO##.O.....O#..#O..O...OO..O##.O.OO....O....##O.OOOO#....#...#..O.O...O...
O...#..O##.O..OO.O.O..#.#O.......O#.O.#..O.O...O.OO..#..O.....OO..O....O#O.#.#..#.O..O.......O..#...
OOO...O.#.O....#OO..O......#....O.....O..#O##...O.O.O..OOO#...#....##.OO..##...O....#..#O..##..#....
##.O#O#........#....##.#.OO.#...O.#...##.O...#..##..O#.#.O.#OO....#.O..O..#O....#.....O.O...#O#O.O.O
....#.#O.O#O.OO...O..O#......#.#.O..O..OOO.OOOO...#O..#O..O..O.........O.#....O.#.........##O.....O.
O...#..#O#OO....O#OO#...O..#..#.#.#...O...#...#.....#.#..............O.O...#.O...OO.#..#..........O.
..O.....#OOOO.O.#...O#...#...#..O....O##.#.#..OOOO#OO...O......O..#O..#.O.O..#.#O...O.O.O#.#OOO..OO#
...O......O........##O..#...........OO..#........OO#...#...#....#O........OOO#..O#.O..#..#.O.O...#O.
.OO.#..###..#.O.O#.#...O#O.O.OO...O#....O#O#...#.O.O#.O..O.....##...#.#O.O#O.....#......O#O...##.OO.
.O.##...#O...#.#...O.......#....OOO.....#.O....O..#..O#...O..O..O...O.O..O....#....##...OOO..O#O....
#...#.#OO#.#O.OO#.#....#...O.O#...##.O#O....##..O..#......#.#....#OO#..#O....#O#..OO...O....OO..O...
.OO#.......OO.....#.O...#O....#.....O........OOO.O.O.#.....O......#O#......##OO.#O..O#..........O...
#.#O......O.O......#.#OO........#.O#...#.O.OO.#......O#.O.......O.O.O..#.O#.#.....O...OO#O......O.O.
..O..O.O#.....OO......###.#........O#..#OO.OOO.#..O...#...#..O#.......O.#.##.#.............#O......."""

ROUNDED_ROCK = "O"
SQUARE_ROCK = "#"
EMPTY_SPACE = "."


class Direction:
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


def platform_load_sum(array: np.array) -> int:
    load = 0
    height = len(array)
    for i, n_rocks in enumerate(np.count_nonzero(array == ROUNDED_ROCK,
                                                 axis=1)):
        load += (height - i) * n_rocks
    return load


def move_rocks(row, reverse) -> None:
    last_free_spot = 0 if not reverse else len(row)
    placable = False
    for i, item in enumerate(row[::-1 if reverse else 1]):
        i = i if not reverse else len(row) - 1 - i
        if item == EMPTY_SPACE and not placable:
            placable = True
            last_free_spot = i
        if item == ROUNDED_ROCK and placable:
            row[i], row[last_free_spot] = row[last_free_spot], row[i]
            last_free_spot += 1 if not reverse else -1
        if item == SQUARE_ROCK:
            placable = False


def tilt(direction: Direction, array: np.array):
    if direction == Direction.EAST:
        np.apply_along_axis(move_rocks, axis=1, arr=array, reverse=True)
    elif direction == Direction.SOUTH:
        np.apply_along_axis(move_rocks, axis=0, arr=array, reverse=True)
    elif direction == Direction.WEST:
        np.apply_along_axis(move_rocks, axis=1, arr=array, reverse=False)
    elif direction == Direction.NORTH:
        np.apply_along_axis(move_rocks, axis=0, arr=array, reverse=False)
    else:
        raise ValueError(f"invalid direction: {direction}")


def cycle(array):
    for direction in [
            Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST
    ]:
        tilt(direction, array)


m = np.array([list(line) for line in platform2.splitlines()])

history = []
history_results = []
total = 1000000000
for i in range(total):

    hash_m = "".join(["".join(row) for row in m])
    result = platform_load_sum(m)
    if hash_m in history:
        # cycle detected
        cycle_start = history.index(hash_m)
        cycle_len = i - cycle_start
        end = ((total - cycle_start) % cycle_len) + cycle_start
        print(history_results[end])
        break

    cycle(m)

    history.append(hash_m)
    history_results.append(result)

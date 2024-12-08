import pytest
import os
from day6 import part1

def test_unique_positions_visited_by_guard():
    file_name = write_to_temp_file("""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""")
    unique_positions = part1.get_unique_positions_visited(file_name)
    assert unique_positions == 41

def test_full_input():
    unique_positions = part1.get_unique_positions_visited('advent-of-code/day6/input.txt')
    assert unique_positions == 5199

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
import pytest
import os
from day6 import part2

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
    unique_positions = part2.get_unique_positions_for_patrol_loops(file_name)
    assert unique_positions == 6

def test_full_input():
    unique_positions = part2.get_unique_positions_for_patrol_loops('advent-of-code/day6/input.txt')
    assert unique_positions == 1915

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
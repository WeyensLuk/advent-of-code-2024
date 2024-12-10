import pytest
import os
from day10 import part1

test_data = [
    ("""...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9""", 2),
    ("""..90..9
...1.98
...2..7
6543456
765.987
876....
987....""", 4),
    ("""10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01""", 3),
    ("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""", 36)
]

@pytest.mark.parametrize("topology_map, expected_sum_of_trailheads", test_data)
def test_sum_of_trailhead_scores(topology_map, expected_sum_of_trailheads):
    file_name = write_to_temp_file(topology_map)
    sum_of_trailhead_scores = part1.sum_of_trailhead_scores(file_name)
    assert sum_of_trailhead_scores == expected_sum_of_trailheads

def test_full_input():
    sum_of_trailhead_scores = part1.sum_of_trailhead_scores('advent-of-code/day10/input.txt')
    assert sum_of_trailhead_scores == 496

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
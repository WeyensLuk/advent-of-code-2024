import pytest
import os
from day10 import part2

test_data = [
    (""".....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....""", 3),
    ("""..90..9
...1.98
...2..7
6543456
765.987
876....
987....""", 13),
    ("""012345
123456
234567
345678
4.6789
56789.""", 227),
    ("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""", 81)
]

@pytest.mark.parametrize("topology_map, expected_rating_of_trailheads", test_data)
def test_sum_of_trailhead_ratings(topology_map, expected_rating_of_trailheads):
    file_name = write_to_temp_file(topology_map)
    sum_of_trailhead_ratings = part2.sum_of_trailhead_ratings(file_name)
    assert sum_of_trailhead_ratings == expected_rating_of_trailheads

def test_full_input():
    sum_of_trailhead_ratings = part2.sum_of_trailhead_ratings('advent-of-code/day10/input.txt')
    assert sum_of_trailhead_ratings == 1120

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
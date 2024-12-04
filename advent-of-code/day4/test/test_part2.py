import pytest
import os
from day4 import part2

def test_find_all_matches_of_xmas_in_sample_wordsearch():
    file_name = write_to_temp_file(""".M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........""")
    occurrences = part2.find_all_occurrences_of_crossed_mas(file_name)
    assert occurrences == 9

def test_full_input():
    occurrences = part2.find_all_occurrences_of_crossed_mas('advent-of-code/day4/input.txt')
    assert occurrences == 1950

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
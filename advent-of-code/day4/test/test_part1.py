import pytest
import os
from day4 import part1

def test_find_all_matches_of_xmas_in_sample_wordsearch():
    file_name = write_to_temp_file("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""")
    occurrences = part1.find_all_occurrences_of_xmas(file_name)
    assert occurrences == 18

def test_full_input():
    occurrences = part1.find_all_occurrences_of_xmas('advent-of-code/day4/input.txt')
    assert occurrences == 2593

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
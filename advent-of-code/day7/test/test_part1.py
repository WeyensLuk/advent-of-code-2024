import pytest
import os
from day7 import part1

def test_sum_of_correct_equations():
    file_name = write_to_temp_file("""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""")
    sum_of_correct_equations = part1.get_sum_of_correct_equations(file_name)
    assert sum_of_correct_equations == 3749

def test_full_input():
    sum_of_correct_equations = part1.get_sum_of_correct_equations('advent-of-code/day7/input.txt')
    assert sum_of_correct_equations == 3119088655389

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
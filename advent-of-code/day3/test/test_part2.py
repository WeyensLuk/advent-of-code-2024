import pytest
import os
from day3 import part2

def test_parse_input_takes_only_correctly_formulated_mul_syntax_input():
    file_name = write_to_temp_file("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    sum = part2.calculate_sum_of_enabled_mul_statements(file_name)
    assert sum == 48

def test_full_input():
    sum = part2.calculate_sum_of_enabled_mul_statements('advent-of-code/day3/input.txt')
    assert sum == 88802350

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
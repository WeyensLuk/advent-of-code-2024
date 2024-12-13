import pytest
import os
from day11 import day11

test_data = [
    (0, [1]),
    (1, [2024]),
    (1000, [10, 0])
]

@pytest.mark.parametrize("initial_number, expected_numbers", test_data)
def test_rock_blink(initial_number, expected_numbers):
    stone = day11.Stone(initial_number)
    stones = stone.blink()
    assert [stone.number for stone in stones] == expected_numbers

def test_multiple_rocks_after_one_blink():
    file_name = write_to_temp_file("0 1 10 99 999")
    number_of_stones = day11.number_of_stones_after_blinking(file_name, 1)
    assert number_of_stones == 7

def test_multiple_rocks_after_six_blink():
    file_name = write_to_temp_file("125 17")
    number_of_stones = day11.number_of_stones_after_blinking(file_name, 6)
    assert number_of_stones == 22

def test_multiple_rocks_after_25_blink():
    file_name = write_to_temp_file("125 17")
    number_of_stones = day11.number_of_stones_after_blinking(file_name, 25)
    assert number_of_stones == 55312

def test_full_input_part1():
    number_of_stones = day11.number_of_stones_after_blinking('advent-of-code/day11/input.txt', 25)
    assert number_of_stones == 183435

def test_full_input_part2():
    number_of_stones = day11.number_of_stones_after_blinking('advent-of-code/day11/input.txt', 75)
    assert number_of_stones == 218279375708592

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
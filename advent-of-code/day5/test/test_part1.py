import pytest
import os
from day5 import part1

def test_correct_sequence_from_example():
    file_name = write_to_temp_file("75,47,61,53,29")
    sequences = part1.get_correct_instruction_sequences(file_name)
    assert len(sequences) == 1
    assert sequences == [[75,47,61,53,29]]

def test_wrong_sequence_with_error_at_start():
    file_name = write_to_temp_file("75,97,47,61,53")
    sequences = part1.get_correct_instruction_sequences(file_name)
    assert len(sequences) == 0

def test_wrong_sequence_with_error_at_end():
    file_name = write_to_temp_file("61,13,29")
    sequences = part1.get_correct_instruction_sequences(file_name)
    assert len(sequences) == 0

def test_wrong_sequence_with_multiple_errors():
    file_name = write_to_temp_file("97,13,75,29,47")
    sequences = part1.get_correct_instruction_sequences(file_name)
    assert len(sequences) == 0

def test_sum_of_middle_page_of_all_correct_sequences():
    file_name = write_to_temp_file("""75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""")
    sum = part1.get_sum_of_middle_page_of_correct_instruction_sequences(file_name)
    assert sum == 143

def test_full_input():
    sum = part1.get_sum_of_middle_page_of_correct_instruction_sequences('advent-of-code/day5/input.txt')
    assert sum == 5268

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(page_rules)
    file.write(text)
    file.close
    return os.path.realpath(file.name)

page_rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

"""
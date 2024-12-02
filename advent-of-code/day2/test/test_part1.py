import pytest
from day2 import part1

def test_levels_with_increase_more_than_3_is_unsafe():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/test/unsafe_increase_more_than_3.txt')
    assert safe_report_amount == 0

def test_levels_with_decrease_more_than_3_is_unsafe():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/test/unsafe_decrease_more_than_3.txt')
    assert safe_report_amount == 0

def test_levels_that_first_increase_then_decrease_are_unsafe():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/test/unsafe_first_increase_then_decrease.txt')
    assert safe_report_amount == 0

def test_levels_that_first_decrease_then_increase_are_unsafe():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/test/unsafe_first_decrease_then_increase.txt')
    assert safe_report_amount == 0

def test_levels_that_neither_increase_nor_decrease_are_unsafe():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/test/unsafe_neither_increase_nor_decrease.txt')
    assert safe_report_amount == 0

def test_levels_that_increase_and_follow_all_rules_are_safe():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/test/safe_increasing.txt')
    assert safe_report_amount == 1

def test_levels_that_decrease_and_follow_all_rules_are_safe():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/test/safe_decreasing.txt')
    assert safe_report_amount == 1

def test_full_input():
    safe_report_amount = part1.get_total_safe_reports('advent-of-code/day2/input.txt')
    assert safe_report_amount == 572
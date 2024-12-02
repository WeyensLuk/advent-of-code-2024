import pytest
from day2 import part2

def test_levels_with_increase_more_than_3_is_unsafe():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/unsafe_increase_more_than_3.txt', 1)
    assert safe_report_amount == 0

def test_levels_with_decrease_more_than_3_is_unsafe():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/unsafe_decrease_more_than_3.txt', 1)
    assert safe_report_amount == 0

def test_levels_that_contain_one_level_that_first_increase_then_decrease_are_safe_with_dampener():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/unsafe_first_increase_then_decrease.txt', 1)
    assert safe_report_amount == 1

def test_levels_that_contain_one_level_that_first_decrease_then_increase_are_safe_with_dampener():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/unsafe_first_decrease_then_increase.txt', 1)
    assert safe_report_amount == 1

def test_levels_that_contain_one_level_that_neither_increases_nor_decreases_are_safe_with_dampener():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/unsafe_neither_increase_nor_decrease.txt', 1)
    assert safe_report_amount == 1

def test_removing_last_level_with_dampener_causes_safe_result():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/safe_last_level_to_be_removed.txt', 1)
    assert safe_report_amount == 1

def test_levels_that_increase_and_follow_all_rules_are_safe():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/safe_increasing.txt', 1)
    assert safe_report_amount == 1

def test_levels_that_decrease_and_follow_all_rules_are_safe():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/test/safe_decreasing.txt', 1)
    assert safe_report_amount == 1

def test_full_input():
    safe_report_amount = part2.get_total_safe_reports('advent-of-code/day2/input.txt', 1)
    assert safe_report_amount == 612
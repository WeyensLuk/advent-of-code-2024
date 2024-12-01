import pytest
from day1 import day1


# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. 
# For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; 
# if you pair up a 9 with a 3, the distance apart is 6.
# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. 
# In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!
def test_part1_provided_input_returns_given_total_distance():
    total_distance = day1.calculate_total_distance("advent-of-code/day1/test/sample_input.txt")
    assert total_distance == 11

def test_part1_full_input_returns_expected_total_distance():
    total_distance = day1.calculate_total_distance("advent-of-code/day1/input.txt")
    assert total_distance == 2086478

def test_part2_provided_input_returns_given_similarity_score():
    similarity_score = day1.calculate_similarity_score("advent-of-code/day1/test/sample_input.txt")
    assert similarity_score == 31

def test_part2_full_input_returns_expected_similarity_score():
    similarity_score = day1.calculate_similarity_score("advent-of-code/day1/input.txt")
    assert similarity_score == 24941624
import re

def calculate_sum_of_mul_statements(input_file):
    statements = read_mul_statements_from_file(input_file)
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    sum = 0

    for statement in statements:
        for match in pattern.finditer(statement):
            sum += int(match.group(1)) * int(match.group(2))
    
    return sum

def read_mul_statements_from_file(input_filename):
    statements = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        statements.append(line)
    return statements
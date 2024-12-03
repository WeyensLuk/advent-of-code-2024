import abc
import re

do_multiplication = True

def calculate_sum_of_enabled_mul_statements(input_file):
    statements = read_mul_statements_from_file(input_file)
    processed_statements = get_valid_statements(statements)
    sum = 0

    for statement in sorted(processed_statements, key=lambda x: (x.line, x.index)):
        sum += statement.operation.execute()
    
    return sum

def get_valid_statements(statements):
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    processed_statements = []

    for i, statement in enumerate(statements):
        for match in mul_pattern.finditer(statement):
            processed_statements.append(ProcessedStatement(i, match.start(), Multiply(int(match.group(1)), int(match.group(2)))))
        for match in do_pattern.finditer(statement):
            processed_statements.append(ProcessedStatement(i, match.start(), Do()))
        for match in dont_pattern.finditer(statement):
            processed_statements.append(ProcessedStatement(i, match.start(), Dont()))
    
    return processed_statements

def read_mul_statements_from_file(input_filename):
    statements = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        statements.append(line)
    return statements

class ProcessedStatement:
    def __init__(self, line, index, operation):
        self.line = line
        self.index = index
        self.operation = operation

class Operation:
    @abc.abstractmethod
    def execute(self):
        pass

class Multiply(Operation):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def execute(self):
        if do_multiplication: return self.left * self.right
        return 0

class Do(Operation):
    def execute(self):
        global do_multiplication
        do_multiplication = True
        return 0

class Dont(Operation):
    def execute(self):
        global do_multiplication
        do_multiplication = False
        return 0
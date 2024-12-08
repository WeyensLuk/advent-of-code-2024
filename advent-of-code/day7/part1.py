from itertools import product

def get_sum_of_correct_equations(input_file):
    equations = read_equations_from_file(input_file)
    sum = 0
    for equation in equations:
        if equation.can_be_solved(): sum += equation.result

    return sum

def read_equations_from_file(input_filename):
    equations = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        split = line.split(": ")
        equations.append(Equation(int(split[0]), [int(member) for member in split[1].split(" ")]))

    return equations

class Equation:
    def __init__(self, result, members):
        self.result = result
        self.members = members
        self.operands = "*+"

    def can_be_solved(self):
        operand_permutations = list(product(self.operands, repeat=len(self.members) - 1))
        for permutation in operand_permutations:
            result = self.equate(self.members[0], self.members[1], permutation[0])
            for i in range(1, len(permutation)):
                result = self.equate(result, self.members[i+1], permutation[i])
            
            if result == self.result: return True
                
        return False
    
    def equate(self, left, right, operand):
        if operand == "+":
            return left + right
        if operand == "*":
            return left * right
        
        raise Exception(f"{operand} is an unknown operation")
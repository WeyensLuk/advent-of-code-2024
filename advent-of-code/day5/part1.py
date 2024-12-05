def get_sum_of_middle_page_of_correct_instruction_sequences(input_file):
    correct_instructions = get_correct_instruction_sequences(input_file)
    sum = 0
    for instruction in correct_instructions:
        sum += instruction[len(instruction)//2]
    
    return sum

def get_correct_instruction_sequences(input_file):
    page_rules, instructions = read_page_rules_and_instructions_from_file(input_file)
    correct_instructions = []

    for instruction in instructions:
        is_valid_instruction = True
        for i in range(len(instruction)):
            for j in range(i + 1, len(instruction)):
                if not any(page_rule.page_dependency == instruction[i] and page_rule.page == instruction[j] for page_rule in page_rules):
                    is_valid_instruction = False
        
        if is_valid_instruction: correct_instructions.append(instruction)
    
    return correct_instructions


def read_page_rules_and_instructions_from_file(input_filename):
    page_rules = []
    instructions = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        if line.find("|") >= 0:
            page_rules.append(read_pager_order_rule(line))
        elif line.find(",") >= 0:
            instructions.append([int(page) for page in line.split(",")])

    return page_rules, instructions

def read_pager_order_rule(line):
    pages = line.split("|")
    return PageOrderRule(int(pages[0])).comes_before(int(pages[1]))

class PageOrderRule:
    def __init__(self, page):
        self.page_dependency = page

    def comes_before(self, page):
        self.page = page
        return self
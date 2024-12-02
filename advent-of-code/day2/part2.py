def get_total_safe_reports(input_filename, problem_dampener):
    reports = read_reports_from_file(input_filename)

    safe_reports = 0
    for report in reports:
        levels = [int(level) for level in report.split(" ")]
        if is_safe(levels): safe_reports+=1
        else:
            for i in range(len(levels)):
                if is_safe(remove_element(levels, i)):
                    safe_reports+=1
                    break
    
    return safe_reports

def read_reports_from_file(input_filename):
    reports = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        reports.append(line)
    return reports

def remove_element(levels, i):
    new_list = list(levels)
    del new_list[i]
    return new_list

def is_safe(levels):
    increasing = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        if difference_larger_than_3(levels[i], levels[i+1]): return False
        if increasing and ensure_sequence_keeps_increasing(levels[i], levels[i+1]): return False
        if not increasing and ensure_sequence_keeps_decreasing(levels[i], levels[i+1]): return False
        if levels_have_same_value(levels[i], levels[i+1]): return False

    return True

def difference_larger_than_3(left, right):
    return abs(left-right) > 3


def ensure_sequence_keeps_increasing(left, right):
    return left > right


def ensure_sequence_keeps_decreasing(left, right):
    return left < right


def levels_have_same_value(left, right):
    return left==right
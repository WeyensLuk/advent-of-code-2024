def read_lists_from_file(input_filename):
    list1, list2 = [], []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        values = line.split("   ")
        list1.append(int(values[0]))
        list2.append(int(values[1]))
    return list1, list2

def calculate_total_distance(input_filename):
    list1, list2 = read_lists_from_file(input_filename)

    list1.sort()
    list2.sort()

    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i]-list2[i])
    
    return total_distance

def calculate_similarity_score(input_filename):
    list1, list2 = read_lists_from_file(input_filename)

    similarity_score = 0
    for location_id in list1:
        similarity_score += location_id * list2.count(location_id)
    
    return similarity_score
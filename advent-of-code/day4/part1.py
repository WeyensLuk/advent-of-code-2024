from helpers.coordinate import Coordinate

def find_all_occurrences_of_xmas(input_file):
    wordsearch = read_wordsearch_from_file(input_file)
    xmas = "XMAS"
    
    return find_all_occurrences(wordsearch, xmas)

def find_all_occurrences(wordsearch, word):
    occurrences = 0
    start_positions = find_all_start_positions(word[0], wordsearch)
    directions = [Coordinate.west(), Coordinate.east(), Coordinate.south(), Coordinate.up(), Coordinate.northwest(), Coordinate.northeast(), Coordinate.southwest(), Coordinate.southeast()]

    for position in start_positions:
        for direction in directions:
            if find(wordsearch, position, word, direction): occurrences+=1
    
    return occurrences

def find(wordsearch, position, word, direction):
    current_position = Coordinate(position.x, position.y)
    for i in range(1, len(word)):
        current_position.x += direction.x
        current_position.y += direction.y
        if current_position.x < 0 or current_position.y < 0 or current_position.x >= len(wordsearch) or current_position.y >= len(wordsearch): return False
        if wordsearch[current_position.x][current_position.y] != word[i]: return False
    
    return True

def find_all_start_positions(letter_to_find, wordsearch):
    start_positions = []
    for i, line in enumerate(wordsearch):
        for j, letter in enumerate(line):
            if letter == letter_to_find:
                start_positions.append(Coordinate(i, j))
    
    return start_positions

def read_wordsearch_from_file(input_filename):
    wordsearch = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        wordsearch.append(line)
    return wordsearch

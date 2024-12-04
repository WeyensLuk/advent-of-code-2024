def find_all_occurrences_of_crossed_mas(input_file):
    wordsearch = read_wordsearch_from_file(input_file)
    mas = "MAS"
    
    return find_all_occurrences(wordsearch, mas)

def find_all_occurrences(wordsearch, word):
    occurrences = 0
    start_positions = find_all_start_positions(word[1], wordsearch)

    for position in start_positions:
        if find(wordsearch, position, word): occurrences+=1
    
    return occurrences

def find(wordsearch, position, word):
    down_left = position + Coordinate.down_left()
    up_right = position + Coordinate.up_right()
    down_right = position + Coordinate.down_right()
    up_left = position + Coordinate.up_left()

    diagonal = wordsearch[down_left.x][down_left.y] + wordsearch[position.x][position.y] + wordsearch[up_right.x][up_right.y]
    other_diagonal = wordsearch[down_right.x][down_right.y] + wordsearch[position.x][position.y] + wordsearch[up_left.x][up_left.y]
    return (diagonal == word or diagonal == word[::-1]) and (other_diagonal == word or other_diagonal == word[::-1])

def find_all_start_positions(letter_to_find, wordsearch):
    start_positions = []
    for i, line in enumerate(wordsearch):
        for j, letter in enumerate(line):
            if letter == letter_to_find and i != 0 and j != 0 and i != len(wordsearch) - 1 and j != len(wordsearch) - 1:
                start_positions.append(Coordinate(i, j))
    
    return start_positions

def read_wordsearch_from_file(input_filename):
    wordsearch = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        wordsearch.append(line)
    return wordsearch

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    @classmethod
    def left(cls):
        return Coordinate(-1, 0)
    
    @classmethod
    def right(cls):
        return Coordinate(1, 0)
    
    @classmethod
    def up(cls):
        return Coordinate(0, -1)

    @classmethod
    def down(cls):
        return Coordinate(0, 1)
    
    @classmethod
    def up_left(cls):
        return Coordinate(-1, -1)
    
    @classmethod
    def up_right(cls):
        return Coordinate(1, -1)
    
    @classmethod
    def down_left(cls):
        return Coordinate(-1, 1)
    
    @classmethod
    def down_right(cls):
        return Coordinate(1, 1)
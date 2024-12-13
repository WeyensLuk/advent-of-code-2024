memory_map = {}

def number_of_stones_after_blinking(input_file, number_of_blinks):
    stones_amount = read_stones_from_file(input_file)
    
    stones_amount = amount_of_stones_after_blinks(stones_amount, number_of_blinks)
    return stones_amount

def amount_of_stones_after_blinks(stones, number_of_blinks):
    if number_of_blinks == 0: return len(stones)

    amount = 0
    for stone in stones:
        if (stone.number, number_of_blinks) in memory_map:
            amount += memory_map[(stone.number, number_of_blinks)]
        else:
            sub_amount = amount_of_stones_after_blinks(stone.blink(), number_of_blinks-1)
            amount += sub_amount
            memory_map[(stone.number, number_of_blinks)] = sub_amount


    return amount

def read_stones_from_file(input_filename):
    stones = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        for stone in line.split(" "):
            stones.append(Stone(int(stone)))

    return stones

class Stone:
    def __init__(self, number):
        self.number = number
    
    def blink(self):
        if self.number == 0:
            return [Stone(1)]
        elif self.is_even_number():
            nr = str(self.number)
            half = len(nr)//2
            return [Stone(int(nr[:half])), Stone(int(nr[half:]))]
        
        return [Stone(self.number * 2024)]
    
    def is_even_number(self):
        return len(str(self.number)) % 2 == 0
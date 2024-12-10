from helpers.grid import Grid
from helpers.coordinate import *

lowest_elevation = '0'
highest_elevation = '9'

def sum_of_trailhead_ratings(input_file):
    grid = read_grid_from_file(input_file)
    trailheads = [coord for height, coord in grid.visit_all() if height == lowest_elevation]
    sum = 0
    for trailhead in trailheads:
        sum += len(get_all_trails(trailhead, grid))

    return sum

def get_all_trails(coord, grid):
    trails = []
    current_elevation = grid.get_cell(coord)
    for direction in ORTHOGONAL_DIRECTIONS:
        next_coord = coord + direction
        if not grid.is_out_of_bounds(next_coord) and grid.get_cell(next_coord) == str(int(current_elevation) + 1):
            if grid.get_cell(next_coord) == highest_elevation: 
                trails.append(next_coord)
                continue
            trails += get_all_trails(next_coord, grid)

    return trails 

def read_grid_from_file(input_filename):
    grid = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        grid.append(line)

    return Grid(grid)
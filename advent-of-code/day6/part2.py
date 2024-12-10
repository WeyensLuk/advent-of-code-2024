from helpers.coordinate import *
from helpers.grid import Grid
from copy import copy, deepcopy

obstacle = "#"

def get_unique_positions_for_patrol_loops(input_file):
    grid = read_grid_from_file(input_file)
    grid.current_position = determine_current_position(grid)
    direction = determine_direction(grid.current_cell)
    positions = find_all_possible_patrol_loops(grid, direction)

    return positions

def determine_current_position(grid):
    for position, coord in grid.visit_all():
        if position in "^<>v":
            return coord

def determine_direction(guard):
    if guard == "^": return NORTH
    if guard == "<": return WEST
    if guard == ">": return EAST
    if guard == "v": return SOUTH

def find_all_possible_patrol_loops(grid, direction):
    extra_obstacle_positions = []
    start_position = grid.current_position.as_tuple()
    visited_cells = [grid.current_position.as_tuple()]
    while True:
        next_position = grid.current_position + direction
        if grid.is_out_of_bounds(next_position): break

        if grid.get_cell(next_position) == obstacle:
            direction = direction.rotate_90degrees_clockwise()
            continue
        
        if next_position != start_position \
            and next_position not in visited_cells \
            and is_patrol_loop(deepcopy(grid), copy(direction)): 
            extra_obstacle_positions.append(next_position)
        grid.navigate(direction)
        visited_cells.append(grid.current_position.as_tuple())
        
    return len(set(extra_obstacle_positions))

def is_patrol_loop(grid, direction):
    new_obstacle_position = grid.current_position + direction

    if grid.is_out_of_bounds(new_obstacle_position): return False
    if grid.get_cell(new_obstacle_position) == obstacle: return False
    grid.set_cell(new_obstacle_position, obstacle)
    
    visited_cells = [(grid.current_position.as_tuple(), direction.as_tuple())]
    
    while True:
        next_position = grid.current_position + direction
        if grid.is_out_of_bounds(next_position): return False

        if grid.get_cell(next_position) == obstacle:
            direction = direction.rotate_90degrees_clockwise()
            continue

        if (next_position, direction) in visited_cells:
            return True

        grid.navigate(direction)
        visited_cells.append((grid.current_position.as_tuple(), direction.as_tuple()))

    return False

def read_grid_from_file(input_filename):
    grid = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        grid.append(list(line))

    return Grid(grid)
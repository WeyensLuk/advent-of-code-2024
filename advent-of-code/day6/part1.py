from helpers.coordinate import *
from helpers.grid import Grid
import copy

obstacle = "#"

def get_unique_positions_visited(input_file):
    grid = read_grid_from_file(input_file)
    grid.current_position = determine_current_position(grid)
    direction = determine_direction(grid.current_cell)
    visited_cells = follow_guard_path(grid, direction)

    return len(set(visited_cells))

def determine_current_position(grid):
    for position, coord in grid.visit_all():
        if position in "^<>v":
            return coord

def determine_direction(guard):
    if guard == "^": return NORTH
    if guard == "<": return WEST
    if guard == ">": return EAST
    if guard == "v": return SOUTH

def follow_guard_path(grid, direction):
    visited_cells = [copy.copy(grid.current_position)]
    while grid.navigate(direction):
        if grid.current_cell != obstacle:
            visited_cells.append(copy.copy(grid.current_position))
        else:
            grid.navigate(direction.inverse())
            direction = direction.rotate_90degrees_clockwise()

    return visited_cells

def read_grid_from_file(input_filename):
    grid = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        grid.append(line)

    return Grid(grid)
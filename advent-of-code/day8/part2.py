from helpers.grid import Grid

nothing = "."
antinode = "#"

def unique_amount_of_anti_nodes(input_file):
    grid = read_grid_from_file(input_file)
    antennae = {}
    for node, coord in grid.visit_all():
        if node != nothing:
            antennae.setdefault(node, []).append(coord)
    
    antinode_coords = []
    for antenna in antennae:
        for i in range(len(antennae[antenna]) - 1):
            for j in range(i+1, len(antennae[antenna])):
                antinode_coords.append(antennae[antenna][i])
                antinode_coords.append(antennae[antenna][j])

                diff = antennae[antenna][i] - antennae[antenna][j]
                antinode_coord = antennae[antenna][i] + diff
                while not grid.is_out_of_bounds(antinode_coord):
                    antinode_coords.append(antinode_coord)
                    antinode_coord += diff

                diff = diff.inverse()
                antinode_coord = antennae[antenna][j] + diff
                while not grid.is_out_of_bounds(antinode_coord):
                    antinode_coords.append(antinode_coord)
                    antinode_coord += diff
    
    antinode_coords = set(antinode_coords)
    return len(antinode_coords)

def read_grid_from_file(input_filename):
    grid = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        grid.append(list(line.rstrip('\n')))

    return Grid(grid)
import pytest
import os
from day9 import part2

def test_decode_filesystem_representation():
    filesystem = part2.Filesystem("2333133121414131402")
    assert filesystem.disk_map == "00...111...2...333.44.5555.6666.777.888899"

def test_defrag_filesystem():
    filesystem = part2.Filesystem("2333133121414131402")
    filesystem.defrag()
    assert filesystem.disk_map == "00992111777.44.333....5555.6666.....8888.."

def test_checksum_defragged_filesystem():
    filesystem = part2.Filesystem("2333133121414131402")
    filesystem.defrag()
    assert filesystem.checksum() == 2858

def test_full_input():
    checksum = part2.get_checksum_after_defragging('advent-of-code/day9/input.txt')
    assert checksum == 6307279963620

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
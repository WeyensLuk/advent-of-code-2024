import pytest
import os
from day9 import part1

def test_decode_filesystem_representation():
    filesystem = part1.Filesystem("2333133121414131402")
    assert filesystem.disk_map == "00...111...2...333.44.5555.6666.777.888899"

def test_defrag_filesystem():
    filesystem = part1.Filesystem("2333133121414131402")
    filesystem.defrag()
    assert filesystem.disk_map == "0099811188827773336446555566.............."

def test_checksum_defragged_filesystem():
    filesystem = part1.Filesystem("2333133121414131402")
    filesystem.defrag()
    assert filesystem.checksum() == 1928

def test_full_input():
    checksum = part1.get_checksum_after_defragging('advent-of-code/day9/input.txt')
    assert checksum == 6291146824486

def write_to_temp_file(text):
    file = open("test_input.txt", "w")
    file.write(text)
    file.close
    return os.path.realpath(file.name)
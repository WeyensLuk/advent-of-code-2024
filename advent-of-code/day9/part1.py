def get_checksum_after_defragging(input_file):
    dense_disk_map = read_dense_diskmap_from_file(input_file)
    fs = Filesystem(dense_disk_map)
    fs.defrag()
    return fs.checksum()

def read_dense_diskmap_from_file(input_filename):
    grid = []
    with open(input_filename, "r") as file:
        lines = file.readlines()
    
    return lines[0]

class Filesystem():
    FREE_SPACE = "."

    def __init__(self, dense_disk_map):
        self.disk_map = self.decode(dense_disk_map)

    def defrag(self):
        defragged = list(self.disk_map)
        for i in range(len(self.disk_map) - 1, -1, -1):
            if self.disk_map[i] != self.FREE_SPACE:
                defragged[defragged.index(self.FREE_SPACE)] = self.disk_map[i]
                defragged[i] = self.FREE_SPACE
            if "." not in "".join(defragged).rstrip("."):
                self.disk_map = "".join(defragged)
                return  

    def checksum(self):
        checksum = 0
        for i in range(len(self.disk_map)):
            if self.disk_map[i] == self.FREE_SPACE: return checksum
            checksum += (i * (ord(self.disk_map[i]) - 48))
    
    def decode(self, dense_disk_map):
        disk_map = ""
        id = 48
        for i in range(len(dense_disk_map)):
            if i % 2 == 0:
                char_to_write = chr(id)
                id += 1
            else:
                char_to_write = self.FREE_SPACE
            
            for j in range(int(dense_disk_map[i])):
                disk_map += char_to_write
        
        return disk_map
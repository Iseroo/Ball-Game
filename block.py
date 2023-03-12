import pygame as pg

def makeColumn(map, index):
    return [i[index].block for i in map]

def makeRow(map, index):
    return [x.block for x in map[index]]



class BlockNode:
    id = 0
    graph = set()
    def __init__(self, north, west, south, east, coords, map_size= 7) -> None:
        self.id = BlockNode.id
        BlockNode.id += 1
        self.north = north
        self.west = west
        self.south = south
        self.east = east
        self.coords = coords
        self.directions = {'north': None, 'south': None, 'east': None, 'west': None}
        self.map_size = map_size
        self.validate_map_walls()
        
    def __str__(self) -> str:
        return f'{self.west} {self.south} {self.east} {self.north}'
        # return f'{ "| " if self.west else "  "}{"二" if self.north and self.south else "▔▔" if self.north else "__" if self.south else "  "}{" |" if self.east else "  "}'

    def setup_directions(self, map):
        
            self.find_next('north', makeColumn(map, self.coords[1]))

            self.find_next('south', makeColumn(map, self.coords[1]))
        
            self.find_next('east', makeRow(map, self.coords[0]))
        
            self.find_next('west', makeRow(map, self.coords[0]))

    def find_next(self, direction, path):
        
        if direction == 'north':
            if self.coords[0] == 0:
                self.directions[direction] = self
            for x in range(self.coords[0], -1, -1):
               
                if path[x].north or x != 0 and path[x-1].south:
                    
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
        elif direction == 'west':
            if self.coords[0] == 0:
                self.directions[direction] = self
            for x in range(self.coords[1], -1, -1):
                if path[x].west or (x != 0 and path[x-1].east):
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
        elif direction == 'south':
            if self.coords[0] == len(path) - 1:
                self.directions[direction] = self
            for x in range(self.coords[0], len(path)):
                if path[x].south or( x != len(path) - 1 and path[x+1].north):
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
        elif direction == 'east':
            if self.coords[0] == len(path) - 1:
                self.directions[direction] = self
            for x in range(self.coords[1], len(path)):
                if path[x].east or (x != len(path) - 1 and path[x+1].west):
                    
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
       


    def get_next(self, direction):
        return self.directions[direction]


    def rotate(self):
        # pass
        # self.coords = (,)
        lst = [self.west, self.south, self.east, self.north]
        binary_str = ''.join(str(bit) for bit in lst)
        print(binary_str)
        incremented_int = int(binary_str, 2) + 1
        padded_binary_str = bin(incremented_int)[2:].zfill(len(lst))
        array = [int(bit) for bit in padded_binary_str]
        print(array)
        self.west, self.south, self.east, self.north = array if len(array) == 4 else (0,0,0,0)
        # return [self.west, self.south, self.east, self.north]
        return self.validate_map_walls()
        
    def validate_map_walls(self):
        blockid = self.id
        if (blockid % self.map_size) % (self.map_size-1) == 0:
            self.east = 1
        if blockid >= self.map_size * (self.map_size ) - self.map_size:
            self.south = 1
        if blockid % self.map_size == 0:
            self.west = 1
        if blockid <= self.map_size - 1 :
            self.north = 1
        return [self.west, self.south, self.east, self.north]


            
class PGBlock:
    def __init__(self, block, x ,y, size= (100,100)) -> None:
        self.block = block
        self.x = x+50
        self.y = y+50
        self.width = size[0]
        self.height = size[1]
        self.wide = 8
        self.color = (0, 0, 0)
        self.rect = (self.x, self.y, self.width, self.height)
        self.coords = self.block.coords
        self.id = self.block.id

    def __str__(self) -> str:
        return f'{self.block}'

    def draw(self, screen):
        
        #draw a rect that not filled
        pg.draw.rect(screen, self.color, self.rect, 1)
        
        # if self.block.id == 0:
# 
        # print(self.id)
        if self.block.north:
            pg.draw.line(screen, (0,0,0), (self.x, self.y), (self.x + self.width, self.y), self.wide)


        if self.block.south:
            # pass
            pg.draw.line(screen, (0,0,0), (self.x, self.y + self.width), (self.x + self.width, self.y + self.width ),self.wide)

        if self.block.east:
            # pass
            pg.draw.line(screen, (0,0,0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.width),self.wide)

        if self.block.west:
            # pass
            pg.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y + self.width),self.wide)

    def get_center(self):
        return (self.x + self.width/2, self.y + self.height/2)

    def clicked_inside(self, pos):
        # print(pos, self.x, self.y, self.width, self.height)
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height
    
    def rotate(self):
        return self.block.rotate()
        
        
        # self.x, self.y = 0,0
# def getCoordsById(id):
    
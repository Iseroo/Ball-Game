import json
import pygame as pg

def makeColumn(map, index):
    return [i[index].block for i in map]

def makeRow(map, index):
    return [x.block for x in map[index]]

# global map
# map = []


class BlockNode:
    id = 0
    graph = set()
    def __init__(self, north, west, south, east, coords) -> None:
        self.id = BlockNode.id
        BlockNode.id += 1
        self.north = north
        self.west = west
        self.south = south
        self.east = east
        self.coords = coords
        self.directions = {'north': None, 'south': None, 'east': None, 'west': None}
        
    def __str__(self) -> str:
        return f'{ "| " if self.west else "  "}{"二" if self.north and self.south else "▔▔" if self.north else "__" if self.south else "  "}{" |" if self.east else "  "}'

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
               
                if path[x].north:
                    
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
        elif direction == 'west':
            if self.coords[0] == 0:
                self.directions[direction] = self
            for x in range(self.coords[1], -1, -1):
                if path[x].west:
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
        elif direction == 'south':
            if self.coords[0] == len(path) - 1:
                self.directions[direction] = self
            for x in range(self.coords[0], len(path)):
                if path[x].south:
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
        elif direction == 'east':
            if self.coords[0] == len(path) - 1:
                self.directions[direction] = self
            for x in range(self.coords[1], len(path)):
                if path[x].east:
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
       


    def get_next(self, direction):
        return self.directions[direction]


    def rotate(self):
        lst = [self.west, self.south, self.east, self.north]
        binary_str = ''.join(str(bit) for bit in lst)
        incremented_int = int(binary_str, 2) + 1
        padded_binary_str = bin(incremented_int)[2:].zfill(len(lst))
        print(lst,int(binary_str, 2), incremented_int, bin(incremented_int))
        array = [int(bit) for bit in padded_binary_str]
        print(array)
        self.west, self.south, self.east, self.north = array if len(array) == 4 else (0,0,0,0)
        



            
class PGBlock:
    def __init__(self, block, x ,y) -> None:
        self.block = block
        self.x = x+50
        self.y = y+50
        self.width = 100
        self.height = 100
        self.wide = 8
        self.color = (0, 0, 0)
        self.rect = (self.x, self.y, self.width, self.height)
        self.coords = self.block.coords
        self.id = self.block.id
        self.directions = self.block.directions
        self.graph = self.block.graph


    def draw(self, screen):
        
        #draw a rect that not filled
        pg.draw.rect(screen, self.color, self.rect, 1)
        



        if self.block.north:
            pg.draw.line(screen, (0,0,0), (self.x, self.y), (self.x + self.width, self.y), self.wide)

        if self.block.south:
            pg.draw.line(screen, (0,0,0), (self.x, self.y + self.width), (self.x + self.width, self.y + self.width),self.wide)

        if self.block.east:
            pg.draw.line(screen, (0,0,0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.width),self.wide)

        if self.block.west:
            pg.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y + self.width),self.wide)

    def get_center(self):
        return (self.x + self.width/2, self.y + self.height/2)

    def clicked_inside(self, pos):
        # print(pos, self.x, self.y, self.width, self.height)
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height
# def getCoordsById(id):
    
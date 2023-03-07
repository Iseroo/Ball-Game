import json
from graph import *

def makeColumn(map, index):
    return [i[index] for i in map]

def makeRow(map, index):
    return map[index]

global map
map = []


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
        if direction == 'north' or direction == 'west':
            if self.coords[0] == 0:
                self.directions[direction] = self
            for x in range(self.coords[0], -1, -1):
                d = path[x].north if direction  == 'north' else path[x].west
                if d:
                    
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
        elif direction == 'south' or direction == "east":
            
            if self.coords[0] == len(path) - 1:
                self.directions[direction] = self
            for x in range(self.coords[0], len(path)):
                d =path[x].south if direction  == 'south' else path[x].east
                if d:
                    self.directions[direction] = path[x]
                    BlockNode.graph.add((self.id, path[x].id))
                    break
       


    def get_next(self, direction):
        return self.directions[direction]

class Ball:
    def __init__(self) -> None:
        pass



def readmap():
    with open('map.json', 'r') as f:
        data = json.load(f)
        for index, i in enumerate(data):
            temp = []
            for index2, i2 in enumerate(i):

                temp.append(BlockNode(i2['north'], i2['west'], i2['south'], i2['east'], (index, index2)))
            print([x.id for x in temp])
            map.append(temp)    

def getIdByCoords(coords):
    for x in map:
        for x2 in x:
            if x2.coords == coords:
                return x2.id
def getCoordsById(id):
     for x in map:
        for x2 in x:
            if x2.id == id:
                return x2.coords

if __name__ == '__main__':
    readmap()
    for i in map:
        for i2 in i:
            i2.setup_directions(map)
    direction = "east"
    coords = (0,2)
    next = map[coords[0]][coords[1]].get_next(direction)
    print(f"from: {map[coords[0]][coords[1]].id} ({coords[0]},{coords[1]}) to direction ({direction}) -> {next} ({next.coords[0]},{next.coords[1]})")
    # a = list(BlockNode.graph)
    # a.sort(key= lambda x : x[0])
    # print(a) 
    # for x in BlockNode.graph:
    #     if x[0] == 11 or x[1] == 11:
    #         print(x)

    # g =  Graph(7*7)
    # for x in BlockNode.graph:
    #     g.add_edge(x[0] ,x[1])
    # source = getIdByCoords((1,4))
    # dest = getIdByCoords((5,2))
    # a = g.printShortestDistance(source, dest, 7*7)
    # print(a)
    # for x in a:
    #     print(getCoordsById(x))
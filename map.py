import json
from block import *
from graph import *

class Map:
    def __init__(self, path, start, end):
        self.path = path
        self.map = []
        self.readmap()
        self.setup_directions()
        self.start = start
        self.end = end
    
    def readmap(self):
        with open(self.path, 'r') as f:
            data = json.load(f)

            for index, vector in enumerate(data):
                temp = []
                for index2, item in enumerate(vector):

                    temp.append(PGBlock(BlockNode(item['north'], item['west'], item['south'], item['east'], (index, index2)), index2*100, index*100))
                # print([x.id for x in temp])

                self.map.append(temp)

    
    def setup_directions(self):
        BlockNode.graph = set()
        for x in self.map:
            for x2 in x:
                x2.block.setup_directions(self.map)

    def get_coords_by_id(self, id):
        # print(id)
        for x in self.map:
            for x2 in x:
                if x2.id == id:
                    return x2.get_center()
                
    def get_block_clicked(self, x_coord, y_coord):
        # print(x_coord)
        for x in self.map:
            for x2 in x:
                if x2.clicked_inside((x_coord, y_coord)):
                    return x2
        return None
                
    def find_path(self):
        return find_path(BlockNode.graph,self.start, self.end)
    

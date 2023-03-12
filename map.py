import json
from block import *
from graph import *
import hashlib
import json


class Map:
    def __init__(self, path, start, end):
        self.path = path
        self.map = []
        
        self.start = start
        self.end = end
        self.readmap()
        self.setup_directions()

    def __str__(self) -> str:
        map_str_list = [] 
        for x in self.map:
            temp = []
            for x2 in x:
                temp.append(str(x2.block))
            map_str_list.append(temp)
        print(map_str_list)
        return str(map_str_list)
        
    
    def readmap(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
            self.size = (len(data[0]), len(data))      
            if self.size[0] != self.size[1]:
                raise Exception('Map is not square')
            self.scale = (700//self.size[0]) / 100    


            for index, vector in enumerate(data):
                temp = []
                for index2, item in enumerate(vector):
                    
                    temp.append(PGBlock(BlockNode(item['north'], item['west'], item['south'], item['east'], (index, index2), self.size[0]), index2*((self.scale*100)), index*(self.scale*100), (self.scale*100, self.scale*100)))
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
        print(self.get_hash())
        return find_path(BlockNode.graph,self.start, self.end)
    
    def get_hash(self):
        return hashlib.md5(str(self).encode()).hexdigest()
    
    def save_map(self):
        with open(f'./maps/{self.get_hash()}.json', 'w') as f:
            map_list = []
            for x in self.map:
                temp = []
                for x2 in x:
                    temp.append({'north': x2.block.north, 'west': x2.block.west, 'south': x2.block.south, 'east': x2.block.east})
                map_list.append(temp) 
            json.dump(map_list, f)
    

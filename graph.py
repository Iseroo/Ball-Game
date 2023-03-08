from collections import deque

def find_path(graph, start, end):
    """
    Finds a path between two nodes in an unweighted directed graph using BFS.

    Args:
        graph (list): The graph represented as a list of tuples, where each tuple contains two node IDs representing a directed edge.
        start (int): The ID of the starting node.
        end (int): The ID of the ending node.

    Returns:
        A list of node IDs representing the path from start to end, or an empty list if no path exists.
    """
    # Convert the input graph to a dictionary of adjacency lists
    adj_list = {}
    for edge in graph:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
        adj_list[edge[0]].append(edge[1])

    # Initialize the queue and the visited set
    queue = deque([(start, [start])])
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Dequeue the next node to explore
        current, path = queue.popleft()

        # If we've reached the end node, return the path
        if current == end:
            return path

        # Mark the current node as visited
        visited.add(current)

        # Add all unvisited neighbors of the current node to the queue
        for neighbor in adj_list.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # If we've searched the entire graph and haven't found the end node, return an empty path
    return []

import json

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


def readmap(path):
    with open('path', 'r') as f:
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



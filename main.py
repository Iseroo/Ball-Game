from graph import *













if __name__ == '__main__':
    readmap()
    for i in map:
        for i2 in i:
            i2.setup_directions(map)


            
    print(BlockNode.graph)
    start = 11
    end = 37
    paths = []
    # for x in range(7*7):
    print(find_path(BlockNode.graph, start, end))
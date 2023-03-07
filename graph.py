import sys
import heapq
class Graph():
 
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        print(self.adj)
 
    def add_edge(self, src, dest):
 
        self.adj[src].append(dest)
        self.adj[dest].append(src)
  
    # a modified version of BFS that stores predecessor
    # of each vertex in array p
    # and its distance from source in array d
    def BFS(self, src, dest, v, pred, dist):
    
        # a queue to maintain queue of vertices whose
        # adjacency list is to be scanned as per normal
        # DFS algorithm
        queue = []
    
        # boolean array visited[] which stores the
        # information whether ith vertex is reached
        # at least once in the Breadth first search
        visited = [False for i in range(v)]
    
        # initially all vertices are unvisited
        # so v[i] for all i is false
        # and as no path is yet constructed
        # dist[i] for all i set to infinity
        for i in range(v):
    
            dist[i] = 1000000
            pred[i] = -1;
        
        # now source is first to be visited and
        # distance from source to itself should be 0
        visited[src] = True;
        dist[src] = 0;
        queue.append(src);
    
        # standard BFS algorithm
        while (len(queue) != 0):
            u = queue[0];
            queue.pop(0);
            for i in range(len(self.adj[u])):
            
                if (visited[self.adj[u][i]] == False):
                    visited[self.adj[u][i]] = True;
                    dist[self.adj[u][i]] = dist[u] + 1;
                    pred[self.adj[u][i]] = u;
                    queue.append(self.adj[u][i]);
    
                    # We stop BFS when we find
                    # destination.
                    if (self.adj[u][i] == dest):
                        print(self.adj[u], u, i, dest)
                        return True;
    
        return False;
    
    # utility function to print the shortest distance
    # between source vertex and destination vertex
    def printShortestDistance(self, s, dest, v):
        
        # predecessor[i] array stores predecessor of
        # i and distance array stores distance of i
        # from s
        pred=[0 for i in range(v)]
        dist=[0 for i in range(v)];
    
        if (self.BFS( s, dest, v, pred, dist) == False):
            print("Given source and destination are not connected")
    
        # vector path stores the shortest path
        path = []
        crawl = dest;
        path.append(crawl);
        
        while (pred[crawl] != -1):
            path.append(pred[crawl]);
            crawl = pred[crawl];
        
    
        # distance from source is in distance array
        print("Shortest path length is : " + str(dist[dest]), end = '')
    
        # printing path from source to destination
        print("\nPath is : : ")
        a = []
        for i in range(len(path)-1, -1, -1):
            a.append(path[i])
        return a
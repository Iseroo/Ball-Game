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




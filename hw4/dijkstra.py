import heapq


def find_shortest_path(graph, source, destination):
    """
    Apply the dijkstra algorithm to find the shortest path from source to destination
    :param graph: A dictionary with the format {node1: ((neighbor1, dist1), (neighbor2, dist2),...),...}
    :param source: The source node
    :param destination: The destination node
    :return: calls the print_shortest_path function once reach the destination node
    """
    # d stores the shortest distance from source in a dictionary
    d = dict.fromkeys(graph.keys())
    d[source] = 0
    # backptr stores the back pointer of the current node in a dictionary in order to print path
    backptr = dict.fromkeys(graph.keys())
    # F is a min_heap with the format [(dist, node)], initialize with source node
    F = []
    heapq.heappush(F, (d[source], source))
    # removed is True when d does not match dist in F
    removed = False
    while len(F) != 0:  # while F is not empty
        f = heapq.heappop(F)
        # pop the node until dist matches d
        if d[f[1]] is not None:
            while (d[f[1]] < f[0]) & (len(F) != 0):
                f = heapq.heappop(F)
                removed = True
        if len(F) != 0 & removed is True:
            f = heapq.heappop(F)
            removed = False
        f = f[1]
        if f == destination:
            print_shortest_path(backptr, d[f], f)
            return
        for w in graph[f]:
            if d[w[0]] is None:
                d[w[0]] = d[f] + w[1]
                backptr[w[0]] = f
                heapq.heappush(F, (d[w[0]], w[0]))
            else:
                if d[f] + w[1] < d[w[0]]:
                    d[w[0]] = d[f] + w[1]
                    backptr[w[0]] = f
                    heapq.heappush(F, (d[w[0]], w[0]))


def print_shortest_path(back, dist, f):
    """
    Print the path built from find_shortest_path
    :param back: The back pointer dictionary
    :param dist: The shortest distance
    :param f: The destination node
    :return: Print both the distance and the path
    """
    print("The shortest distance is", dist)
    path = []
    while f is not None:
        path.append(f)
        f = back[f]
    path.reverse()
    print("The shortest path is", path)

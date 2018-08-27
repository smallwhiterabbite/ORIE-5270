import heapq


def transform(file):
    """
    Transform txt file into a list of Edge
    :param file:
    :return: A dictionary graph with node as keys, (neighbor, distance) as values
    """
    graph = {}
    f = open(file, 'r')
    count = 0
    for line in f:
        count = count + 1

    f = open(file, 'r')
    while count > 0:
        count = count - 2
        n = float(f.readline().splitlines()[0])
        v = f.readline().splitlines()[0]
        if v != '':
            s = v.split(',')
            graph[n] = []
            for i in range(0, len(s), 2):
                graph[n].append((float(s[i][1:]), float(s[i + 1][:-1])))
        else:
            graph[n] = []
    return graph


# find shortest path with dijkstra's algorithm
def find_shortest_path(txt_file, source, destination):
    """
    Apply the dijkstra algorithm to find the shortest path from source to destination
    :param txt_file: The graph txt file
    :param source: The source node
    :param destination: The destination node
    :return: call the print_shortest_path function once reach the destination node,
             which returns shortest distance and corresponding path
    """
    graph = transform(txt_file)

    # d stores the shortest distance from source in a dictionary
    d = dict.fromkeys(graph.keys())
    d[source] = 0
    # p stores the back pointer of the current node in a dictionary in order to print path
    p = dict.fromkeys(graph.keys())
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
            return print_shortest_path(p, d[f], f)
        for w in graph[f]:
            if d[w[0]] is None:
                d[w[0]] = d[f] + w[1]
                p[w[0]] = f
                heapq.heappush(F, (d[w[0]], w[0]))
            else:
                if d[f] + w[1] < d[w[0]]:
                    d[w[0]] = d[f] + w[1]
                    p[w[0]] = f
                    heapq.heappush(F, (d[w[0]], w[0]))


def print_shortest_path(back, dist, f):
    """
    Print the path built from find_shortest_path
    :param back: The back pointer dictionary
    :param dist: The shortest distance
    :param f: The destination node
    :return: Shortest distance and the path
    """
    path = []
    while f is not None:
        path.append(f)
        f = back[f]
    path.reverse()
    return dist, path


# find negative cycle with Bellman-Ford algorithm
class Edge(object):

    def __init__(self, u, v, w):
        """
        :param u: Start of the edge
        :param v: End of the edge
        :param w: Weight of the edge
        """
        self.u = u
        self.v = v
        self.w = w


def find_negative_cycle(txt_file):
    """
    Apply the bellman-ford algorithm to find if there is a negative cycle
    :param txt_file: The graph txt file
    :return: Calls the print_negative_cycle function once discover a negative cycle
    """
    graph = transform(txt_file)
    n_vertex = len(graph)
    edge = []
    for v in graph:
        if len(graph[v]) != 0:
            for e in graph[v]:
                edge.append(Edge(v, e[0], e[1]))
    n_edge = len(edge)

    # step 1: initialize d and p which stores distance to source node and the back pointer
    inf = 9999
    d = dict.fromkeys(graph.keys())
    for key in d.keys():
        d[key] = inf
    p = dict.fromkeys(graph.keys())
    source = edge[0].u
    p[source] = source
    d[source] = 0

    # step 2: repeat n_vertex-1 times
    for i in range(n_vertex-1):
        for j in range(n_edge):
            u = edge[j].u
            v = edge[j].v
            w = edge[j].w
            if d[u] is not None:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    p[v] = u

    # step 3: run the n_vertex time
    for j in range(n_edge):
        u = edge[j].u
        v = edge[j].v
        w = edge[j].w
        if d[u] is not None:
            if d[v] > d[u] + w:
                return print_negative_cycle(v, p)
    return print_negative_cycle(None, None)


def print_negative_cycle(node, back):
    """
    Print out the negative cycle if there exits one
    :param node: A node in the negative cycle, None if there is no such cycle
    :param back: A dictionary which stores the back pointer of each node
    :return: Either the path of the cycle or None if there is no such cycle
    """
    if node is None:
        return None
    start = node
    path = [start]
    node = back[node]
    while node != start:
        path.append(node)
        node = back[node]
    path.append(start)
    return path


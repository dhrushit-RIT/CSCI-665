RIDICULOUSLY_LARGE_NUMBER = 999999999


class Node:
    __slots__ = "neighbors", "value"

    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_edge(self, other_node, weight):
        if (other_node, weight) not in self.neighbors:
            self.neighbors.append((other_node, weight))


class Graph:
    __slots__ = "vertices", "edges", "edges_by_index"

    def __init__(self):
        self.vertices = []
        self.edges = []
        self.edges_by_index = []  # to be used if you are sure that the edges' and vertices' sequence is not changed

    def add_edge_by_index(self, start, end, weight, undirected=False):
        self.edges.append((self.vertices[start], self.vertices[end], weight))
        self.edges_by_index.append((start, end, weight))
        self.vertices[start].add_edge(self.vertices[end], weight)
        if undirected:
            self.vertices[end].add_edge(self.vertices[start], weight)

    def add_edge_unique_by_index(self, start, end, weight, undirected=False):
        if not (self.vertices[start], self.vertices[end], weight) in self.edges:
            self.add_edge_by_index(start, end, weight, undirected)
        if undirected:
            if not (self.vertices[end], self.vertices[start], weight) in self.edges:
                self.add_edge_by_index(end, start, weight, undirected)

    def add_edge(self, start, end, weight, undirected=False):
        self.edges.append((start, end, weight))
        start.add_edge(end, weight)
        if undirected:
            end.add_edge(start, weight)

    def add_edge_unique(self, start, end, weight, undirected=False):
        if not (start, end, weight) in self.edges:
            self.add_edge(start, end, weight, undirected)

    def add_vertex(self, vert):
        self.vertices.append(vert)


class FFGraph(Graph):
    __slots__ = "student_nodes", "clothing_nodes", "source_node", "sink_node"

    def __init__(self):
        super().__init__()
        self.source_node = FFNode(-1)
        self.sink_node = FFNode(-2)
        self.student_nodes = []
        self.clothing_nodes = []

    def add_clothing(self, clothing):
        self.clothing_nodes.append(clothing)

    def add_student(self, hat):
        self.student_nodes.append(hat)

    def add_forward_edge(self, start_node, end_node, weight, capacity, edge_type="forward"):
        if not start_node.contains_edge(end_node):
            self.edges.append((start_node, end_node, weight, 0, capacity, edge_type))
            start_node.add_edge(end_node, FFEdge(start_node, end_node, weight, 0, capacity, edge_type))

    def __str__(self):
        ret = "Graph\n=====\n"
        for edge in self.edges:
            ret += str(edge[0]) + "-" + str(edge[1]) + ":W" + str(edge[2]) + ":F" + str(edge[3]) + ":C" + str(
                edge[4]) + ":" + str(edge[5]) + "\n"
        return ret

    def add_backward_edge(self, start, end, weight, capacity):
        if end != self.source_node:
            self.add_forward_edge(start, end, weight, capacity, "backward")

    def clear_visited(self):
        self.source_node.visited = False
        for node in self.clothing_nodes:
            node.visited = False
        for node in self.student_nodes:
            node.visited = False
        self.sink_node.visited = False

    def clear_path_parents(self):
        self.source_node.path_parent = None
        for node in self.clothing_nodes:
            node.path_parent = None
        for node in self.student_nodes:
            node.path_parent = None
        self.sink_node.path_parent = None

    def get_shortest_path_source_to_sink(self):
        self.clear_visited()
        self.clear_path_parents()
        queue = [self.source_node]

        while len(queue) > 0:
            par = queue.pop(0)
            par.visited = True
            if par == self.sink_node:
                break

            for nbr in par.neighbors:
                if not nbr[0].visited:
                    nbr[0].path_parent = par
                    queue.append(nbr)

        if not self.sink_node.visited:
            return None

        path = []
        source_node = self.sink_node

        while source_node != self.source_node:
            path.insert(0, source_node)
            source_node = source_node.path_parent

        return path

    def get_path_source_to_sink_dfs(self, root, destination, pth):
        if root == destination:
            pth.append((root, None))
            return pth
        for nbr in root.neighbors:
            edge_to_nbr = nbr[1]
            if edge_to_nbr.flow == 0:
                edge_to_nbr.flow = 1
                if edge_to_nbr.edge_type == "forward":
                    self.add_backward_edge(nbr[0], root, 1, 1)
                else:
                    # print("using backward edge")
                    nbr[0].free_capacity(root)
                nbr[0].visited = True
                updated_pth = pth[:]
                updated_pth.append((root, nbr[1]))
                new_path = self.get_path_source_to_sink_dfs(nbr[0], destination, updated_pth)
                if len(new_path) > 0 and new_path[-1][0] == destination:
                    return new_path
        return []


class FFNode:
    __slots__ = "neighbors", "value", "visited", "path_parent"

    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def contains_edge(self, end_node):
        for nbr in self.neighbors:
            if nbr[0] == end_node:
                return True
        return False

    def free_capacity(self, node):
        for nbr in self.neighbors:
            if nbr[0] == node:
                nbr[1].flow = 0

    def add_edge(self, other_node, edge):
        if (other_node, edge) not in self.neighbors:
            self.neighbors.append((other_node, edge))

    def get_one_flow_edge(self):
        for nbr in self.neighbors:
            if nbr[1].flow == 1:
                return nbr[0]

    def __str__(self):
        return " " + str(self.value) + " "


class FFEdge:
    __slots__ = "start_node", "end_node", "weight", "flow", "capacity", "edge_type"

    def __init__(self, start_node, end_node, weight, flow, capacity, edge_type="forward"):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
        self.flow = flow
        self.capacity = capacity
        self.edge_type = "forward"

    def use_capacity(self, amount):
        assert self.capacity >= amount
        self.capacity -= amount

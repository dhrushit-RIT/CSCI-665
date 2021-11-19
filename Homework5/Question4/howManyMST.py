class Graph:
    __slots__ = "edges", "vertices", "dfs_rec_util_fin_order", "dfs_finish_order", "edge_counter"

    def __init__(self):
        self.edges = []
        self.vertices = []
        self.dfs_rec_util_fin_order = 0
        self.dfs_finish_order = []
        self.edge_counter = None

    def set_edge_count_arr(self):
        max_edge = max(self.edges, key=lambda x: x[2])
        self.edge_counter = [0] * max_edge

    def add_node(self, node):
        self.vertices.append(node)

    def sort_edges(self, descending=False):
        self.edges.sort(key=lambda x: x[2], reverse=descending)

    def add_edge_unique(self, from_node, to_node, weight):
        edge = (from_node, to_node, weight)
        if edge not in self.edges:
            from_node.add_edge(to_node, weight)
            to_node.add_edge(from_node)
            self.edges.append(edge)

    def add_edge(self, from_node, to_node, weight=1):
        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node)
        self.edges.append((from_node, to_node, weight))

    def delete_edge(self, edge):
        self.edges.remove(edge)

    def reset_visited(self):
        for node in self.vertices:
            node._visited = False

    def __str__(self):
        graph_str = ""
        for vert in self.vertices:
            graph_str += str(vert) + "\n"
        return graph_str


class Node:
    __slots__ = "node_id", "value", "connections", "_visited", "finish_order", "finished",

    def __init__(self, val, nid=-1) -> None:
        self.connections = []
        self.value = val
        self._visited = False
        self.finish_order = None
        self.node_id = nid
        self.finished = False

    def unfinish(self):
        self.finished = False

    def reset_connections(self):
        self.connections = []

    def set_order(self, order):
        self.finish_order = order

    def add_edge(self, other_node, weight=1):
        self.connections.append((other_node, weight))

    def mark_visited(self):
        self._visited = True

    def finish(self):
        self.finished = True

    def is_visited(self):
        return self._visited

    def is_finished(self):
        return self.finished

    def __str__(self):
        node_str = str(self.value) + " : "
        connected_nodes = []
        for connection in self.connections:
            connected_nodes.append(
                str(connection[0].value) + "(" + str(connection[1]) + ")")

        node_str += ", ".join(connected_nodes)
        return node_str


class Edge:
    __slots__ = "from_node", "to_node", "weight", "direction"

    def __init__(self, from_node, to_node, weight) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.direction = 2
        self.weight = weight


def process_input():
    nm = [int(x) for x in input().strip().split()]
    n = nm[0]
    m = nm[1]

    g = Graph()

    for node_index in range(n):
        g.add_node(Node(node_index))

    for _ in range(m):
        line = [int(x) for x in input().strip().split()]
        from_node = g.vertices[line[0]]
        to_node = g.vertices[line[1]]
        weight = line[2]
        g.add_edge_unique(from_node, to_node, weight)
        # g.add_edge_unique(to_node, from_node, weight)

    return g


class UnionFind:
    __slots__ = "graph", "boss", "size_arr", "set"

    def __init__(self, uf_graph) -> None:
        self.graph = uf_graph
        self.boss = []
        self.size_arr = []
        self.set = []
        for vert in uf_graph.vertices:
            self.boss.append(vert)
            self.set.append([vert])
            self.size_arr.append(1)

    def find(self, node):
        return self.boss[node.value]

    def union(self, node1, node2):
        if self.size_arr[node1.value] >= self.size_arr[node2.value]:
            for idx in range(len(self.boss)):
                if self.boss[idx] == self.boss[node2.value]:
                    self.boss[idx] = self.boss[node1.value]

            self.size_arr[node1.value] += self.size_arr[node2.value]
            self.set[node1.value].extend(self.set[node2.value])
        else:
            for idx in range(len(self.boss)):
                if self.boss[idx] == self.boss[node1.value]:
                    self.boss[idx] = self.boss[node2.value]

            self.size_arr[node2.value] += self.size_arr[node1.value]
            self.set[node2.value].extend(self.set[node1.value])


def find_mst_kruskal(k_graph):
    k_graph.sort_edges()
    aUF = UnionFind(k_graph)

    so_many_edges_included = 0
    included_edges = []
    num_mst = 1

    for edge_index in range(len(k_graph.edges)):
        if so_many_edges_included >= len(k_graph.vertices) - 1:
            break

        if edge_index < len(k_graph.edges) - 1:
            curr_edge = k_graph.edges[edge_index]
            next_edge = k_graph.edges[edge_index + 1]
            if curr_edge[2] == next_edge[2]:
                if aUF.find(curr_edge[0]) != aUF.find(curr_edge[1]) and aUF.find(next_edge[0]) != aUF.find(
                        next_edge[1]):
                    num_mst *= 2

        if aUF.find(k_graph.edges[edge_index][0]) == aUF.find(k_graph.edges[edge_index][1]):
            continue

        else:
            if edge_index > 0:
                curr_edge = k_graph.edges[edge_index]
                prev_edge = k_graph.edges[edge_index - 1]
                current_edge_weight = curr_edge[2]
                prev_edge_weight = prev_edge[2]
                if current_edge_weight == prev_edge_weight:
                    prev_boss = aUF.find(prev_edge[0])
                    # if aUF.find(prev_edge[0]) == aUF.find(prev_edge[1]):
                    if aUF.find(curr_edge[0]) == prev_boss or aUF.find(curr_edge[1]) == prev_boss or aUF.find(curr_edge[0]) != aUF.find(curr_edge[1]):
                        num_mst //= 2

            aUF.union(k_graph.edges[edge_index][0], k_graph.edges[edge_index][1])
            included_edges.append(k_graph.edges[edge_index])
            so_many_edges_included += 1

    # for an_edge in k_graph.edges:
    #     if so_many_edges_included >= len(k_graph.vertices) - 1:
    #         break
    #     if aUF.find(an_edge[0]) == aUF.find(an_edge[1]):
    #         continue
    #     else:
    #         # num_mst
    #         aUF.union(an_edge[0], an_edge[1])
    #         included_edges.append(an_edge)
    #         so_many_edges_included += 1

    return included_edges, num_mst


if __name__ == '__main__':
    graph = process_input()
    # print(graph)

    mst, mst_count = find_mst_kruskal(graph)

    # for edge in mst:
    #     print(str(edge[0].value) + "-" +
    #           str(edge[1].value) + ":" + str(edge[2]))
    print(mst_count)
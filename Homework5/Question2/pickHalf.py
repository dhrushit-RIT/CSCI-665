class Graph:
    __slots__ = "edges", "vertices", "dfs_rec_util_fin_order", "dfs_finish_order"

    def __init__(self):
        self.edges = []
        self.vertices = []
        self.dfs_rec_util_fin_order = 0
        self.dfs_finish_order = []

    def add_node(self, node):
        self.vertices.append(node)

    def add_edge_unique(self, from_node, to_node):
        edge = (from_node, to_node)
        if edge not in self.edges:
            from_node.add_edge(to_node)
            self.edges.append(edge)

    def add_edge(self, from_node, to_node):
        from_node.add_edge(to_node)
        self.edges.append((from_node, to_node))

    def delete_edge(self, edge):
        self.edges.remove(edge)

    def reset_visited(self):
        for node in self.vertices:
            node._visited = False

    def bfs(self, start_node):
        self.reset_visited()
        queue = [start_node]
        # visited = []

        while len(queue) > 0:
            explore_node = queue.pop(0)
            explore_node.mark_visited()

            for nbr in explore_node.connections:
                if not nbr.is_visited():
                    queue.append(nbr)

        self.reset_visited()

    def dfs_util(self, node):
        if node.is_visited():
            return

        node.mark_visited()
        for nbr in node.connections:
            if not nbr.is_visited():
                self.dfs_util(nbr)

    def dfs(self, start_node):
        self.reset_visited()
        self.dfs_util(start_node)
        self.reset_visited()

    def dfs_rec_util(self, node, order=False):
        if not node.is_visited():
            node.mark_visited()

            for nbr in node.connections:
                if not nbr.is_visited():
                    self.dfs_rec_util(nbr, order)

            if order:
                self.dfs_finish_order.append(node)
                node.set_order(self.dfs_rec_util_fin_order)
                self.dfs_rec_util_fin_order += 1

    def dfs_rec_with_order(self, start_node):
        self.dfs_rec_util_fin_order = 0
        self.dfs_finish_order = []
        self.reset_visited()
        self.dfs_rec_util(start_node, True)
        self.reset_visited()

    def dfs_rec(self, start_node):
        self.reset_visited()
        self.dfs_rec_util(start_node)
        self.reset_visited()

    def collect_component_nodes_iter(self, node):
        accumulator = []
        stack = [node]

        while len(stack) > 0:
            explore_node = stack.pop()
            if explore_node.is_visited():
                if not explore_node.is_finished():
                    accumulator.append(explore_node)
                    explore_node.finish()
            else:
                explore_node.mark_visited()
                stack.append(explore_node)

                for nbr in explore_node.connections:
                    if not nbr.is_visited():
                        stack.append(nbr)
        return accumulator

    def collect_component_nodes(self, node, accumulator):
        if not node.is_visited():
            node.mark_visited()

            for nbr in node.connections:
                if not nbr.is_visited():
                    self.collect_component_nodes(nbr, accumulator)

            accumulator.append(node)
        return accumulator

    def dfs_iter(self, start_node):
        stack = [start_node]

        while len(stack) > 0:
            explore_node = stack.pop()
            if explore_node.is_visited():
                if not explore_node.is_finished():
                    self.dfs_finish_order.append(explore_node)
                    explore_node.finish()
            else:
                explore_node.mark_visited()
                stack.append(explore_node)

                for nbr in explore_node.connections:
                    if not nbr.is_visited():
                        stack.append(nbr)

    def reverse_edges(self):
        for node in self.vertices:
            node.reset_connections()
        temp_edges = self.edges[:]
        self.edges = []
        for edge in temp_edges:
            self.add_edge(edge[1], edge[0])

    def reset_finished(self):
        for vert in self.vertices:
            vert.unfinish()

    def compute_connected_components(self):
        if len(self.vertices) <= 0:
            raise Exception("empty vertices array")

        self.reset_visited()

        self.dfs_finish_order = []
        for node in self.vertices:
            self.dfs_iter(node)

        self.reverse_edges()

        self.dfs_finish_order.reverse()

        self.reset_visited()
        self.reset_finished()
        connected_components = []
        for node in self.dfs_finish_order:
            if not node.is_visited():
                connected_components.append(
                    self.collect_component_nodes_iter(node))

        self.reverse_edges()
        return connected_components

    def __str__(self):
        graph_str = ""
        for vert in self.vertices:
            graph_str += str(vert) + "\n"
        return graph_str


class Node:
    __slots__ = "node_id", "value", "connections", "_visited", "finish_order", "finished"

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

    def add_edge(self, other_node):
        self.connections.append(other_node)

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
            connected_nodes.append(str(connection.value))

        node_str += ", ".join(connected_nodes)
        return node_str


def process_input():
    n = int(input())

    g = Graph()
    for card_index in range(n):
        g.add_node(Node(card_index + 1))

    for edge_index in range(n):
        line = [int(x) for x in input().strip().split()]
        g.add_edge_unique(g.vertices[line[0] - 1], g.vertices[line[1] - 1])
        g.add_edge_unique(g.vertices[line[1] - 1], g.vertices[line[0] - 1])

    return g


if __name__ == '__main__':
    graph = process_input()
    # print(graph)

    components = graph.compute_connected_components()
    is_correct = True
    for component in components:
        is_correct = is_correct & ((len(component) & 1) == 0)

    # print("is_correct", is_correct)
    if is_correct:
        print("YES")
    else:
        print("NO")

"""
file: addOne.py
description: Determine determines if it is possible to
add just a single edge to a given graph such that it becomes strongly connected.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

class Graph:
    __slots__ = "edges", "vertices", "dfs_rec_util_fin_order", "dfs_finish_order"
    """
    Initializes graph. 

    :param: None 
    :return: None
    """
    def __init__(self):
        self.edges = []
        self.vertices = []
        self.dfs_rec_util_fin_order = 0
        self.dfs_finish_order = []
    """
    Adds new node to vertices. 

    :param: new node to add 
    :return: None
    """
    def add_node(self, node):
        self.vertices.append(node)

    """
    Adds new node from given node if not already present. 

    :param: new node to add, from node to add to
    :return: None
    """
    def add_edge_unique(self, from_node, to_node):
        edge = (from_node, to_node)
        if edge not in self.edges:
            from_node.add_edge(to_node)
            self.edges.append(edge)
    """
    Adds new edge. 

    :param: new node to add, from node to add to
    :return: None
    """
    def add_edge(self, from_node, to_node):
        from_node.add_edge(to_node)
        self.edges.append((from_node, to_node))
    """
    Deletes edge. 

    :param: edge to delete
    :return: None
    """
    def delete_edge(self, edge):
        self.edges.remove(edge)
    """
    Resets visited nodes. 

    :param: None
    :return: None
    """
    def reset_visited(self):
        for node in self.vertices:
            node._visited = False
    """
    DFS function helper. 

    :param: node to check for
    :return: None
    """
    def dfs_util(self, node):
        if node.is_visited():
            return

        node.mark_visited()
        for nbr in node.connections:
            if not nbr.is_visited():
                self.dfs_util(nbr)
    """
    DFS. 

    :param: starting node
    :return: None
    """
    def dfs(self, start_node):
        self.reset_visited()
        self.dfs_util(start_node)
        self.reset_visited()
    """
    DFS recursive helper. 

    :param: node to check for, without order
    :return: None
    """
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
    """
    DFS recursive with order. 

    :param: starting node
    :return: None
    """
    def dfs_rec_with_order(self, start_node):
        self.dfs_rec_util_fin_order = 0
        self.dfs_finish_order = []
        self.reset_visited()
        self.dfs_rec_util(start_node, True)
        self.reset_visited()
    """
    DFS recursive. 

    :param: starting node
    :return: None
    """
    def dfs_rec(self, start_node):
        self.reset_visited()
        self.dfs_rec_util(start_node)
        self.reset_visited()
    """
    Collect nodes iteratively and returns an array with them. 

    :param: node
    :return: accumulator array
    """
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
    """
    Same as previous function but recursively.

    :param: node and accumulator
    :return: accumulator
    """
    def collect_component_nodes(self, node, accumulator):
        if not node.is_visited():
            node.mark_visited()

            for nbr in node.connections:
                if not nbr.is_visited():
                    self.collect_component_nodes(nbr, accumulator)

            accumulator.append(node)
        return accumulator
    """
    DFS iteratively. 

    :param: starting node
    :return: None
    """
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
    """
    Reverse edges. 

    :param: None
    :return: None
    """
    def reverse_edges(self):
        for node in self.vertices:
            node.reset_connections()
        temp_edges = self.edges[:]
        self.edges = []
        for edge in temp_edges:
            self.add_edge(edge[1], edge[0])
    """
    Resets vertices at the end. 

    :param: None
    :return: None
    """
    def reset_finished(self):
        for vert in self.vertices:
            vert.unfinish()
    """
    Computes and returns the components that are connected recursively. 

    :param: None
    :return: connected components (combined nodes)
    """
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
                connected_components.append(self.collect_component_nodes_iter(node))

        self.reverse_edges()
        return connected_components

    def __str__(self):
        graph_str = ""
        for vert in self.vertices:
            graph_str += str(vert) + "\n"
        return graph_str


class Node:
    __slots__ = "node_id", "value", "connections", "_visited", "finish_order", "finished"
    """
    Initializes node. 

    :param: value
    :return: None
    """
    def __init__(self, val, nid=-1) -> None:
        self.connections = []
        self.value = val
        self._visited = False
        self.finish_order = None
        self.node_id = nid
        self.finished = False
    """
    Sets node as unfinished. 

    :param: None
    :return: None
    """
    def unfinish(self):
        self.finished = False
    """
    Resets the array containing nodes connections. 

    :param: None
    :return: None
    """
    def reset_connections(self):
        self.connections = []
    """
    Sets order for nodes. 

    :param: order
    :return: None
    """
    def set_order(self, order):
        self.finish_order = order
    """
    Add an edge between two nodes. 

    :param: other node to connect current node to.
    :return: None
    """
    def add_edge(self, other_node):
        self.connections.append(other_node)
    """
    Marks visited nodes. 

    :param: None
    :return: None
    """
    def mark_visited(self):
        self._visited = True
    """
    Sets nodes to finished. 

    :param: None
    :return: None
    """
    def finish(self):
        self.finished = True
    """
    Checks whether a node has been visited already. 

    :param: None 
    :return: True if it has been visited. False otherwise
    """
    def is_visited(self):
        return self._visited
    """
    Checks wehther node has been finished. 

    :param: None
    :return: True if it has been finished. False otherwise
    """
    def is_finished(self):
        return self.finished

    def __str__(self):
        node_str = str(self.value) + " : "
        connected_nodes = []
        for connection in self.connections:
            connected_nodes.append(str(connection.value))

        node_str += ", ".join(connected_nodes)
        return node_str


class Edge:
    __slots__ = "from_node", "to_node", "weight"
    """
    Initializes an egde. 

    :param: node of origin and node to destination.
    :return: None
    """
    def __init__(self, from_node, to_node, weight) -> None:
        self.from_node = from_node
        self.to_node = to_node
"""
Processes input. 

:param: None.
:return: graph formed from given input.
"""

def process_input():
    num_nodes = int(input())

    graph = Graph()

    nodes = []
    for node_idx in range(num_nodes):
        node = Node(node_idx + 1)
        nodes.append(node)
        graph.add_node(node)

    for node_idx in range(num_nodes):
        line = input()
        connected_to_node_ids = [int(x) for x in line.split() if int(x) != 0]

        for idx in connected_to_node_ids:
            graph.add_edge(nodes[node_idx], nodes[idx - 1])

    return graph

"""
Runs a test from the file and prints "YES" if the length of 
the connected components equals 1 (or NO otherwise)

:param: None.
:return: None.
"""
def test_from_file():
    g = process_input()
    components = g.compute_connected_components()

    #
    # base case where the graph is already strongly connected
    #
    if len(components) == 1:
        print("YES")
        return

    #
    # Create the new graph from the components
    #
    cc_nodes = []
    graph_cc = Graph()
    component_nodes_mapper = [0] * len(g.vertices)
    for idx, comp in enumerate(components):
        comp_name = "".join([str(x.value) for x in comp])
        node = Node(comp_name, idx)
        cc_nodes.append(node)
        graph_cc.add_node(node)
        for elem in comp:
            component_nodes_mapper[elem.value - 1] = idx

    for vert in g.vertices:
        for connection in vert.connections:
            from_node = component_nodes_mapper[vert.value - 1]
            to_node = component_nodes_mapper[connection.value - 1]

            if from_node != to_node:
                graph_cc.add_edge_unique(cc_nodes[from_node], cc_nodes[to_node])

    #
    # find the root of the topology
    #
    incoming_count = [0] * len(graph_cc.vertices)

    for edge in graph_cc.edges:
        edge_to = edge[1]
        incoming_count[edge_to.node_id] += 1

    root = [node for node in graph_cc.vertices if incoming_count[node.node_id] == 0][0]

    #
    # find the END node
    # END node is the node that finishes first in a recursive DFS
    #
    graph_cc.dfs_rec_with_order(root)
    first_finish_node = graph_cc.dfs_finish_order[0]

    #
    # add edge from the END component to the ROOT component
    #
    graph_cc.add_edge(first_finish_node, root)

    #
    # find the number of components after adding the edge
    #
    cc_components = graph_cc.compute_connected_components()

    #
    # test if adding one edge to the graph connects all the components
    #
    if len(cc_components) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    test_from_file()

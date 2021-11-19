"""
This is a turn on Bellman Ford. With the assumption that there are no negative weight edges.
"""

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


def process_input():
    vertices = int(input())
    num_vials = int(input())
    total_time = int(input())
    num_edges = int(input())

    graph = Graph()
    nodes = []
    for idx in range(vertices):
        graph.add_vertex(Node(idx))

    for _ in range(num_edges):
        (start_index, end_index, weight) = (y for y in [int(x) for x in input().strip().split()])
        graph.add_edge_unique_by_index(start_index, end_index, weight, True)

    return graph, num_vials, total_time


def bellman_ford(graph, source):
    source_weight_array = []

    #
    # initialize
    #
    for vert in graph.vertices:
        if vert is source:
            source_weight_array.append((-1, 0))
        else:
            source_weight_array.append((-1, -1))

    num_changes_prev_iterations = RIDICULOUSLY_LARGE_NUMBER

    for itter_count in range(len(graph.vertices)):
        if num_changes_prev_iterations == 0:
            break
        num_changes_prev_iterations = 0
        for edge in graph.edges_by_index:
            source_index = edge[0]
            source_dist = source_weight_array[source_index][1]
            if source_dist != -1:
                dest_index = edge[1]
                dest_dist = source_weight_array[dest_index][1]
                if dest_dist == -1 or dest_dist > source_dist + edge[2]:
                    dest_dist = source_dist + edge[2]
                    source_weight_array[dest_index] = (source_index, dest_dist)  # (parent, distance)
                    num_changes_prev_iterations += 1

    return source_weight_array


def bellman_ford_with_num_edge_limit_and_total_length_limit(graph, source, total_vials, total_time):
    source_weight_array = []
    final_dest_index = len(graph.vertices) - 1
    final_source_index = 0

    #
    # initialize
    #
    for vert in graph.vertices:
        if vert is source:
            source_weight_array.append((-1, 0, 0))
        else:
            source_weight_array.append((-1, -1, 0))  # (parent, distance, num_vials|edges)

    num_changes_prev_iterations = RIDICULOUSLY_LARGE_NUMBER

    for itter_count in range(len(graph.vertices) - 1):
        if num_changes_prev_iterations == 0:
            break
        dist_to_final_dest = source_weight_array[-1][1]
        num_vials_to_final_dest = source_weight_array[-1][2]
        dest_is_reachable = dist_to_final_dest != -1 and num_vials_to_final_dest <= total_vials and dist_to_final_dest < total_time
        if dest_is_reachable:
            break
        num_changes_prev_iterations = 0
        for edge in graph.edges_by_index:
            source_index = edge[0]
            source_dist = source_weight_array[source_index][1]
            if source_dist != -1:
                dest_index = edge[1]
                dest_dist = source_weight_array[dest_index][1]
                num_vials_to_source = source_weight_array[source_index][2]
                num_vials_to_dest = num_vials_to_source + (
                    0 if (dest_index == final_dest_index or dest_index == final_source_index) else 1)
                new_dest_dist = source_dist + edge[2]
                gain_in_dist = dest_dist > new_dest_dist and num_vials_to_dest <= total_vials
                gain_in_vials = new_dest_dist <= total_time and num_vials_to_dest < source_weight_array[dest_index][2]
                gain_from_init = dest_dist == -1 and new_dest_dist <= total_time and num_vials_to_dest <= total_vials
                if gain_from_init or gain_in_dist or gain_in_vials:
                    dest_dist = source_dist + edge[2]
                    source_weight_array[dest_index] = (source_index, dest_dist, num_vials_to_dest)  # (parent, distance)
                    num_changes_prev_iterations += 1

    return source_weight_array


def bellman_ford_v2(graph, source, total_vials, total_time):
    source_weight_array = []
    final_dest_index = len(graph.vertices) - 1
    final_source_index = 0

    #
    # initialize
    #
    for vert in graph.vertices:
        if vert is source:
            source_weight_array.append(((-1, 0, 0), (-1, 0, 0)))
        else:
            source_weight_array.append(((-1, -1, 0), (-1, -1, 0)))  # (parent, distance, num_vials|edges)

    num_changes_prev_iterations = RIDICULOUSLY_LARGE_NUMBER

    for itter_count in range(len(graph.vertices) - 1):
        if num_changes_prev_iterations == 0:
            break

        dist_to_final_dest = source_weight_array[-1][1][1]
        num_vials_to_final_dest = source_weight_array[-1][1][2]
        dest_is_reachable = dist_to_final_dest != -1 and num_vials_to_final_dest <= total_vials and dist_to_final_dest < total_time
        if dest_is_reachable:
            break

        #
        # reset source weight array
        #
        for source_weight_index in range(len(source_weight_array)):
            source_weight_array[source_weight_index] = (
                source_weight_array[source_weight_index][1], source_weight_array[source_weight_index][1])

        num_changes_prev_iterations = 0
        for edge in graph.edges_by_index:
            source_index = edge[0]
            source_dist = source_weight_array[source_index][0][1]
            if source_dist != -1:
                dest_index = edge[1]
                dest_dist = source_weight_array[dest_index][0][1]
                num_vials_to_source = source_weight_array[source_index][0][2]
                num_vials_to_dest = num_vials_to_source + (
                    0 if (dest_index == final_dest_index or dest_index == final_source_index) else 1)
                new_dest_dist = source_dist + edge[2]
                gain_in_dist = dest_dist > new_dest_dist and num_vials_to_dest <= total_vials
                # gain_in_vials = new_dest_dist <= total_time and num_vials_to_dest < source_weight_array[dest_index][1][
                #     2]
                gain_from_init = dest_dist == -1 and new_dest_dist <= total_time and num_vials_to_dest <= total_vials
                if gain_from_init or gain_in_dist:  # or gain_in_vials:
                    dest_dist = source_dist + edge[2]
                    source_weight_array[dest_index] = (source_weight_array[dest_index][0], (
                        source_index, dest_dist, num_vials_to_dest))  # (parent, distance)
                    num_changes_prev_iterations += 1

    return source_weight_array


def main():
    maze, num_vials, total_time = process_input()
    # print("\nnum vials = " + str(num_vials) + "\ntotal time = " + str(total_time) + "\n")
    start_node = maze.vertices[0]
    end_node = maze.vertices[-1]
    weighted_paths = bellman_ford_v2(maze, start_node, num_vials, total_time)

    dest_to_end_node = weighted_paths[-1][1][1]
    if dest_to_end_node == -1:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()

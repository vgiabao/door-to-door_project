from copy import deepcopy

class Graph:
    def __init__(self):
        self.nodes = []

    def __str__(self):
        return '\n'.join([str(node) for node in self.nodes])

    def add_node(self, node):
        self.nodes.append(node)

    def find_shortest_path(self):
        original = deepcopy(self)
        solution = Graph()
        solution.add_node(original.nodes.pop(0))
        total_len = 0
        while original.nodes:
            distance = [solution.nodes[-1].get_distance(node) for node in
                        original.nodes]
            total_len += min(distance)
            solution.add_node(original.nodes.pop(distance.index(
                min(distance))))
            if len(original.nodes) == 1:
                total_len += solution.nodes[0].get_distance(original.nodes[0])
                solution.add_node(original.nodes[0])
                return solution, total_len
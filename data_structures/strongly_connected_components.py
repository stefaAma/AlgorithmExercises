import csv


class DuplicateException(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self):
        return "DuplicateException: " + self._message


class VertexNotFoundException(Exception):
    def __init__(self, vertex):
        super().__init__()
        self._vertex = str(vertex)

    def __str__(self):
        return f"VertexNotFoundException: vertex with id value of -- {self._vertex} -- cannot be found!"


class Node(object):
    def __init__(self, value):
        self._value = value
        self._nodes = []
        self._scc_node = None
        self._scc_nodes = []
        self._discovery_time = 0
        self._completion_time = 0

    @property
    def value(self):
        return self._value

    @property
    def nodes(self):
        return self._nodes

    @property
    def scc_node(self):
        return self._scc_node

    @scc_node.setter
    def scc_node(self, scc_node):
        self._scc_node = scc_node

    @property
    def scc_nodes(self):
        return self._scc_nodes

    @property
    def discovery_time(self):
        return self._discovery_time

    @discovery_time.setter
    def discovery_time(self, discovery_time):
        self._discovery_time = discovery_time

    @property
    def completion_time(self):
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        self._completion_time = completion_time

    def __str__(self):
        return f" -vertex {str(self._value)}- "


class Graph(object):
    def __init__(self):
        self._vertices = []

    @property
    def vertices(self):
        return self._vertices

    def find(self, value):
        length = len(self._vertices)
        i = 0
        while i < length:
            if self._vertices[i].value == value:
                return self._vertices[i]
            i += 1
        raise VertexNotFoundException(value)

    def __str__(self):
        return str([str(vertex) for vertex in self.vertices])


def map_vertex(mapped_vertices, vertex):
    if vertex in mapped_vertices:
        raise DuplicateException(f"There is a vertex -- {str(vertex)} -- mapped at least twice!")
    mapped_vertices.append(vertex)


def read_directed_graph():
    directed_graph = Graph()
    with open("graphs/directed_graph.csv") as input_file:
        csv_input = csv.reader(input_file)
        mapped_vertices = []
        for line in csv_input:
            main_vertex = None
            for index, vertex in enumerate(line):
                vertex = int(vertex)
                if index == 0:
                    map_vertex(mapped_vertices, vertex)
                    try:
                        existing_vertex = directed_graph.find(vertex)
                        main_vertex = existing_vertex
                    except VertexNotFoundException:
                        main_vertex = Node(vertex)
                        directed_graph.vertices.append(main_vertex)
                else:
                    new_vertex = None
                    try:
                        new_vertex = directed_graph.find(vertex)
                    except VertexNotFoundException:
                        new_vertex = Node(vertex)
                        directed_graph.vertices.append(new_vertex)
                    finally:
                        main_vertex.nodes.append(new_vertex)
    print(str(directed_graph))
    return directed_graph


def recursive_dfs(node, vertices, time):
    time += 1
    node.discovery_time = time
    adjacent_nodes = node.nodes
    for adjacent_node in adjacent_nodes:
        if adjacent_node.discovery_time == 0:
            time = recursive_dfs(adjacent_node, vertices, time)
    time += 1
    node.completion_time = time
    vertices.insert(0, node.value)
    return time


def dfs_search(direct_graph):
    vertices = []
    time = 0
    for vertex in direct_graph.vertices:
        if vertex.discovery_time == 0:
            time = recursive_dfs(vertex, vertices, time)
    return vertices


def transposed_graph(direct_graph):
    transposed_direct_graph = Graph()
    for vertex in direct_graph.vertices:
        # current_vertex = None
        try:
            current_vertex = transposed_direct_graph.find(vertex.value)
        except VertexNotFoundException:
            current_vertex = Node(vertex.value)
            transposed_direct_graph.vertices.append(current_vertex)
        for adjacent_node in vertex.nodes:
            other_vertex = None
            try:
                other_vertex = transposed_direct_graph.find(adjacent_node.value)
            except VertexNotFoundException:
                other_vertex = Node(adjacent_node.value)
                transposed_direct_graph.vertices.append(other_vertex)
            finally:
                other_vertex.nodes.append(current_vertex)
    return transposed_direct_graph


def create_scc_graph_node(current_vertex, scc_graph_node, time):
    time += 1
    current_vertex.discovery_time = time
    scc_graph_node.scc_nodes.append(current_vertex)
    current_vertex.scc_node = scc_graph_node
    adjacent_vertices = current_vertex.nodes
    for adjacent_node in adjacent_vertices:
        if adjacent_node.completion_time != 0:
            adjacent_scc_graph_node = adjacent_node.scc_node
            if scc_graph_node not in adjacent_scc_graph_node.nodes:
                adjacent_scc_graph_node.nodes.append(scc_graph_node)
        elif adjacent_node.discovery_time == 0:
            time = create_scc_graph_node(adjacent_node, scc_graph_node, time)
    time += 1
    current_vertex.completion_time = time
    return time


def create_scc_graph(transposed_direct_graph, vertices):
    scc_graph = Graph()
    i = 0
    time = 0
    for vertex in vertices:
        current_vertex = transposed_direct_graph.find(vertex)
        if current_vertex.discovery_time == 0:
            i += 1
            scc_graph_node = Node(i)
            scc_graph.vertices.append(scc_graph_node)
            time = create_scc_graph_node(current_vertex, scc_graph_node, time)
    return scc_graph


if __name__ == "__main__":
    original_graph = read_directed_graph()
    vs = dfs_search(original_graph)
    t_graph = transposed_graph(original_graph)
    result_graph = create_scc_graph(t_graph, vs)

    for v in result_graph.vertices:
        print(f"{str(v)}")
        print(" references")
        for original_vertex in v.scc_nodes:
            print(f"        {str(original_vertex)}")
        print(" points to:")
        for adj_vertex in v.nodes:
            print(f"        {str(adj_vertex)}")

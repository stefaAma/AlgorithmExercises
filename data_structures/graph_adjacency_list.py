import csv


class DuplicateException(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self):
        return "DuplicateException: " + self._message


class Node(object):
    def __init__(self, key):
        self._key = key
        self._next = None

    @property
    def key(self):
        return self._key

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node


class Graph(object):
    def __init__(self, directed):
        self._adjacency_list = []
        self._vertices = []
        self._map_vertex_to_pos = {}
        self._map_pos_to_vertex = {}
        self._directed = directed
        if directed is True:
            self._type = "Directed"
        else:
            self._type = "Undirected"

    @property
    def adjacency_list(self):
        return self._adjacency_list

    @adjacency_list.setter
    def adjacency_list(self, adjacency_list):
        self._adjacency_list = adjacency_list

    @property
    def directed(self):
        return self._directed

    @property
    def type(self):
        return self._type

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        self._vertices = vertices

    @property
    def map_vertex_to_pos(self):
        return self._map_vertex_to_pos

    @property
    def map_pos_to_vertex(self):
        return self._map_pos_to_vertex

    def __str__(self):
        return self._type + " Graph\n" + "vertices: " + str(self._vertices)


def map_vertex(directed_graph, mapped_vertices, vertex, pos):
    if vertex in mapped_vertices:
        raise DuplicateException(f"There is a vertex -- {str(vertex)} -- mapped at least twice!")
    mapped_vertices.append(vertex)
    directed_graph.map_vertex_to_pos[vertex] = pos
    directed_graph.map_pos_to_vertex[pos] = vertex


def read_directed_graph():
    with open("graphs/directed_graph.csv") as input_file:
        csv_input = csv.reader(input_file)
        directed_graph = Graph(True)
        pos = 0
        mapped_vertices = []
        for line in csv_input:
            if len(line) > 1:
                for index, vertex in enumerate(line):
                    vertex = int(vertex)
                    if index == 0:
                        map_vertex(directed_graph, mapped_vertices, vertex, pos)
                        directed_graph.adjacency_list.append(None)
                    else:
                        vertex_node = Node(vertex)
                        vertex_node.next = directed_graph.adjacency_list[pos]
                        directed_graph.adjacency_list[pos] = vertex_node
                    if vertex not in directed_graph.vertices:
                        directed_graph.vertices.append(vertex)
                pos += 1
            else:
                vertex = int(line[0])
                directed_graph.vertices.append(vertex)
    print(f"Vertices: {str(directed_graph.vertices)}")
    return directed_graph


def find_connected_vertices(directed_graph):
    connected_vertices = []
    for pos, node in enumerate(directed_graph.adjacency_list):
        vertex = directed_graph.map_pos_to_vertex[pos]
        if vertex not in connected_vertices:
            connected_vertices.append(vertex)
        while node is not None:
            if node.key not in connected_vertices:
                connected_vertices.append(node.key)
            node = node.next
    connected_vertices.sort()
    return connected_vertices


def position_mapping(undirected_graph, connected_vertices):
    for pos, vertex in enumerate(connected_vertices):
        undirected_graph.map_pos_to_vertex[pos] = vertex
        undirected_graph.map_vertex_to_pos[vertex] = pos


def undirected_adjacency_list_fix(undirected_graph):
    pos = 0
    while pos < len(undirected_graph.adjacency_list):
        if undirected_graph.adjacency_list[pos] is None:
            del_vertex = undirected_graph.map_pos_to_vertex[pos]
            del undirected_graph.map_vertex_to_pos[del_vertex]
            del undirected_graph.map_pos_to_vertex[pos]
            del undirected_graph.adjacency_list[pos]
            for x in range(pos, len(undirected_graph.adjacency_list)):
                vertex = undirected_graph.map_pos_to_vertex[x + 1]
                del undirected_graph.map_vertex_to_pos[vertex]
                del undirected_graph.map_pos_to_vertex[x + 1]
                undirected_graph.map_pos_to_vertex[x] = vertex
                undirected_graph.map_vertex_to_pos[vertex] = x
        else:
            pos += 1


def directed_to_undirected(directed_graph):
    undirected_graph = Graph(False)
    undirected_graph.vertices = directed_graph.vertices.copy()
    connected_vertices = find_connected_vertices(directed_graph)
    undirected_graph.adjacency_list = [None for x in connected_vertices]
    position_mapping(undirected_graph, connected_vertices)
    for directed_pos, directed_node in enumerate(directed_graph.adjacency_list):
        vertex = directed_graph.map_pos_to_vertex[directed_pos]
        undirected_pos = undirected_graph.map_vertex_to_pos[vertex]
        while directed_node is not None:
            if directed_node.key != vertex:
                if directed_node.key > vertex:
                    new_node = Node(directed_node.key)
                    new_node.next = undirected_graph.adjacency_list[undirected_pos]
                    undirected_graph.adjacency_list[undirected_pos] = new_node
                else:
                    minor_vertex_pos = undirected_graph.map_vertex_to_pos[directed_node.key]
                    minor_vertex_node = undirected_graph.adjacency_list[minor_vertex_pos]
                    while minor_vertex_node is not None and minor_vertex_node.key != vertex:
                        minor_vertex_node = minor_vertex_node.next
                    if minor_vertex_node is None:
                        new_node = Node(vertex)
                        new_node.next = undirected_graph.adjacency_list[minor_vertex_pos]
                        undirected_graph.adjacency_list[minor_vertex_pos] = new_node
            directed_node = directed_node.next
    undirected_adjacency_list_fix(undirected_graph)
    return undirected_graph


def print_adjacency_list(graph):
    print(f"-- Output for an {graph.type} Graph --", end="")
    for pos, node in enumerate(graph.adjacency_list):
        vertex = graph.map_pos_to_vertex[pos]
        print(f'\n{str(vertex)} to: ', end="")
        while node is not None:
            print(f"{str(node.key)} ", end="")
            node = node.next


if __name__ == "__main__":
    try:
        d_graph = read_directed_graph()
    except DuplicateException as e:
        print(e)
    else:
        u_graph = directed_to_undirected(d_graph)
        print_adjacency_list(u_graph)

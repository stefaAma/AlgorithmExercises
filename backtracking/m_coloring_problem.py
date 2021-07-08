class GraphNode(object):
    def __init__(self, number):
        self._number = number
        self._color = None
        self._sibling_nodes = []

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def sibling_nodes(self):
        return self._sibling_nodes

    @property
    def number(self):
        return self._number

    def link(self, node):
        self._sibling_nodes.append(node)
        if self not in node.sibling_nodes:
            node.link(self)


colors = ["red", "white", "green"]


def color_graph(current_node, color):
    copy_array = colors.copy()
    copy_array.remove(color)
    current_node.color = color
    colors_left = len(copy_array)
    num_siblings = len(current_node.sibling_nodes)
    i = 0
    is_assigned = True
    siblings = current_node.sibling_nodes
    while is_assigned and i < num_siblings:
        is_assigned = False
        if siblings[i].color is None:
            j = 0
            while is_assigned is False and j < colors_left:
                is_assigned = color_graph(siblings[i], copy_array[j])
                j += 1
        else:
            if siblings[i].color != color:
                is_assigned = True
        i += 1
    if is_assigned is False:
        current_node.color = None
    return is_assigned


def update_colors(array, sibling_node):
    if sibling_node.color in array:
        array.remove(sibling_node.color)


def color_graph_optimized(current_node):
    num_siblings = len(current_node.sibling_nodes)
    i = 0
    copy_array = colors.copy()
    while i < num_siblings:
        update_colors(copy_array, current_node.sibling_nodes[i])
        i += 1
    if len(copy_array) == 0:
        return False
    else:
        current_node.color = copy_array[0]
        i = 0
        result = True
        while result and i < num_siblings:
            if current_node.sibling_nodes[i].color is None:
                result = color_graph_optimized(current_node.sibling_nodes[i])
            i += 1
        return result


# BFS searching_algorithm
def bfs_printing(first_node):
    queue = [first_node]
    visited_nodes = []
    while len(queue) > 0:
        current_node = queue.pop(0)
        print("Node (" + str(current_node.number) + ") - Color (" + current_node.color + ")")
        visited_nodes.append(current_node.number)
        siblings = current_node.sibling_nodes
        num_siblings = len(siblings)
        i = 0
        while i < num_siblings:
            if siblings[i].number not in visited_nodes and siblings[i] not in queue:
                queue.append(siblings[i])
            i += 1


def execute_algorithm():
    # node creation
    node_one = GraphNode(1)
    node_two = GraphNode(2)
    node_three = GraphNode(3)
    node_four = GraphNode(4)
    node_five = GraphNode(5)
    node_six = GraphNode(6)
    node_seven = GraphNode(7)
    node_eight = GraphNode(8)
    node_nine = GraphNode(9)
    node_ten = GraphNode(10)

    #node_eleven = GraphNode(11)
    #node_eleven.link(node_nine)
    #node_eleven.link(node_ten)
    #node_eleven.link(node_four)
    #node_eleven.link(node_one)

    node_one.link(node_two)
    node_one.link(node_five)
    node_two.link(node_three)
    node_two.link(node_five)
    node_three.link(node_four)
    node_three.link(node_five)
    node_four.link(node_five)
    # node linking
    #node_one.link(node_two)
    #node_one.link(node_three)
    #node_one.link(node_four)
    #node_two.link(node_five)
    #node_two.link(node_nine)
    #node_three.link(node_seven)
    #node_three.link(node_eight)
    #node_four.link(node_six)
    #node_four.link(node_ten)
    #node_five.link(node_six)
    #node_five.link(node_eight)
    #node_six.link(node_seven)
    #node_seven.link(node_nine)
    #node_eight.link(node_ten)
    #node_nine.link(node_ten)
    if color_graph_optimized(node_one) is True:
        bfs_printing(node_one)
    else:
        print("The given graph CAN'T BE coloured!")


execute_algorithm()

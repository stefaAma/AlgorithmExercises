class DirectedGraphNode(object):
    def __init__(self, node_id):
        self._id = node_id
        self._child_nodes = []
        self._in_the_cycle = False

    @property
    def id(self):
        return self._id

    @property
    def child_nodes(self):
        return self._child_nodes

    @property
    def in_the_cycle(self):
        return self._in_the_cycle

    @in_the_cycle.setter
    def in_the_cycle(self, value):
        self._in_the_cycle = value

    def link(self, node):
        self._child_nodes.append(node)


def is_acyclic(current_node):
    if current_node.in_the_cycle is True:
        return False
    current_node.in_the_cycle = True
    for child_node in current_node.child_nodes:
        if is_acyclic(child_node) is False:
            return False
    current_node.in_the_cycle = False
    return True


def execute_algorithm():
    node_one = DirectedGraphNode(1)
    node_two = DirectedGraphNode(2)
    node_three = DirectedGraphNode(3)
    node_four = DirectedGraphNode(4)

    # node linking

    node_one.link(node_two)
    node_one.link(node_three)
    node_two.link(node_four)
    node_three.link(node_two)
    node_three.link(node_four)
    #node_three.link(node_three)
    #node_four.link(node_one)

    if is_acyclic(node_one) is True:
        print("The graph is acyclic!")
    else:
        print("The graph is NOT acyclic!")


execute_algorithm()

class UndirectedGraphNode(object):
    def __init__(self, node_id):
        self._id = node_id
        self._in_the_cycle = False
        self._sibling_nodes = []

    @property
    def id(self):
        return self._id

    @property
    def in_the_cycle(self):
        return self._in_the_cycle

    @in_the_cycle.setter
    def in_the_cycle(self, value):
        self._in_the_cycle = value

    @property
    def sibling_nodes(self):
        return self._sibling_nodes

    def link(self, node):
        self._sibling_nodes.append(node)
        if self not in node.sibling_nodes:
            node.link(self)


def is_acyclic(current_node, previous_node):
    if current_node.in_the_cycle is True:
        return False
    current_node.in_the_cycle = True
    siblings = current_node.sibling_nodes.copy()
    if previous_node is not None:
        siblings.remove(previous_node)
    for sibling in siblings:
        result = is_acyclic(sibling, current_node)
        if result is False:
            return False
    # current_node.in_the_cycle = False
    return True


def execute_algorithm():
    node_one = UndirectedGraphNode(1)
    node_two = UndirectedGraphNode(2)
    node_three = UndirectedGraphNode(3)
    node_four = UndirectedGraphNode(4)

    # node linking

    node_one.link(node_two)
    node_one.link(node_three)
    node_three.link(node_four)
    node_three.link(node_three)

    if is_acyclic(node_one, None) is True:
        print("The graph is acyclic!")
    else:
        print("The graph is NOT acyclic!")


execute_algorithm()

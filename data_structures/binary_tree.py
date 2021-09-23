class BinaryTreeNode(object):
    def __init__(self, key_value):
        self._parent = None
        self._left_child = None
        self._right_child = None
        self._key_value = key_value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, left_child):
        self._left_child = left_child

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, right_child):
        self._right_child = right_child

    @property
    def key_value(self):
        return self._key_value

    def __str__(self):
        return f"Node Value - {self._key_value}"

    def __del__(self):
        print(f"-- Node {self._key_value} deleted --")


class BinaryTree(object):
    def __init__(self, root=None):
        self._root = root

    def insert_node(self, new_node):
        parent_node = None
        current_node = self._root
        while current_node is not None:
            parent_node = current_node
            if current_node.key_value < new_node.key_value:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        if parent_node is None:
            self._root = new_node
        else:
            new_node.parent = parent_node
            if parent_node.key_value < new_node.key_value:
                parent_node.right_child = new_node
            else:
                parent_node.left_child = new_node

    def find_node(self, key):
        current_node = self._root
        while current_node is not None and current_node.key_value != key:
            if current_node.key_value >= key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return current_node

    @staticmethod
    def find_minimum(starting_node):
        if starting_node is None:
            return None
        current_node = starting_node
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node

    @staticmethod
    def find_maximum(starting_node):
        if starting_node is None:
            return None
        current_node = starting_node
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node

    @staticmethod
    def predecessor(node):
        predecessor = BinaryTree.find_maximum(node.left_child)
        if predecessor is not None:
            return predecessor
        current_node = node
        predecessor = node.parent
        while predecessor is not None and predecessor.left_child == current_node:
            current_node = predecessor
            predecessor = predecessor.parent
        return predecessor

    @staticmethod
    def successor(node):
        successor = BinaryTree.find_minimum(node.right_child)
        if successor is not None:
            return successor
        current_node = node
        successor = node.parent
        while successor is not None and successor.right_child == current_node:
            current_node = successor
            successor = successor.parent
        return successor

    def absolute_minimum(self):
        return BinaryTree.find_minimum(self._root)

    def absolute_maximum(self):
        return BinaryTree.find_maximum(self._root)

    # I have chosen to implement an iterative version for exercise purposes
    def print_tree_nodes(self):
        if self._root is None:
            print("The tree doesn't have any elements!")
        else:
            current_node = self._root
            last_node = current_node.parent
            while current_node is not None:
                if last_node is current_node.parent:
                    last_node = current_node
                    if current_node.left_child is not None:
                        current_node = current_node.left_child
                    else:
                        print(current_node)
                        if current_node.right_child is not None:
                            current_node = current_node.right_child
                        else:
                            current_node = current_node.parent
                elif last_node is current_node.left_child:
                    last_node = current_node
                    print(current_node)
                    if current_node.right_child is not None:
                        current_node = current_node.right_child
                    else:
                        current_node = current_node.parent
                else:
                    last_node = current_node
                    current_node = current_node.parent

    def link_to_father_node(self, to_be_replaced, replacement):
        if to_be_replaced.parent is None:
            self._root = replacement
        elif to_be_replaced.parent.left_child is to_be_replaced:
            to_be_replaced.parent.left_child = replacement
        else:
            to_be_replaced.parent.right_child = replacement
        if replacement is not None:
            replacement.parent = to_be_replaced.parent

    def delete_node(self, node):
        if node.left_child is None:
            self.link_to_father_node(node, node.right_child)
        elif node.right_child is None:
            self.link_to_father_node(node, node.left_child)
        else:
            predecessor = BinaryTree.predecessor(node)
            if predecessor.parent is not node:
                self.link_to_father_node(predecessor, predecessor.left_child)
                predecessor.left_child = node.left_child
                predecessor.left_child.parent = predecessor
            predecessor.right_child = node.right_child
            predecessor.right_child.parent = predecessor
            self.link_to_father_node(node, predecessor)


def create_binary_tree():
    root_node = input("Insert the root node value:  ")
    tree_nodes = []
    insert = input("Do you want to insert another element? (Y = yes/ y = yes /anything else = no):  ")
    while insert == "Y" or insert == "y":
        val = input("Insert Value:  ")
        tree_nodes.append(int(val))
        insert = input("Do you want to insert another element? (Y = yes/ y = yes /anything else = no):  ")
    binary_tree = BinaryTree(BinaryTreeNode(int(root_node)))
    for key in tree_nodes:
        binary_tree.insert_node(BinaryTreeNode(key))
    return binary_tree


if __name__ == "__main__":
    bt = create_binary_tree()
    find_insert = input("Do you want to insert a value to find? (Y = yes/ y = yes /anything else = no):  ")
    while find_insert == "Y" or find_insert == "y":
        val_to_find = input("Insert a value to find:  ")
        found_node = bt.find_node(int(val_to_find))
        if found_node is not None:
            print(f"The predecessor of -- {found_node} -- is -- {BinaryTree.predecessor(found_node)} --")
            print(f"The successor of -- {found_node} -- is -- {BinaryTree.successor(found_node)} --\n")
            delete_insert = input("Do you want to delete this node? (Y = yes/ y = yes /anything else = no):  ")
            if delete_insert == "Y" or delete_insert == "y":
                bt.delete_node(found_node)
                del found_node
        else:
            print("The value isn't in the tree")
        find_insert = input("Do you want to insert another value to find? (Y = yes/ y = yes /anything else = no):  ")
    print("\nOUTPUT: ")
    print(f"The minimum value stored in the tree is {bt.absolute_minimum()}")
    print(f"The maximum value stored in the tree is {bt.absolute_maximum()}")
    print("\n -- The tree values in ascending order -- \n")
    bt.print_tree_nodes()

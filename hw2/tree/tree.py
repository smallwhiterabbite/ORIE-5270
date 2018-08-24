class Tree(object):

    def __init__(self, root):
        self.root = root
        self.height = self.get_height(root)
        # initialize tree_build structure of a list of list of "|"
        self.structure = [["|" for i in range(2**self.height-1)] for j in range(self.height)]

    def get_height(self, node):
        """
        Get the height of the tree
        :param node: init: root, the current node in recursive calls
        :return: the height of the tree, 0 if there is no root
        """
        while node is not None:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))
        return 0

    def build_tree(self, node, h, l, r):
        """
        Replace the structure field by recursively looking at each level of the tree
        :param node: init: root, current node in recursive step
        :param h: init: 0, row index
        :param l: init:0, the left boundary of current node
        :param r: init:2^h-2 the right boundary of current node, (l+r)/2 is the column index
        :return: A list of list with desired tree structure values
        """
        if node is not None:
            self.structure[h][int((l + r) / 2)] = node.value
            self.build_tree(node.left, h + 1, l, (l + r) / 2 - 1)
            self.build_tree(node.right, h + 1, (l + r) / 2 + 1, r)

    def print_tree(self):
        """
        Print out the tree built from build_tree
        :return: structured tree
        """
        self.build_tree(self.root, 0, 0, 2**self.height-1)
        for i in self.structure:
            print(i)
        return self.structure


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

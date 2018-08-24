import unittest
from tree.tree import Tree, Node


class Test(unittest.TestCase):

    def setUp(self):
        self.answer1 = [[1]]
        self.answer2 = [["|", "|", "|", 1, "|", "|", "|"],
                        ["|", 2, "|", "|", "|", "|", "|"],
                        [3, "|", "|", "|", "|", "|", "|"]]
        self.answer3 = [["|", "|", "|", 1, "|", "|", "|"],
                        ["|", 2, "|", "|", "|", 3, "|"],
                        [4, "|", 5, "|", 6, "|", 7]]
        self.answer4 = [["|", "|", "|", 7, "|", "|", "|"],
                        ["|", 9, "|", "|", "|", 6, "|"],
                        ["|", "|", 4, "|", 2, "|", "|"]]

    # test base case, only root in the tree
    def test1(self):
        a = Node(1, None, None)
        tree1 = Tree(a)
        assert tree1.print_tree() == self.answer1

    # test when there is only left child
    def test2(self):
        c = Node(3, None, None)
        b = Node(2, c, None)
        a = Node(1, b, None)
        tree2 = Tree(a)
        assert tree2.print_tree() == self.answer2

    # test for a full tree
    def test3(self):
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)
        g = Node(7, None, None)
        b = Node(2, d, e)
        c = Node(3, f, g)
        a = Node(1, b, c)
        tree3 = Tree(a)
        assert tree3.print_tree() == self.answer3

    # test for a full tree
    def test4(self):
        d = Node(4, None, None)
        e = Node(2, None, None)
        b = Node(9, None, d)
        c = Node(6, e, None)
        a = Node(7, b, c)
        tree4 = Tree(a)
        assert tree4.print_tree() == self.answer4

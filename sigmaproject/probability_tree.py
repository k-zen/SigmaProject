# -*- coding: utf-8 -*-


class Fraction(object):
    num: int = 0
    den: int = 0

    def __init__(self, num: int = 0, den: int = 0):
        self.num = num
        self.den = den

    def get_value_as_decimal(self) -> float:
        if self.den == 0:
            return 0.0

        return self.num / self.den

    def __repr__(self):
        return "{0}/{1}".format(self.num, self.den)


class Node(object):
    __node_id: int = 0
    __value: Fraction = Fraction(num=0, den=0)
    __children: [] = []

    def __init__(self, node_id: int, value: Fraction = Fraction(0, 0)):
        self.__node_id = node_id
        self.__value = value

    def get_node_id(self):
        return self.__node_id

    def get_value(self):
        return self.__value

    def get_children(self) -> []:
        return self.__children

    def set_value(self, new_value: Fraction):
        self.__value = new_value

    def add_children(self, children: []):
        self.__children = children
        return self

    def desc(self, indent: int):
        string: str = "{0}NODE {1} = {2} ({3})\n".format(
            "  " * indent,
            self.__node_id,
            self.__value.get_value_as_decimal(),
            self.__value
        )
        for child in self.__children:
            string += child.desc(indent + 1)

        return string


class ProbabilityTree(object):
    """
    A probability tree object. The tree is as follows:

                          |-- P(1/1)
                          | (Node 3)
               |-- P(1) --|
               | (Node 1) |-- P(2/1)
               |            (Node 4)
        P -----|
        (Root) |          |-- P(1/2)
               |          | (Node 5)
               |-- P(2) --|
                 (Node 2) |-- P(2/2)
                            (Node 6)
    """

    DEBUG = True
    """
    boolean: Flag to enable debug mode.
    """

    ROOT = 0
    NODE_1 = 1
    NODE_2 = 2
    NODE_3 = 3
    NODE_4 = 4
    NODE_5 = 5
    NODE_6 = 6

    def __init__(self):
        self.probability_tree: Node = Node(node_id=self.ROOT)

        init_methods = [
            self._init_sequence,
            self._init_failure
        ]

        for method in init_methods:
            try:
                method()
                break
            except AttributeError:
                continue

    def _init_sequence(self):
        self.probability_tree.add_children(
            [
                Node(node_id=self.NODE_1).add_children(
                    [
                        Node(node_id=self.NODE_3),
                        Node(node_id=self.NODE_4)
                    ]),
                Node(node_id=self.NODE_2).add_children(
                    [
                        Node(node_id=self.NODE_5),
                        Node(node_id=self.NODE_6)
                    ])
            ])

    def _init_failure(self):
        raise ValueError('None of the initialization methods worked.')

    def update_tree(self, node: Node, node_id: int, value: Fraction):
        child: Node
        for child in node.get_children():
            if child.get_node_id() == node_id:
                child.set_value(value)
            else:
                self.update_tree(child, node_id, value)

    def get_value_from_tree(self, node: Node, node_id: int) -> float:
        value: float = 0.0
        child: Node
        for child in node.get_children():
            if child.get_node_id() == node_id:
                return child.get_value().get_value_as_decimal()
            else:
                value += self.get_value_from_tree(child, node_id)

        return value

    def compute_tree(self):
        return

    def compute_prior(self):
        return

    def compute_likelihood(self):
        return

    def compute_posterior(self):
        return

    def print(self):
        print(self.probability_tree.desc(0).strip())

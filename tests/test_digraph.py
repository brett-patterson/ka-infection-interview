from unittest import TestCase

from ka_infection.di_graph import Node, NodeError


class TestDiGraph(TestCase):
    def test_create_node(self):
        data = 5
        node = Node(data)
        self.assertEqual(data, node.data())

        data = {'key': [1, 2, 3]}
        node = Node(data)
        self.assertEqual(data, node.data())

    def test_neighbors(self):
        node = Node(1)
        node_2 = Node(2)

        self.assertEqual(set(), node.neighbors())

        node.add_neighbor(node_2)
        self.assertEqual(set([node_2]), node.neighbors())

        node.add_neighbor(node_2)
        self.assertEqual(set([node_2]), node.neighbors())

        node.remove_neighbor(node_2)
        self.assertEqual(set(), node.neighbors())

        self.assertRaises(NodeError, lambda: node.remove_neighbor(node_2))

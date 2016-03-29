from unittest import TestCase

from ka_infection.graph import Node, NodeError


class TestGraph(TestCase):
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
        self.assertEqual(set([node]), node_2.neighbors())

        node.add_neighbor(node_2)
        self.assertEqual(set([node_2]), node.neighbors())
        self.assertEqual(set([node]), node_2.neighbors())

        node.remove_neighbor(node_2)
        self.assertEqual(set(), node.neighbors())
        self.assertEqual(set(), node_2.neighbors())

        node.remove_neighbor(node_2)
        self.assertEqual(set(), node.neighbors())
        self.assertEqual(set(), node_2.neighbors())

        self.assertRaises(NodeError, lambda: node.add_neighbor('str'))

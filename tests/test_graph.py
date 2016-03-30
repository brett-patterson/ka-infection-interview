from unittest import TestCase

from ka_infection.graph import Graph, Node, GraphError


class TestGraph(TestCase):
    def test_create_node(self):
        tag = 5
        node = Node(tag)
        self.assertEqual(tag, node.tag())

    def test_label_node(self):
        node = Node(1)

        self.assertRaises(KeyError, lambda: node.get_label('foo'))
        self.assertEqual(5, node.get_label('foo', 5))

        node.label('foo', 10)
        self.assertEqual(10, node.get_label('foo'))

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

        self.assertRaises(GraphError, lambda: node.add_neighbor('str'))

    def test_graph(self):
        adj_list = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}
        graph = Graph(adj_list)

        self.assertEquals(
            set([0, 1, 2, 3]),
            set([n.tag() for n in graph.nodes()])
        )

        self.assertEquals(2, graph.get_node(2).tag())

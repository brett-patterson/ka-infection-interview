from unittest import TestCase

from ka_infection.user import UserGraph, UserNode


class TestGraph(TestCase):
    def test_create_node(self):
        tag = 5
        node = UserNode(tag)
        self.assertEqual(tag, node.tag)

    def test_neighbors(self):
        node = UserNode(1)
        node_2 = UserNode(2)

        self.assertEqual(set(), node.neighbors)

        node.add_neighbor(node_2)
        self.assertEqual(set([node_2]), node.neighbors)
        self.assertEqual(set([node]), node_2.neighbors)

        node.add_neighbor(node_2)
        self.assertEqual(set([node_2]), node.neighbors)
        self.assertEqual(set([node]), node_2.neighbors)

        node.remove_neighbor(node_2)
        self.assertEqual(set(), node.neighbors)
        self.assertEqual(set(), node_2.neighbors)

        node.remove_neighbor(node_2)
        self.assertEqual(set(), node.neighbors)
        self.assertEqual(set(), node_2.neighbors)

        self.assertRaises(TypeError, lambda: node.add_neighbor('str'))

    def test_graph(self):
        adj_list = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}
        graph = UserGraph(adj_list)

        self.assertEquals(
            set([0, 1, 2, 3]),
            set([u.tag for u in graph.users()])
        )

        self.assertEquals(2, graph.get_user(2).tag)

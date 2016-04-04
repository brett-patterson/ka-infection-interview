from unittest import TestCase

from ka_infection.user import UserGraph
from ka_infection.infection import total_infection, limited_infection


class TestInfection(TestCase):
    def test_total_infection(self):
        adj_list = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}
        graph = UserGraph(adj_list)
        total_infection(graph.get_user(0))

        for tag in range(0, 3):
            self.assertTrue(graph.get_user(tag).metadata['infected'])

        self.assertFalse(graph.get_user(3).metadata.get('infected', False))

    def test_limited_infection(self):
        adj_list = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}

        graph = UserGraph(adj_list)
        limited_infection(graph.get_user(0), graph, 1)

        for tag in range(0, 3):
            self.assertFalse(
                graph.get_user(tag).metadata.get('infected', False)
            )
        self.assertTrue(graph.get_user(3).metadata['infected'])

        graph = UserGraph(adj_list)
        limited_infection(graph.get_user(0), graph, 3)

        for tag in range(0, 3):
            self.assertTrue(graph.get_user(tag).metadata['infected'])
        self.assertFalse(graph.get_user(3).metadata.get('infected', False))

        graph = UserGraph(adj_list)
        limited_infection(graph.get_user(0), graph, 2)

        users = [graph.get_user(t) for t in range(0, 3)]
        infected = filter(lambda u: u.metadata.get('infected', False), users)
        self.assertEquals(1, len(infected))

        graph = UserGraph(adj_list)
        limited_infection(graph.get_user(0), graph, 2, delta=1)

        for tag in range(0, 3):
            self.assertTrue(graph.get_user(tag).metadata['infected'])
        self.assertFalse(graph.get_user(3).metadata.get('infected', False))

from unittest import TestCase

from ka_infection.user import UserGraph
from ka_infection.infection import total_infection


class TestInfection(TestCase):
    def test_total_infection(self):
        adj_list = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}
        graph = UserGraph(adj_list)
        total_infection(graph.get_user(0))

        for tag in range(0, 3):
            self.assertTrue(graph.get_user(tag).metadata['infected'])

        self.assertFalse(graph.get_user(3).metadata.get('infected', False))

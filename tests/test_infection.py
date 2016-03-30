from unittest import TestCase

from ka_infection.graph import Graph
from ka_infection.infection import total_infection


def neighbor_by_tag(node, tag):
    """ A helper function to find a neighboring node by its tag.
    """
    for neighbor in node.neighbors():
        if neighbor.tag() == tag:
            return neighbor
    return None


class TestInfection(TestCase):
    def test_total_infection(self):
        adj_list = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}
        graph = Graph(adj_list)
        total_infection(graph.get_node(0))

        for tag in range(0, 3):
            self.assertTrue(graph.get_node(tag).get_label('infected'))

        self.assertFalse(graph.get_node(3).get_label('infected', False))

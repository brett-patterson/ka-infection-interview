""" An implementation of a directed graph. """


class NodeError(Exception):
    """ A custom exception type to throw from Node objects.
    """
    pass


class Node(object):
    """ A node within a directed, acyclic graph.
    """
    def __init__(self, data):
        """ Create a new Node.

        Parameters:
        -----------
        data : any
            Arbitrary data to associate with the node.

        """
        self._data = data
        self._neighbors = set()

    def __repr__(self):
        """ Get a human-readable string representation of the node.
        """
        return 'Node<{}>'.format(self._data)

    def data(self):
        """ Get the data associated with this node.
        """
        return self._data

    def neighbors(self):
        """ Get the set of all neighbors of this node.
        """
        return self._neighbors

    def add_neighbor(self, node):
        """ Add an edge from this node to another.

        Parameters:
        -----------
        node : Node
            The node to create an edge to.

        """
        self._neighbors.add(node)

    def remove_neighbor(self, node):
        """ Remove an edge between this node and another.
        """
        if node not in self._neighbors:
            raise NodeError('{} not found in neighbors of {}', node, self)

        self._neighbors.remove(node)

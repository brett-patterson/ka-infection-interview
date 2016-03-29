""" An implementation of an undirected graph. """


class NodeError(Exception):
    """ A custom exception type to throw from Node objects.
    """
    pass


class Node(object):
    """ A node within an undirected graph.
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
        if not isinstance(node, Node):
            raise NodeError('A node\'s neighbors must be instances of Node')

        node._neighbors.add(self)
        self._neighbors.add(node)

    def remove_neighbor(self, node):
        """ Remove an edge between this node and another.
        """
        if node in self._neighbors:
            self._neighbors.remove(node)

        if self in node._neighbors:
            node._neighbors.remove(self)

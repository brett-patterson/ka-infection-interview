class GraphError(Exception):
    """ A custom exception type to throw from Graph objects.
    """
    pass


class Graph(object):
    """ An undirected graph implementation.
    """
    def __init__(self, adj_list):
        """ Construct a graph from an adjacency list.

        Parameters:
        -----------
        adj_list : dict
            An adjacency list represented as a dictionary whose keys are
            node tags and values are a list of neighboring tags.
        """
        self._nodes = {tag: Node(tag) for tag in adj_list.keys()}
        for tag, node in self._nodes.items():
            for neighbor_tag in adj_list[tag]:
                node.add_neighbor(self._nodes[neighbor_tag])

    def get_node(self, tag):
        """ Get a node by its tag.
        """
        return self._nodes[tag]

    def nodes(self):
        """ Get a list of the nodes in the graph.
        """
        return self._nodes.values()


class Node(object):
    """ A node within an undirected graph.
    """
    def __init__(self, tag):
        """ Create a new Node.

        Parameters:
        -----------
        tag : any
            A unique tag for the node.

        """
        self._tag = tag
        self._labels = {}
        self._neighbors = set()

    def __repr__(self):
        """ Get a human-readable string representation of the node.
        """
        return 'Node<{}>'.format(self._tag)

    def tag(self):
        """ Get the tag for this node.
        """
        return self._tag

    def label(self, key, value):
        """ Label the node with a key and value.
        """
        self._labels[key] = value

    def get_label(self, key, default=None):
        """ Get the value of a label for the node.
        """
        if default is None:
            return self._labels[key]
        return self._labels.get(key, default)

    def remove_label(self, key):
        """ Remove a label from the node.
        """
        del self._labels[key]

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
            raise GraphError('A node\'s neighbors must be instances of Node')

        node._neighbors.add(self)
        self._neighbors.add(node)

    def remove_neighbor(self, node):
        """ Remove an edge between this node and another.
        """
        if node in self._neighbors:
            self._neighbors.remove(node)

        if self in node._neighbors:
            node._neighbors.remove(self)

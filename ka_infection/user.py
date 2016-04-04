
class UserGraph(object):
    """ An undirected graph implementation.
    """
    def __init__(self, adj_list, metadata={}):
        """ Construct a graph from an adjacency list.

        Parameters:
        -----------
        adj_list : dict
            An adjacency list represented as a dictionary whose keys are
            user tags and values are a list of neighboring tags.

        labels: dict
            An optional dictionary of initial metadata to apply to the users.
            The keys are user tags the values are dictionaries of metadata.
        """
        self._users = {tag: UserNode(tag) for tag in adj_list.keys()}
        for tag, node in self._users.items():
            for neighbor_tag in adj_list[tag]:
                node.add_neighbor(self.get_user(neighbor_tag))

        for tag, md in metadata.items():
            self.get_user(tag).metadata.update(md)

    def get_user(self, tag):
        """ Get a user by its tag.
        """
        return self._users[tag]

    def users(self):
        """ Get a list of the users in the graph.
        """
        return self._users.values()


class UserNode(object):
    """ A user node within an undirected user graph.
    """
    def __init__(self, tag):
        """ Create a new UserNode.

        Parameters:
        -----------
        tag : any
            A unique tag for the user.

        """
        self.tag = tag
        self.neighbors = set()
        self.metadata = {}

    def __eq__(self, other):
        """ Override the equals operator to be a comparison between tags.
        """
        if not isinstance(other, UserNode):
            return False

        return self.tag == other.tag

    def __repr__(self):
        """ Get a human-readable string representation of the user.
        """
        return 'User<{}>'.format(self.tag)

    def add_neighbor(self, node):
        """ Add an edge from this node to another.

        Parameters:
        -----------
        node : Node
            The node to create an edge to.

        """
        if not isinstance(node, UserNode):
            raise TypeError('A user\'s neighbors must be instances of User')

        node.neighbors.add(self)
        self.neighbors.add(node)

    def remove_neighbor(self, node):
        """ Remove an edge between this node and another.
        """
        if node in self.neighbors:
            self.neighbors.remove(node)

        if self in node.neighbors:
            node.neighbors.remove(self)

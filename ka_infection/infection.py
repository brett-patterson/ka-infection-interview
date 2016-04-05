
def connected_component(node):
    """ Get the connected component for a node using a breadth first search.

    Parameters:
    -----------
    node : UserNode
        The node to start the search from.

    """
    component = set()
    queue = [node]

    while len(queue) > 0:
        node = queue.pop(0)

        if node not in component:
            component.add(node)
            queue.extend(list(node.neighbors))

    return component


def total_infection(start_node):
    """ Infect the entire connected component of a node. Uses a breadth first
    search to traverse the graph.

    Parameters:
    -----------
    start_node : UserNode
        The node to start the infection from.

    """
    for node in connected_component(start_node):
        node.metadata['infected'] = True


def limited_infection(start_node, graph, target, delta=0):
    """ Infect an approximate number of nodes, attempting to maintain the
    property that all connected components are infected together. The
    start_node is not guaranteed to be infected. This algorithm performs
    greedily -- the solution may not be globally optimal.

    Parameters:
    -----------
    start_node : UserNode
        The node to start the infection from.

    graph : UserGraph
        The full graph that the start node is in.

    target : int
        The approximate number of nodes to infect.

    delta : int
        A margin of error for the target number of nodes. That is, the range
        [target - delta, target + delta] is considered acceptable.

    """
    n_infected = 0
    start_nodes = graph.users()
    partial_components = set()

    # Put the start node at the top of the stack of possible start nodes
    start_nodes.remove(start_node)
    start_nodes.append(start_node)

    # Try to mark entire components as infected first
    while n_infected < target + delta and len(start_nodes) > 0:
        start = start_nodes.pop()
        comp = connected_component(start)

        # Remove all nodes in the connected component from the stack of
        # possible start nodes
        for node in comp:
            if node in start_nodes:
                start_nodes.remove(node)

        if len(comp) > target + delta:
            # If this component is too big to infect completely, store it as a
            # candidate to be partially infected
            partial_components.add(frozenset(comp))
        else:
            # Otherwise, mark the component as infected
            n_infected += len(comp)
            for node in comp:
                node.metadata['infected'] = True

    # If we need to infect more nodes, we'll have to infect partial components
    while n_infected < target - delta and len(partial_components) > 0:
        comp = set(partial_components.pop())

        # Use a breadth first search to do the partial infection so that
        # infected nodes are neighbors
        queue = [comp.pop()]
        while len(queue) > 0 and n_infected < target:
            node = queue.pop(0)

            if not node.metadata.get('infected', False):
                node.metadata['infected'] = True
                n_infected += 1
                queue.extend(list(node.neighbors))


def total_infection(start_node):
    """ Infect the entire connected component of a node. Uses a breadth first
    search to traverse the graph.

    Parameters:
    -----------
    start_node : Node
        The node to start the infection from. Must have a dictionary as its
        data.

    """
    queue = [start_node]

    while len(queue) > 0:
        node = queue.pop(0)

        if not node.get_label('infected', False):
            node.label('infected', True)

            queue.extend(list(node.neighbors()))

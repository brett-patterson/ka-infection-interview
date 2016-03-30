
def total_infection(start_node):
    """ Infect the entire connected component of a node. Uses a breadth first
    search to traverse the graph.

    Parameters:
    -----------
    start_node : UserNode
        The node to start the infection from.

    """
    queue = [start_node]

    while len(queue) > 0:
        node = queue.pop(0)

        if not node.metadata.get('infected', False):
            node.metadata['infected'] = True

            queue.extend(list(node.neighbors))

from graphviz import Graph


def render_graph(graph, name=None, directory=None, fill_infected='green3'):
    """ Render a user graph to an SVG file. Infected nodes are colored
    appropriately.

    Parameters:
    -----------
    graph : UserGraph
        The graph to render.

    name : str
        A name for the graph.

    directory : str
        The directory to render to.

    fill_infected : str
        The fill color for infected nodes.

    """
    dot = Graph(name=name, format='svg', strict=True)

    for user in graph.users():
        if user.metadata.get('infected', False):
            dot.attr('node', style='filled', fillcolor=fill_infected)

        dot.node(unicode(user.tag))
        dot.attr('node', style='')

    for user in graph.users():
        for neighbor in user.neighbors:
            dot.edge(unicode(user.tag), unicode(neighbor.tag))

    dot.render(directory=directory, cleanup=True)

from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])

    for knex in ancestors:
        graph.add_edge(knex[1], knex[0])

    paths = graph.dft(starting_node)
    if len(paths) is 1:
        return -1
    oldest = 0
    longest = 0

    for path in paths:
        if len(path) > longest:
            oldest = path[-1]
            longest = len(path)
        if len(path) == longest and path[-1] < oldest:
            oldest = path[-1]
    return oldest

















# old_moose = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# earliest_ancestor(old_moose, 6)
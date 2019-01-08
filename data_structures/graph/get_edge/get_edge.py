"""Module to extend Graph class with the ability to get edges/weights."""


def get_edges(graph, cities):
    """Loop through a list to find if the elements are connected on a graph."""
    """Returns the resulting total weight if all edges are connected."""

    result = 0
    path = False

    if len(cities) == 1:
        return 'A trip involves at least two cities!'

    for i in range(len(cities) - 1):
        adjacent_cities = graph.get_neighbors(cities[i])
        if cities[i + 1] in adjacent_cities:
            result += graph.graph[cities[i]][cities[i + 1]]
        else:
            path = False
            return path, '$0'
            # if at any point there's no edge between two cities
            # don't bother with the rest

    path = True
    return path, f'${result}'
    # if the loop completes, there's a valid path
    # so return True along with the total weight

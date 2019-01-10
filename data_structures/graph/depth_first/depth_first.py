"""Module to implement depth-first search with existing Graph implementation."""


def depth_first(graph, start_val, result=None):
    """Recursive depth-first search."""
    if result is None:
        result = []
        # create a list to hold visited keys
    if start_val not in result:
        result.append(start_val)
        print(start_val, ', ', sep='', end='')
    for key in graph.graph[start_val]:
        if key not in result:
            depth_first(graph, key, result)
    return result

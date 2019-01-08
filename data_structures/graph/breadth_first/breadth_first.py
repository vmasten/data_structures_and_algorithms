"""Module to add breadth-first search to Graph implementation."""
from ...stack.queue import Queue
# used for keeping track of visited vertices


def breadth_first_traversal(graph, start_val):
    """Perform a breadth-first traversal given a passed in starting point."""
    result = []
    visited = []
    # one list keeps track of vertices themselves, the other whether a given
    # vertex has already been visited

    queue = Queue()
    queue.enqueue(start_val)
    visited.append(start_val)
    # first, add the passed in starting vertex to the queue
    # and note that it's been visited

    while queue.front:
        working = str(queue.dequeue())
        # Without casting to a string, the get_neighbors function doesn't
        # recognize it as a vertex value

        result.append(working)
        # Add the vertex to the result list

        if graph.get_neighbors(working):
            next = graph.get_neighbors(working)
            for item in next:
                if item not in visited:
                    visited.append(item)
                    queue.enqueue(item)
                    # If the vertex has neighbors, and they haven't already
                    # been visited, capture them too

    for i in range(len(result) - 1):
        print(result[i], ', ', sep='', end='')
    print(result[-1])
    # This is a little hacky, but was the easiest way to make sure there
    # wasn't a trailing , after the end of the results list

    return result

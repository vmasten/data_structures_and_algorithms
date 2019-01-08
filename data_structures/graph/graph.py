"""Module to implement graph data structure."""


class Graph:
    """Implements a graph data structure via a class."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def __repr__(self):
        """Magic method for debugging."""
        output = f'<Graph: - {self.graph}>'
        return output

    def __str__(self):
        """Magic method to return an fstring of the graph's root."""
        output = f'Graph: - {self.graph}'
        return output

    def __len__(self):
        """Return the length of the graph."""
        return len(self.graph)

    def add_vert(self, val):
        """Add a vertex to the graph."""
        if self.has_vert(val):
            return self.graph
            # if the vertex exists, don't do anything

        self.graph[val] = {}
        return self.graph
        # otherwise, add the new vertex and return the modified graph

    def has_vert(self, val):
        """Check whether an input vertex exists in the graph."""
        result = False

        if val in self.graph:
            result = True
            return result

        else:
            return result

        # checks for a key in the graph
        # returns vertex or bool

    def add_edge(self, v1, v2, weight):
        """Add an edge between two vertices."""
        if self.has_vert(v1) and self.has_vert(v2):
            # both vertices exist

            self.graph[v1][v2] = weight
            self.graph[v2][v1] = weight
            # create new edge between the vertices with the input weight

        return self.graph

    def get_neighbors(self, val):
        """Get all neighbors of an input vertex."""
        if self.has_vert(val):
            result = list(self.graph[val].keys())
            # cast the dictionary keys to a list

            return result

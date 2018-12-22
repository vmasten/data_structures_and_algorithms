"""Module to implement graph data structure."""


class Graph:
    """
    """
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        output = f'<Graph: - {self.graph}>'
        return output

    def __str__(self):
        output = f'Graph: - {self.graph}'
        return output

    def __len__(self):
        return len(self.graph)

    def add_vert(self, val):
        """
        """
        if self.has_vert(val):
            return self.graph

        self.graph[val] = {}
        return self.graph

        # add vertice to self.graph
        # check to see if the vert already exists: if so raise exception
        # create a helper method
        # return self

    def has_vert(self, val):
        """
        """
        result = False

        if val in self.graph:
            result = True
            return result

        else:
            return result

        # checks for a key in the graph
        # returns vertex or bool

    def add_edge(self, v1, v2, weight):
        """
        """
        # add a relationship and weight between two verts
        # don't forget to validate
        # returns self
        if self.has_vert(v1) and self.has_vert(v2):

            self.graph[v1][v2] = weight
            self.graph[v2][v1] = weight

        return self.graph



    def get_neighbors(self, val):
        """
        """
        if self.has_vert(val):
            return self.graph[val]
        # Given a val (key), return all adjacent verts
        # returns tuple of vals

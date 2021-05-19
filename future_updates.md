# Planned functions in future updates

These functions are planned to be added to the library:

<pre><code>add_vertex: adds a new vertex to the graph
remove_vertex: removes a given vertex and associated edges from the graph
is_cyclical: checks whether the graph contains a cycle

    def add_vertex(self, name):
        """
        Adds a vertex to graph, if vertex already exists nothing is executed
        :param name: name of added vertex
        """
        pass
        
    def remove_vertex(self, a):
        """
        Removes the given vertex with name a. If the vertex does not exist nothing is executed
        :param a: name of the vertex
        """
        pass
        
    def is_cyclical(self):
        """
        Checks whether the graph contains a cycle of edges, meaning that there are two different paths between two nodes
        :return: boolean True or False depending on if the graph contains a cycle or not
        """
        pass
        
    def contains(self, a):
        """
        Checks the graph contains a vertex with the name a
        :param a: name of the vertex
        """
        pass
        
    def healthy(self):
        """
        Checks whether graph is healthy in the following respects:
        - An even number of vertices have an odd number of edges
        - self._size gives the right number of vertices
        - self._edge gives the right number of edges
        - No edges have negative weight
        :return: True if graph is considered healthy, otherwise False 
        """
        pass
        
    def merge(self, other_graph):
        """
        Merges another graph into the graph.
        If the other graph has any vertices with the same name as a vertex in the initial graph then the resulting
         graph's vertex with that name will have the combined edges of the merged vertices.
        If the other graph has an edge that goes between two vertices with the same names as an edge in the initial graph
         the resulting graphs edge between the two vertices will have the minimum weight of the two preexisting edges.
        :param other_graph: Graph to be merged into initial graph
        """
        pass
</code></pre>
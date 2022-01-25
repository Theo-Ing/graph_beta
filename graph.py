# Theo Ingelstam

"""
Library to create weighted undirected graphs and perform operations on the graph.
This implementation does not permit multiple edges between the same two vertices nor non-positive weight on edges.
"""

from math import inf
import queue


class _Vertex:
    def __init__(self):
        """
        Creates an empty vertex object that keeps track of neighbors using a proximity list.
        """
        self.neighbor = dict()  # all neighbor vertices names and the weight value of the edge connecting them


class Graph:
    def __init__(self, vertices_names=()):
        """
        Creates a graph object, receives input of an iterable object containing the names of initial vertex names.
        :param vertices_names: <iterable> object containing the names of the initial vertices, duplicates not counted twice
        """
        self._V = dict()    # vertices of the graph in a hash-table with names as keys
        self._size = 0      # number of vertices in graph
        self._edge = 0      # number of edges in graph

        # create vertices
        for vertex in vertices_names:
            if vertex not in self._V:
                self._V[vertex] = _Vertex()
                self._size += 1

    def add_edge(self, name1, name2, weight=1):
        """
        Connects vertices name1 and name2 with an edge of given weight, if the vertices already
         are connected the weight is updated to the new weight.
        If name1 or name2 does not exist nothing is executed.
        If weight is less than or equal to zero nothing is executed.
        :param name1: <any object, not NoneType> name of the first vertex to be connected
        :param name2: <any object, not NoneType> name of second vertex to be connected
        :param weight: <int or tuple> the weight of the created edge
        """
        # check existence of name1 and name2
        if not ((name1 in self._V) and (name2 in self._V)):
            return

        if weight > 0:
            if not self.is_neighbor(name1, name2):
                self._edge += 1
            self._V[name1].neighbor[name2] = weight
            self._V[name2].neighbor[name1] = weight

    def remove_edge(self, name1, name2):
        """
        Removes the edge connecting the vertices name1 and name2.
        If the edge does not exist nothing is executed.
        If name1 or name2 does not exist nothing is executed.
        :param name1: <any object, not NoneType> name of the first vertex
        :param name2: <any object, not NoneType> name of the second vertex
        """
        # check existence of name1 and name2
        if not ((name1 in self._V) and (name2 in self._V)):
            return None, None

        if self.is_neighbor(name1, name2):
            del self._V[name1].neighbor[name2]
            del self._V[name2].neighbor[name1]
            self._edge -= 1

    def is_neighbor(self, name1, name2):
        """
        Checks whether the vertices name1 and name2 are neighbours.
        If name1 or name2 does not exist False is returned.
        :param name1: <any object, not NoneType> name of the first vertex
        :param name2: <any object, not NoneType> name of the second vertex
        :return: <boolean> True or False depending on if name1 and name2 are neighbours
        """
        if (name1 in self._V) and (name2 in self._V):
            if name2 in self._V[name1].neighbor:
                return True
        return False

    def is_path(self, name1, name2):
        """
        Checks whether there is a path between the vertices name1 and name2.
        If name1 or name2 does not exist False is returned.
        :param name1: <any object, not NoneType> name of the first vertex
        :param name2: <any object, not NoneType> name of the second vertex
        :return: <boolean> True or False depending on if there is a path between name1 and name2
        """
        if self._size == 0:
            return False
        if (name1 in self._V) and (name2 in self._V):
            visited = set()
            self._bfs(name1, visited, name2)
            if name2 in visited:
                return True
        return False

    def is_connected(self):
        """
        Checks whether the entire graph is connected.
        :return: <boolean> True or False depending on if graph is connected
        """
        if self._size == 0:
            return True
        visited = set()
        start = next(iter(self._V))     # https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/ O(1)
        self._bfs(start, visited)
        if len(visited) == self._size:
            return True
        return False


    def shortest_path(self, start, target):
        """
        Returns the shortest path between vertices with names start and target, if one exists, and the combined weight
         of the path.
        If start and target are not connected None is returned. If start or target does not exist None is returned.
        :param start: <any object, not NoneType> name of the start vertex
        :param target: <any object, not NoneType> name of the target vertex
        :return: <list or None>, <int, float or None> the shortest path between a and b (list) and the combined weight
         of the path
        """
        # check existence of start and target
        if not ((start in self._V) and (target in self._V)):
            return None, None

        # Dijkstra's algorithm (https://yourbasic.org/algorithms/graph/)
        dist = dict()
        prev = dict()
        q = set(self._V.keys())     # queue of undecided vertices
        for vertex in q:
            dist[vertex] = inf
            prev[vertex] = None
        dist[start] = 0

        while len(q) != 0:
            current = self._smallest_dist_name(q, dist)
            q.remove(current)
            if current == target:
                break   # reached desired vertex
            if dist[current] == inf:
                break   # visited all possible vertices
            for name, value in self._V[current].neighbor.items():
                temp = dist[current] + value
                if temp < dist[name]:
                    dist[name] = temp
                    prev[name] = current

        if dist[target] == inf:
            return None, None
        # build path
        path = []
        position = target
        while True:
            path.append(position)
            if position == start:
                break
            position = prev[position]
        path.reverse()
        return path, dist[target]

    def total_vertices(self):
        """
        Returns the number of vertices in the graph.
        :return: <int> number of vertices in graph
        """
        return self._size

    def total_edges(self):
        """
        Returns number of edges in the graph.
        :return: <int> number of edges in graph
        """
        return self._edge

    @staticmethod
    def _smallest_dist_name(q, dist):
        """
        Returns the name in q with the smallest corresponding value in q
        :param q: <set> vertex names
        :param dist: <dictionary> vertex names as keys and distances as values
        :return: <object, not NoneType> the name in q with the smallest value in dist
        """
        min_value = inf
        min_name = None
        for name in q:
            if dist[name] <= min_value:
                min_value = dist[name]
                min_name = name
        return min_name

    def _bfs(self, start, visited, end=None):
        """
        Traverses graph with start in the vertex with the name [start] using a BFS algorithm, adding all visited
        vertices to the set "visited".
        Option to add end vertex name, algorithm will stop if the vertex with the name end is encountered
        :param start: <any object, not NoneType> name of the vertex to start the BFS algorithm
        :param visited: <set> names of the already visited vertices
        :param end: <object> name of target end vertex
        """
        q = queue.Queue()   # creates a FIFO queue
        visited.add(start)
        q.put(start)
        while not q.empty():
            a = q.get()
            for x in self._V[a].neighbor:
                if x not in visited:
                    visited.add(x)
                    q.put(x)
                    if x == end:
                        return  # break early if end is encountered

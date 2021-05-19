# Weighted undirected graph (Beta)

## A library for handling and creating graphs

A weighted undirected graph is a network of vertices where pairs of vertices can be connected with an edge of some value.
Graphs are studied thoroughly in the mathematical field named after them, "Graph theory". For more
information you can visit below links:
- [{wikipedia} Graph theory](https://en.wikipedia.org/wiki/Graph_theory)
- [{yourbasic} Introduction to graph algorithms: definitions and examples](https://yourbasic.org/algorithms/graph/)

This implementation does not permit multiple edges between a given pair of vertices nor non-positive weight on edges.

### Documentation (ver 1.0.0)

#### class Graph

<pre>class Graph
    def __init__(self, vertices_names)</pre>

Creates a graph object, receives input of an iterable object containing the names of initial vertex names.\
**:param vertices_names:** _\<iterable\>_ object containing the names of the initial vertices, duplicates not counted twice

#### method add_edge

<pre>def add_edge(self, name1, name2, weight=1)</pre>

Connects vertices name1 and name2 with an edge of given weight, if the vertices already are connected the weight is
updated to the new weight.\
If name1 or name2 does not exist nothing is executed.\
If weight is less than or equal to zero nothing is executed.\
**:param name1:** _\<any object, not NoneType\>_ name of the first vertex to be connected\
**:param name2:** _\<any object, not NoneType\>_ name of second vertex to be connected\
**:param weight:** _\<int or tuple\>_ the weight of the created edge

#### method remove_edge

<pre>def remove_edge(self, name1, name2)</pre>

Removes the edge connecting the vertices name1 and name2.\
If the edge does not exist nothing is executed.\
If name1 or name2 does not exist nothing is executed.\
**:param name1:** _\<any object, not NoneType\>_ name of the first vertex\
**:param name2:** _\<any object, not NoneType\>_ name of the second vertex

#### method is_neighbor

<pre>def is_neighbor(self, name1, name2)</pre>

Checks whether the vertices name1 and name2 are neighbours.\
If name1 or name2 does not exist False is returned.\
**:param name1:** _\<any object, not NoneType\>_ name of the first vertex\
**:param name2:** _\<any object, not NoneType\>_ name of the second vertex\
**:return:** _\<boolean\>_ True or False depending on if name1 and name2 are neighbours

#### method is_path

<pre>def is_path(self, name1, name2)</pre>

Checks whether there is a path between the vertices name1 and name2.\
If name1 or name2 does not exist False is returned.\
**:param name1:** _\<any object, not NoneType\>_ name of the first vertex\
**:param name2:** _\<any object, not NoneType\>_ name of the second vertex\
**:return:** _\<boolean\>_ True or False depending on if there is a path between name1 and name2

#### method is_connected

<pre>def is_connected(self)</pre>

Checks whether the entire graph is connected.\
**:return:** \<boolean\> True or False depending on if graph is connected

#### method shortest_path

<pre>def shortest_path(self, start, target)</pre>

Returns the shortest path between vertices with names start and target, if one exists, and the combined weight of the path.\
If start and target are not connected None is returned. If start or target does not exist None is returned.\
**:param start:** _\<any object, not NoneType\>_ name of the start vertex\
**:param target:** _\<any object, not NoneType\>_ name of the target vertex\
**:return:** _\<list or None\>, \<int, float or None\>_ the shortest path between start and target (list) and the combined weight
 of the path

#### method total_vertices

<pre>def total_vertices(self)</pre>

Returns the number of vertices in the graph.\
**:return:** _\<int\>_ number of vertices in graph

#### method total_edges

<pre>def total_edges(self)</pre>

Counts number of edges in the graph.\
**:return:** _\<int\>_ number of edges in graph

### Roadmap

- The API of this library may be updated in the future
- Version numbers adhere to [semantic versioning](http://semver.org/).

This library is not considered complete as of yet and can therefore be subject to major changes, all of which to either
add new features or improve time/memory complexity for a preexisting method or the library as a whole.

### Change Log

[change_log.md](change_log.md)

### Planned future additions

[future_updates.md](future_updates.md)

# Theo Ingelstam, grudat21, övn7

from graph import Graph


def test():
    """
    Test code for graph.py
    """
    # empty graph
    graph0 = Graph()
    assert graph0.total_vertices() == 0
    assert graph0.total_edges() == 0
    assert graph0.is_connected()
    assert not graph0.is_path("a", "b")

    # standard case with three vertices
    graph1 = Graph(["a", "b", "c"])
    assert graph1.total_vertices() == 3
    assert not graph1.is_connected()
    assert not graph1.is_path("a", "b")
    # add edge
    graph1.add_edge("a", "b", 4)
    assert graph1.total_edges() == 1
    assert graph1._V["a"].neighbor["b"] == 4
    assert graph1._V["b"].neighbor["a"] == 4
    assert not graph1.is_connected()
    assert graph1.is_path("a", "b")
    # add existing edge
    graph1.add_edge("b", "a", 2)
    assert graph1.total_edges() == 1
    assert graph1._V["a"].neighbor["b"] == 2
    assert graph1._V["b"].neighbor["a"] == 2
    # add new edge with no given weight
    graph1.add_edge("c", "b")
    assert graph1.total_edges() == 2
    assert graph1._V["c"].neighbor["b"] == 1
    assert graph1._V["b"].neighbor["c"] == 1
    assert graph1.is_connected()
    assert graph1.is_path("a", "c")
    # connect non-existing vertex
    graph1.add_edge("c", "d")
    assert graph1.total_vertices() == 3
    assert graph1.total_edges() == 2
    assert graph1.is_connected()
    # remove edge
    graph1.remove_edge("c", "b")
    assert graph1.total_edges() == 1
    assert not "c" in graph1._V["b"].neighbor
    assert not "b" in graph1._V["c"].neighbor
    assert not graph1.is_connected()
    assert not graph1.is_path("a", "c")
    # add edge with negative weight
    graph1.add_edge("c", "b", -1)
    assert graph1.total_edges() == 1
    assert not "c" in graph1._V["b"].neighbor
    assert not "b" in graph1._V["c"].neighbor
    assert not graph1.is_connected()

    # test duplicates
    graph2 = Graph(["a", "b", "a"])
    assert graph2.total_vertices() == 2

    # test res/ex1.png
    ex1 = Graph(["A", "B", "C", "D"])
    ex1.add_edge("A", "B", 5)
    ex1.add_edge("A", "C", 3)
    ex1.add_edge("B", "C", 6)
    ex1.add_edge("B", "D", 3)
    ex1.add_edge("C", "D", 9)
    assert ex1.total_vertices() == 4
    assert ex1.total_edges() == 5
    assert ex1.is_connected()
    path, length = ex1.shortest_path("A", "D")
    assert path == ["A", "B", "D"]
    assert length == 8

    # test res/ex2.png
    ex2 = Graph(["A", "B", "C", "D", "E", "F"])
    ex2.add_edge("A", "C", 13)
    ex2.add_edge("A", "D", 2)
    ex2.add_edge("A", "F", 10)
    ex2.add_edge("B", "C", 8)
    ex2.add_edge("B", "D", 15)
    ex2.add_edge("B", "E", 12)
    ex2.add_edge("C", "E", 7)
    ex2.add_edge("C", "F", 4)
    ex2.add_edge("D", "F", 3)
    assert ex2.total_vertices() == 6
    assert ex2.total_edges() == 9
    assert ex2.is_connected()
    path, length = ex2.shortest_path("A", "E")
    assert path == ["A", "D", "F", "C", "E"]
    assert length == 16

    # test res/ex3.png
    ex3 = Graph([i for i in range(9)])
    ex3.add_edge(0, 1, 3)
    ex3.add_edge(0, 3, 2)
    ex3.add_edge(0, 8, 4)
    ex3.add_edge(1, 7, 4)
    ex3.add_edge(2, 3, 6)
    ex3.add_edge(2, 5, 1)
    ex3.add_edge(2, 7, 2)
    ex3.add_edge(3, 4, 1)
    ex3.add_edge(4, 8, 8)
    ex3.add_edge(5, 6, 8)
    ex3.add_edge(6, 7, 10)
    assert ex3.total_vertices() == 9
    assert ex3.total_edges() == 11
    assert ex3.is_connected()
    path, length = ex3.shortest_path(8, 6)
    assert path == [8, 0, 1, 7, 6] or path == [8, 0, 3, 2, 5, 6]
    assert length == 21

    # test res/ex4.png
    ex4 = Graph(["A", "B", "C", 1, 2, 3])
    ex4.add_edge("A", "B", 5)
    ex4.add_edge("A", "C", 3)
    ex4.add_edge("B", "C", 6)
    ex4.add_edge(1, 2, 1)
    ex4.add_edge(1, 3, 3)
    ex4.add_edge(2, 3, 6)
    assert ex4.total_vertices() == 6
    assert ex4.total_edges() == 6
    assert not ex4.is_connected()
    assert not ex4.is_path(3, "A")
    path, length = ex4.shortest_path(3, "A")
    assert path is None
    assert length is None
    path1, length1 = ex4.shortest_path(3, 2)
    assert path1 == [3, 1, 2]
    assert length1 == 4


if __name__ == '__main__':
    test()

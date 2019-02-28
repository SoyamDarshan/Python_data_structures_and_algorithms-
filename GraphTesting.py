# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:07:51 2019

@author: ThinkPad
"""


class Graph:

    def __init__(self):
        self.outgoing = {}
        self.vertices = {}

    def insert_edge(self, u, v):

        if u in self.outgoing.keys():
            self.outgoing[u].append(v)
        else:
            self.outgoing[u] = [v]

#        if v in self.outgoing.keys():
#            self.outgoing[v].append(u)
#        else:
#            self.outgoing[v] = [u]
#            print(type(self.outgoing[u]))
            
    def degree(self, v):
        adj = self.outgoing
        return len(adj[v])

    def print_edges(self):
        for edge in self.outgoing.keys():
            print(edge, end=' -> ')
            print(" -> ".join(str(i) for i in self.outgoing[edge]))

    def BFS(self, startvertex):
        print("BFS : ", end="")
        visited = {}
        queue = []
        visited[startvertex] = True
        queue.append(startvertex)
        while queue:
            startvertex = queue.pop(0)
            print(startvertex, end=' ')
            if startvertex in self.outgoing.keys():
                for edge in self.outgoing[startvertex]:
                    if edge in visited and visited[edge]:
                        pass
                    else:
                        queue.append(edge)
                        visited[edge] = True
            else:
                visited[startvertex] = True
        print()

    def DFS(self):
        print("DFS : ", end="")
        visited = {}
        for i in self.outgoing.keys():
            self.DFSrec(i, visited)
        self.vertices = visited
        print()

    def DFSrec(self, startindex, visited):
        if startindex in visited and visited[startindex]:
            pass
        else:
            visited[startindex] = True
            print(startindex, end=' ')
            if startindex in self.outgoing.keys():
                for i in self.outgoing[startindex]:
                    if i not in visited:
                        self.DFSrec(i, visited)

    def toopological_sort(self, start, visited=[], sort=[]):
        current = start
        visited.append(current)
        if current in self.outgoing:
            neighbors = self.outgoing[current]
            for neighbor in neighbors:
                if neighbor not in visited:
                    print(visited)
                    sort = self.toopological_sort(neighbor, visited, sort)
        sort.append(current)
        if len(visited) != len(self.vertices):
            for vertice in self.vertices:
                if vertice not in visited:
                    print(visited)
                    sort = self.toopological_sort(vertice, visited, sort)
        return sort


if __name__ == '__main__':
    name = Graph()
    name.insert_edge(3, 4)
    name.insert_edge(1, 4)
    name.insert_edge(2, 4)
    name.insert_edge(5, 4)
    name.insert_edge(3, 7)
    name.insert_edge(3, 8)
    name.insert_edge(3, 1)
    name.insert_edge(2, 6)
    name.insert_edge(7, 9)
    name.insert_edge(3, 5)
    name.insert_edge(8, 6)
    name.insert_edge(1, 9)
    name.insert_edge(9, 8)
    name.insert_edge(19, 20)
    name.print_edges()
    print(name.outgoing)
    name.BFS(3)
    name.DFS()
    print("Vertices = ", name.vertices.keys())
    print("Degree = ", name.degree(3))
    print("Size = ", len(name.vertices))
    print(name.toopological_sort(3))

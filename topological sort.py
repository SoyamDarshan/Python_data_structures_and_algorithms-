# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:41:10 2019

@author: ThinkPad
"""
#
#
#def toopological_sort(self, start, visited=[], sort=[]):
#    current = start
#    visited.append(current)
#    neighbors = self.outgoing[current]
#    for neighbor in neighbors:
#        if neighbor not in visited:
#            sort = toopological_sort(neighbor, visited, sort)
#    sort.append(current)
#
#    if len(visited) != len(self.vertices):
#        for vertice in self.vertices:
#            if vertice not in visited:
#                toopological_sort(vertice, visited, sort)
#
#    return sort

edges = {3: [4, 7, 8, 1, 5], 1: [4, 9], 2: [4, 6], 5: [4], 7: [9], 8: [6], 9: [8], 19: [20]}
vertices = [3, 4, 7, 9, 8, 6, 1, 5, 2, 19, 20]


def topological_sort(start, visited, sort):
    """Perform topolical sort on a directed acyclic graph."""
    current = start
    # add current to visited
    visited.append(current)
    if current in edges:
        neighbors = edges[current]
        for neighbor in neighbors:
            # if neighbor not in visited, visit
            if neighbor not in visited:
                sort = topological_sort(neighbor, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    # return sort
    return sort


sort = topological_sort(3, [], [])
print(sort)
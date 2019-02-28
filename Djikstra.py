# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:24:36 2019

@author: ThinkPad
"""

import sys


class PriorityQueue:
    # Based on Min Heap
    def __init__(self):
        self.cur_size = 0
        self.array = []
        self.pos = {}   # To store the pos of node in array

    def isEmpty(self):
        return self.cur_size == 0

    def min_heapify(self, idx):
        lc = self.left(idx)
        rc = self.right(idx)
        if lc < self.cur_size and self.array(lc)[0] < self.array(idx)[0]:
            smallest = lc
        else:
            smallest = idx
        if rc < self.cur_size and self.array(rc)[0] < self.array(smallest)[0]:
            smallest = rc
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        # Inserts a node into the Priority Queue
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    def extract_min(self):
        # Removes and returns the min element at top of priority queue
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size - 1]
        self.cur_size -= 1
        self.min_heapify(1)
        del self.pos[min_node]
        return min_node

    def left(self, i):
        # returns the index of left child
        return 2 * i + 1

    def right(self, i):
        # returns the index of right child
        return 2 * i + 2

    def par(self, i):
        # returns the index of parent
        return i // 2

    def swap(self, i, j):
        # swaps array elements at indices i and j
        # update the pos{}
        self.pos[self.array[i][1]] = j
        self.pos[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def decrease_key(self, tup, new_d):
        idx = self.pos[tup[1]]
        # assuming the new_d is atmost old_d
        self.array[idx] = (new_d, tup[1])
        while idx > 0 and self.array[self.par(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par(idx))
            idx = self.par(idx)


class Graph:
    def __init__(self, num):
        self.adjList = {}   # To store graph: u -> (v,w)
#        self.num_nodes = num    # Number of nodes in graph
#        # To store the distance from source vertex
#        self.dist = [0] * self.num_nodes
#        self.par = [-1] * self.num_nodes  # To store the path

    def insert_edge(self, u, v, w):
        #  Edge going from node u to v and v to u with weight w
        # u (w)-> v, v (w) -> u
        # Check if u already in graph
        if u in self.adjList.keys():
            self.adjList[u][v] = w
        else:
            self.adjList[u] = {v: w}

        # Assuming undirected graph
#        if v in self.adjList.keys():
#            self.adjList[v].append((u, w))
#        else:
#            self.adjList[v] = [(u, w)]

    def show_graph(self):
        # u -> v(w)
        for u in self.adjList:
            print(u, '->', ' -> '.join(str("{}({})".format(v, w))
                                       for v, w in self.adjList[u]))

    def dijkstra(self, src):
        # Flush old junk values in par[]
        self.par = [-1] * self.num_nodes
        # src is the source node
        self.dist[src] = 0
        Q = PriorityQueue()
        Q.insert((0, src))  # (dist from src, node)
        for u in self.adjList.keys():
            if u != src:
                self.dist[u] = sys.maxsize  # Infinity
                self.par[u] = -1

        while not Q.isEmpty():
            u = Q.extract_min()  # Returns node with the min dist from source
            # Update the distance of all the neighbours of u and
            # if their prev dist was INFINITY then push them in Q
            for v, w in self.adjList[u]:
                new_dist = self.dist[u] + w
                if self.dist[v] > new_dist:
                    if self.dist[v] == sys.maxsize:
                        Q.insert((new_dist, v))
                    else:
                        Q.decrease_key((self.dist[v], v), new_dist)
                    self.dist[v] = new_dist
                    self.par[v] = u

        # Show the shortest distances from src
        self.show_distances(src)

    def show_distances(self, src):
        print("Distance from node: {}".format(src))
        for u in range(self.num_nodes):
            print('Node {} has distance: {}'.format(u, self.dist[u]))

    def show_path(self, src, dest):
        # To show the shortest path from src to dest
        # WARNING: Use it *after* calling dijkstra
        path = []
        cost = 0
        temp = dest
        # Backtracking from dest to src
        while self.par[temp] != -1:
            path.append(temp)
            if temp != src:
                for v, w in self.adjList[temp]:
                    if v == self.par[temp]:
                        cost += w
                        break
            temp = self.par[temp]
        path.append(src)
        path.reverse()

        print('----Path to reach {} from {}----'.format(dest, src))
        for u in path:
            print('{}'.format(u), end=' ')
            if u != dest:
                print('-> ', end='')

        print('\nTotal cost of path: ', cost)


if __name__ == '__main__':
    name = Graph(11)
    name.insert_edge(3, 4, 32)
    name.insert_edge(1, 4, 45)
    name.insert_edge(2, 4, 56)
    name.insert_edge(5, 4, 78)
    name.insert_edge(3, 7, 12)
    name.insert_edge(3, 8, 22)
    name.insert_edge(3, 1, 62)
    name.insert_edge(2, 6, 31)
    name.insert_edge(7, 9, 42)
    name.insert_edge(3, 5, 18)
    name.insert_edge(8, 6, 33)
    name.insert_edge(1, 9, 55)
    name.insert_edge(9, 8, 25)
    name.insert_edge(19, 20, 20)
    print(name.adjList)
    name.dijkstra(3)
#    print("Vertices = ", name.vertices.keys())
#    print("Degree = ", name.degree(3))
#    print("Size = ", len(name.vertices))
#    print(name.toopological_sort(3))

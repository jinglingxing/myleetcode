#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:30:13 2020

@author: jinlingxing
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #case: when graph is empty
        if node is None:
            return None
        #initialize queue with reference node
        queue = [node]
        #create root node(reference node)
        root = Node(node.val, [])
        #initialize hashmap
        hashMap = {}
        #put root in hashmap
        hashMap[node] = root
        #bfs as long as queue is not empty
        while(len(queue) != 0):
            #take current node form queue
            curr = queue.pop(0)
            #iterare neighbours
            for i in curr.neighbors:
            #check if neighbours in hashmap, if neighbor is not in hashmap
                if i not in hashMap:
                #create nodes(neighbours)
                    newNode = Node(i.val, [])
                #add node to hashmap, key is value, and value is the node(neighbour)
                    hashMap[i] = newNode
                #append original neighbour node to queue
                    queue.append(i)
            #add the nieghbour node to current node.neighbors
                hashMap[curr].neighbors.append(hashMap[i])
        return root
    
if __name__ == "__main__":
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)
    e1.neighbors = [2,4]
    e2.neighbors = [1,3]
    e3.neighbors = [2,4]
    e4.neighbors = [1,3]
    node = [e1,e2,e3,e4]
    sol = Solution()
    sol.cloneGraph(node)
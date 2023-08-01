"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
"""


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # graph: {0: [1, 2], 1: [0, 2], 2: [1, 0]}

        def dfs(sr: int, st: int) -> bool:
            if sr in visited:
                return False

            if sr == st:
                return True

            visited.add(sr)

            # sr=0, st=2, nei: [1,2], visited: (0)
            # sr=1, st=2, nei: [0,2], visited: (0,1)
            # sr=0, return
            # sr=2, st=2, nei: [1,0], visited: (0,1,2), return True
            neighbors = graph[sr]
            for nei in neighbors:
                if dfs(nei, st):
                    return True
            return False

        return dfs(source, destination)

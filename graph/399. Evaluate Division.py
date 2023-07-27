"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
        # queries = [["a","c"]]
        # Output: [6.00000]

        # graph: {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.333}}
        graph = defaultdict(dict)

        for i in range(len(equations)):
            x, y = equations[i][0], equations[i][1]
            graph[x][y] = values[i]
            graph[y][x] = 1 / values[i]

        def dfs(start: str, end: str, visited: set) -> float:
            # visited set is used to avoid visiting nodes that have already been visited(infinity loop)
            if start in visited or start not in graph:
                return -1
            if start == end:
                return 1
            visited.add(start)

            # traverse the neighbors of start and find the path value recursively
            # first iter: start=a, end=c, nei=b, visited:(a), val=2, return 2*3
            # second ite: start=b, end=c, nei=a,c, visited: (a,b), val=3, return 1*3
            # third iter: start=a, end=c, a in visited, return -1
            # third iter: start=c, end=c, return 1
            for nei, val in graph[start].items():
                path_val = dfs(nei, end, visited)
                if path_val != -1:
                    return val * path_val
            return -1

        res = []
        for query in queries:
            # start=a, end=c
            start, end = query
            res.append(dfs(start, end, set()))
        return res

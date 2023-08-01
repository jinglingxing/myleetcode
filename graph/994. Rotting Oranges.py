"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = grid
        # count the rotten oranges
        q = collections.deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 2:
                    q.append((i, j))
                if visited[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        if len(q) == 0:
            return -1

        min_ = -1
        # down, up, left, right
        d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            size = len(q)
            while size > 0:
                x, y = q.popleft()
                size -= 1
                for dx, dy in d:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        visited[i][j] = 2
                        fresh -= 1
                        q.append((i, j))
            min_ += 1

        if fresh == 0:
            return min_
        return -1
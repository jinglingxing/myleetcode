"""
You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

Example:
Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
"""


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # forest = [[1,2,3],[0,0,0],[7,6,5]]
        m, n = len(forest), len(forest[0])

        pq = []
        for row in range(m):
            for col in range(n):
                height = forest[row][col]
                if height > 1:
                    heapq.heappush(pq, (height, row, col))

        # pq = [(2, 0, 1), (3, 0, 2), (7, 2, 0), (6, 2, 1), (5, 2, 2)]

        def shortest_distance(sx, sy, ex, ey) -> int:
            """
            sx, sy: start point x, y
            ex, ey: end point x, y
            """
            steps = 0
            # (1, 0) -> right, (-1, 0) -> left
            # (0, 1) -> down,  (0, -1) -> up
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            que = deque([(sx, sy)])
            visited = {(sx, sy)}

            while len(que):
                for _ in range(len(que)):
                    i, j = que.popleft()

                    if (i, j) == (ex, ey):
                        # i=0, j=1, ex=0, ey=1
                        return steps

                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        # i=0, j=0, x=0, y=1, ex=0, ey=1, forest[0][1]=2, visited: {(0, 1), (0, 0)}, que=[(0, 1)]
                        if 0 <= x < m and 0 <= y < n and forest[x][y] != 0 and (x, y) not in visited:
                            que.append((x, y))
                            visited.add((x, y))
                            print('visited:', visited)
                        print(que, 'i=', i, ',', 'j=', j, ',',
                              'x=', x, ',', 'y=', y, ',',
                              'ex=', ex, ',', 'ey=', ey)
                steps += 1
            return -1

        start_x, start_y = 0, 0
        total_steps = 0

        while len(pq):
            height, end_x, end_y = heapq.heappop(pq)
            # height=2, end_x=0, end_y=1, steps=1
            steps = shortest_distance(start_x, start_y, end_x, end_y)

            if steps == -1:
                return -1

            total_steps += steps
            start_x, start_y = end_x, end_y

        return total_steps
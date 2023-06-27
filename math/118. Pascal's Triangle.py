class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # math
        res = [[1]]
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(res[i - 1][j - 1] + res[i - 1][j])

            temp.append(1)
            res.append(temp)
        return res

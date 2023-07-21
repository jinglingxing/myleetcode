class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        index_one_img1 = []
        index_one_img2 = []

        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j]:
                    index_one_img1.append((i, j))

                if img2[i][j]:
                    index_one_img2.append((i, j))

        r = {}
        for i1, j1 in index_one_img1:
            for i2, j2 in index_one_img2:
                shift = (i1 - i2, j1 - j2)
                if shift not in r:
                    r[shift] = 0
                r[shift] += 1

        return max(r.values()) if r else 0

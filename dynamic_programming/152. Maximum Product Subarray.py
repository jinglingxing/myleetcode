class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = [nums[0]]*n
        min_product = [nums[0]]*n


        for i in range(1, n):
            max_product[i] = max(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])
            min_product[i] = min(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])

        return max(max_product)
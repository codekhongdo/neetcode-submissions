class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(i: int, current_xor: int) -> int:
            if i == len(nums):
                return current_xor
            take = dfs(i + 1, current_xor ^ nums[i])
            skip = dfs(i + 1, current_xor)
            return take + skip
        return dfs(0, 0)
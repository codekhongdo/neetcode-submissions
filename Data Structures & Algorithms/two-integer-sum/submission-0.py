class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            b=target-nums[i]
            if b in a:
                return [a[b], i]
            a[nums[i]] = i
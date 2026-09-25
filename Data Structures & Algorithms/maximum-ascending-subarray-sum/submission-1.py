class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum=nums[0]
        max_sum=float("-inf")
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sum+=nums[i]
            else:
                if sum>max_sum:
                    max_sum=sum
                sum=nums[i]
        return max(max_sum,sum)

        
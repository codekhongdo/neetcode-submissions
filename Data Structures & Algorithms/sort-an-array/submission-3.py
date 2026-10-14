class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        pivot=len(nums)//2
        left=[x for x in nums if x<nums[pivot]]
        mid=[x for x in nums if x==nums[pivot]]
        right=[x for x in nums if x>nums[pivot]]
        return self.sortArray(left)+mid+self.sortArray(right)
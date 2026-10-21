class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        note=1
        for run in range(1,len(nums)):
            if nums[run]==nums[run-1]:
                continue
            else:
                nums[note]=nums[run]
                note+=1
        return note
        
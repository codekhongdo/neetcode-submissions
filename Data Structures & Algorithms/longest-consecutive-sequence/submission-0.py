class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        A=0
        c=1
        my_set=set(nums)
        for i in nums:
            B=0
            c=0
            while (i-1 not in my_set) and (i+c in my_set):
               c+=1 
               B+=1
               if B>A:
                A=B 
        return A 
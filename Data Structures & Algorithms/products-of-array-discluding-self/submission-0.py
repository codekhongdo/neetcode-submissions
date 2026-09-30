class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[1]*n
        trai=1
        for i in range(n):
            output[i]=trai
            trai*=nums[i]
        phai=1
        for i in range(n-1,-1,-1):
            output[i]*=phai
            phai*=nums[i]
        return output
        
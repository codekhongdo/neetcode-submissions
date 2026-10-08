class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        A=[]
        i=1
        while i<=2:
            for k in range(len(nums)):
                A.append(nums[k])
            i+=1
        return A
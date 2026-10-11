class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        A={}
        for i in nums:
            A[i] = A.get(i, 0) + 1
        return max(A,key=A.get)

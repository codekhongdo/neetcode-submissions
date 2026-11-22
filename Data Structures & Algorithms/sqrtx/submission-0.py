class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        left=0
        right=x
        while left<=right:
            mid=(right+left)//2
            if mid*mid==x:
                ans=mid
                return ans
            elif mid*mid<x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans



        
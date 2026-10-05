class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        left=0
        right=len(heights)-1
        while left<right:
            H=min(heights[left],heights[right])
            W=right-left
            S=W*H
            if S>m:
                m=S
            if heights[left]>heights[right]:
                right-=1
            elif heights[left]>heights[right]:
                left+=1
            else:
                left+=1
        return m

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {0: 0, 1: 0}
        
        def add_re(i):
            if i in memo:
                return memo[i]
            memo[i]=min(add_re(i-1)+cost[i-1],add_re(i-2)+cost[i-2])
            return memo[i]
            
        return add_re(n)

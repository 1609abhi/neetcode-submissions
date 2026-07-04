class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        final=len(cost)
        dp = [-1 for _ in range(final+1)]

        def count(index):

            if index==0:
                return 0
            
            if index==1:
                return 0

            if dp[index]!=-1:
                return dp[index]

            one_step=cost[index-1]+count(index-1)
            two_step=cost[index-2]+count(index-2)
            
            dp[index]=min(one_step,two_step)
            return dp[index]

        return count(final)
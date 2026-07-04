class Solution:
    def climbStairs(self, n: int) -> int:

        dp=[-1 for _ in range(n+1)]

        def count(n):
            if n==1:
                return 1
            if n==2:
                return 2

            if dp[n] != -1:
                return dp[n]

            dp[n]=count(n-1)+count(n-2)
            return dp[n]

        return count(n)        

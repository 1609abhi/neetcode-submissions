class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n=len(coins)
        dp=[[0 for _ in range(amount+1)] for _ in range(n)]
        
        for index in range(n):
            dp[index][0]=0

        for target in range(amount+1):
            if target % coins[0]==0:
                dp[0][target]=target//coins[0]
            else:
                dp[0][target]=float("inf")

        
        for index in range(1,n):
            for target in range(1,amount+1):
                
                #pick
                pick=float("inf")
                if coins[index]<=target:
                    pick=1+dp[index][target-coins[index]]

                #not pick
                not_pick=0+dp[index-1][target]

                dp[index][target]=min(pick,not_pick)
        
        ans=dp[n-1][amount]

        if ans==float("inf"):
            return -1
        
        else:
            return ans
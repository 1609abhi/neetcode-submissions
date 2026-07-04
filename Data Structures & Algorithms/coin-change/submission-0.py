class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        
        def count(index,target):

            if target==0:
                return 0
            
            if index==0:
                if target % coins[index]==0:
                    return target//coins[index]
                else:
                    return float("inf")

            if dp[index][target]!=-1:
                return dp[index][target]

            #pick
            pick=float("inf")
            if coins[index]<=target:
                pick=1+count(index,target-coins[index])

            #not pick
            not_pick=0+count(index-1,target)

            dp[index][target]=min(pick,not_pick)

            return dp[index][target]
        
        ans=count(n-1,amount)

        if ans==float("inf"):
            return -1
        
        else:
            return ans
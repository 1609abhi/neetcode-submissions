class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp=[[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        def total(index,amt):

            if amt==0:
                return 1

            if index==len(coins)-1:
                if amt%coins[index]==0:
                    return 1
                else:
                    return 0
            
            if dp[index][amt] != -1:
                return dp[index][amt]

            pick=0
            #pick
            if coins[index]<=amt:
                pick=total(index,amt-coins[index])
            
            #not pick
            not_pick=total(index+1,amt)

            dp[index][amt]=pick+not_pick

            return dp[index][amt]

        return total(0,amount)
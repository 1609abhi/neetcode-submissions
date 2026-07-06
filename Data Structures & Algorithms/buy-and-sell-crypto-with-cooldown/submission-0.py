class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        ## buy is 0/1 binary... 1 you can buy... 0 you cant buy.... index represent day

        dp=[[-1 for _ in range(2)] for _ in range(len(prices))]

        def total(index,buy):

            if index>=len(prices):
                return 0

            if dp[index][buy]!=-1:
                return dp[index][buy]
            if buy:
                ## buy on current day
                buy_current=-prices[index]+total(index+1,1-buy)

                ## dont buy 
                buy_not_current=total(index+1,buy)

                dp[index][buy]=max(buy_current,buy_not_current)
                return max(buy_current,buy_not_current)
            else:

                ## sell on current day
                sell_current=prices[index]+total(index+2,1-buy)

                ## dont sell on current day
                sell_not_current=total(index+1,buy)

                dp[index][buy]=max(sell_current,sell_not_current)
                return max(sell_current,sell_not_current)

        return total(0,1)
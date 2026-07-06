class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp=[[-1 for _ in range(n)] for _ in range(m)]

        def count(row,col):

            if row==0 and col==0:
                return 1
            
            if row<0 or col<0:
                return 0

            if dp[row][col]!=-1:
                return dp[row][col]


            total=0

            #up
            total+=count(row-1,col)

            #left
            total+=count(row,col-1)

            dp[row][col]=total
            
            return total

        return count(m-1,n-1)
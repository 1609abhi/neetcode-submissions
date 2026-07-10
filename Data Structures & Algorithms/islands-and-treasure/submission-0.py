from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        visited_array=[[False for _ in range(n)] for _ in range(m)]
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j,0))
                    visited_array[i][j]=True

        while(q):   

            for _ in range(len(q)): 
                r,c,step=q.popleft()
                for delr,delc in [(-1,0),(0,1),(+1,0),(0,-1)]:
                    newr=r+delr
                    newc=c+delc
                    if newr>=0 and newc>=0 and newr<m and newc<n and visited_array[newr][newc]==False and grid[newr][newc]==2147483647:
                        visited_array[newr][newc]=True
                        grid[newr][newc]=1+step
                        q.append((newr,newc,step+1))



from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        visited_array=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    visited_array[i][j]=True
        
        time=0
        while(q):
            for _ in range(len(q)):
                r,c,step=q.popleft()
                time=max(time,step)

                for delr,delc in [(-1,0),(0,1),(+1,0),(0,-1)]:
                    newr=r+delr
                    newc=c+delc

                    if newr>=0 and newr<len(grid) and newc>=0 and newc<len(grid[0]) and visited_array[newr][newc]==False and grid[newr][newc]==1:
                        q.append((newr,newc,1+step))
                        visited_array[newr][newc]=True


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited_array[i][j]==False:
                    return -1

        return time


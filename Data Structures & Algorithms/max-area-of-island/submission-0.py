from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        visited_array=[[False for _ in range(n)] for _ in range(m)]

        def bfs(row,col):
            q=deque()
            q.append((row,col))
            visited_array[row][col]=True
            area=1

            while(q):
                r,c=q.popleft()

                for delr,delc in [(-1,0),(0,1),(1,0),(0,-1)]:
                    newr=r+delr
                    newc=c+delc
                    if newr>=0 and newc>=0 and newr<m and newc<n and visited_array[newr][newc]==False and grid[newr][newc]==1:
                        q.append((newr,newc))
                        visited_array[newr][newc]=True
                        area+=1
            
            return area
        
        max_area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited_array[i][j]==False:
                    max_area=max(max_area,bfs(i,j))
        
        return max_area


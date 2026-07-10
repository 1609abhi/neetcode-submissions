class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited_array=[[False for _ in range(n)] for _ in range(m)]

        def dfs(row,col):
            visited_array[row][col]=True

            #up,right,down,left
            delr=[-1,0,+1,0]
            delc=[0,+1,0,-1]

            for r,c in zip(delr,delc):
                newr=row+r
                newc=col+c
                if newr>=0 and newc>=0 and newr<m and newc<n and grid[newr][newc]=="1" and visited_array[newr][newc]==False:
                    dfs(newr,newc)
        
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    if visited_array[i][j]==False:
                        count+=1
                        dfs(i,j)
                        

        return count

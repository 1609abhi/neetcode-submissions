from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ## index

        ans=[]
        for i in range(len(nums)):

            while(len(q)>0 and nums[i]>=nums[q[-1]]):
                q.pop()
            
            q.append(i)
            
            if q[0]==i-k:
                q.popleft()

            if i-k+1>=0:
                ans.append(nums[q[0]])
        
        return ans
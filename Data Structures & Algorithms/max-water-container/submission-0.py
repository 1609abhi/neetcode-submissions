class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        max_water=float("-inf")
        while(i<j):
            water=min(heights[i],heights[j])*(j-i)
            max_water=max(max_water,water)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
                
        return max_water
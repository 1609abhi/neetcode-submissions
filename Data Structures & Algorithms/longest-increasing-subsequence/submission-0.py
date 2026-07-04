class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp={}

        def longest(prev,index):
            
            if index<0:
                return 0

            if (index,prev) in dp:
                return dp[(index,prev)]

            #pick
            pick=float("-inf")
            if nums[index]<prev:
                pick=1+longest(nums[index],index-1)

            #not pick
            not_pick=0+longest(prev,index-1)

            if (index,prev) not in dp:
                dp[(index,prev)]=max(pick,not_pick)

            return dp[(index,prev)]
        
        return longest(float("inf"),len(nums)-1)

class Solution:
    def rob(self, nums: List[int]) -> int:

        dp=[-1 for _ in range(len(nums))]

        def count(index):

            if index==len(nums):
                return 0
            
            if index==len(nums)-1:
                return nums[len(nums)-1]

            if dp[index]!=-1:
                return dp[index]

            #rob current one
            rob=nums[index]+count(index+2)

            #not rob current one
            not_rob=0+count(index+1)

            dp[index]=max(rob,not_rob)
            return dp[index]

        return count(0)
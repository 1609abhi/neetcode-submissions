class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        nums_s=nums[:len(nums)-1]
        nums_e=nums[1:]

        dp_s=[-1 for _ in range(len(nums_s))]
        dp_e=[-1 for _ in range(len(nums_e))]

        def count(index,nums,dp):

            if index==len(nums):
                return 0
            
            if index==len(nums)-1:
                return nums[len(nums)-1]

            if dp[index]!=-1:
                return dp[index]

            #rob current one
            rob=nums[index]+count(index+2,nums,dp)

            #not rob current one
            not_rob=0+count(index+1,nums,dp)

            dp[index]=max(rob,not_rob)
            return dp[index]

        return max(count(0,nums_s,dp_s),count(0,nums_e,dp_e))
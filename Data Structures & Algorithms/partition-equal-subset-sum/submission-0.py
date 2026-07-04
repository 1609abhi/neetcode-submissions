class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        tot=sum(nums)
        
        if tot%2!=0:
            return False

        dp=[[-1 for _ in range(tot//2+1)] for _ in range(len(nums))]

        def total(index,target):

            if target==0:
                return True
            
            if index<0:
                return False

            if dp[index][target]!=-1:
                return dp[index][target]

            #not pick
            not_pick=total(index-1,target)

            #pick
            pick=False
            if nums[index]<=target:
                pick=total(index-1,target-nums[index])

            dp[index][target]=pick or not_pick
            return dp[index][target]

        return total(len(nums)-1,tot//2)
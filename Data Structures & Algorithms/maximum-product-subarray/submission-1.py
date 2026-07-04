class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        global_max=nums[0]
        current_max=nums[0]
        current_min=nums[0]

        for i in range(1,len(nums)):

            val1=current_max*nums[i]
            val2=current_min*nums[i]
            val3=nums[i]

            current_max=max(val1,max(val2,val3))
            current_min=min(val1,min(val2,val3))
            
            global_max=max(global_max,current_max)
        
        return global_max



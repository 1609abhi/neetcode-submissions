class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        product=[0 for _ in range(n)]

        for i in range(n):
            prod=1
            for j in range(n):
                if j!=i:
                    prod=prod*nums[j]
            
            product[i]=prod
        
        return product


        
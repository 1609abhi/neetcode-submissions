# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         product=[0 for _ in range(n)]

#         for i in range(n):
#             prod=1
#             for j in range(n):
#                 if j!=i:
#                     prod=prod*nums[j]
            
#             product[i]=prod
        
#         return product

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        product=[1 for _ in range(n)]
        prefix=[1 for _ in range(n)]
        suffix=[1 for _ in range(n)]
        
        prod=1
        for i in range(1,n):
            prod=prod*nums[i-1]
            prefix[i]=prod
            
        prod=1
        for i in range(n-2,-1,-1):
            prod=prod*nums[i+1]
            suffix[i]=prod
        

        for i in range(n):
            product[i]=prefix[i]*suffix[i]
        
        return product


        

        
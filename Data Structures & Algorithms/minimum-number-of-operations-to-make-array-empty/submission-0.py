import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash_map={}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]]=1
            else:
                hash_map[nums[i]]+=1
        
        count=0
        for val in hash_map.values():
            if val<2:
                return -1
            else:
                count+=math.ceil(val/3)

        return count
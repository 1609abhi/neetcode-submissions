class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_map={}

        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]]=1
            else:
                return True
        
        return False
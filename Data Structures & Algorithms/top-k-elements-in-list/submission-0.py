class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for val in nums:
            if val not in hash_map:
                hash_map[val]=1
            else:
                hash_map[val]+=1
        
        hash_map=list(hash_map.items())
        
        hash_map.sort(key=lambda x:-x[1])
        
        ans=[]
        
        for i in range(k):
            ans.append(hash_map[i][0])
        
        return ans


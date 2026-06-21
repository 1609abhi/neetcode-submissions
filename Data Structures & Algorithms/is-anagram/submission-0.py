class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map={}
        for char in s:
            if char not in hash_map:
                hash_map[char]=1
            else:
                hash_map[char]+=1
        
        for char in t:
            if char in hash_map:
                hash_map[char]-=1
                if hash_map[char]==0:
                    del hash_map[char]
            else:
                return False
        
        if len(hash_map)!=0:
            return False
        
        return True
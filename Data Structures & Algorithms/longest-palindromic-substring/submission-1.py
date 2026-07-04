class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        max_len=0
        index1=-1
        index2=-1

        for i in range(len(s)):
            l=i
            r=i
            while(l>=0 and r<=len(s)-1 and s[l]==s[r]):
                length=r-l+1
                if length>max_len:
                    max_len=length
                    index1=l
                    index2=r
                l-=1
                r+=1
            
        for i in range(len(s)):
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                length=r-l+1
                if length>max_len:
                    max_len=length
                    index1=l
                    index2=r
                l-=1
                r+=1
        
        return s[index1:index2+1]

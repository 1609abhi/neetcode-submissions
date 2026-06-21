class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.split(" ")
        s="".join(s)

        new_s=[]
        
        for char in s:
            if (ord("a")<=ord(char)<=ord("z") or ord("A")<=ord(char)<=ord("Z") or ord("0")<=ord(char)<=ord("9")):
                new_s.append(char)

        s="".join(new_s)      
        i=0
        j=len(s)-1
        while(i<=j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
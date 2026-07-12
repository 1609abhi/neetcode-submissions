from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        chars=["0","0","0","0"]
        visited=set(deadends)

        q=deque()
        q.append(("0000",0))
        visited.add("0000")
        
        while(q):
            char,step=q.popleft()
            if char==target:
                return step

            for i in range(4):
                cur=str((int(char[i])+1)%10)
                cur=char[:i]+cur+char[i+1:]
                if cur in visited:
                    continue
                else:
                    q.append((cur,1+step))
                    visited.add(cur)

            for i in range(4):
                cur=str((int(char[i])-1)%10)
                cur=char[:i]+cur+char[i+1:]
                if cur in visited:
                    continue
                else:
                    q.append((cur,1+step))
                    visited.add(cur)

        return -1



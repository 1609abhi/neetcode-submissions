from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)!= n-1:
            return False
        adj_list=[[] for _ in range(n)]
        visited_array=[False for _ in range(n)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(i):
            q=deque()
            q.append((i,-1))
            visited_array[i]=True

            while(q):

                node,parent=q.popleft()
                for neighbour in adj_list[node]:
                    if visited_array[neighbour]==False:
                        q.append((neighbour,node))
                        visited_array[neighbour]=True

                    elif visited_array[neighbour]==True and neighbour!=parent and parent != -1:
                        return True

            return False

        for i in range(n):
            if visited_array[i]==False:
                if bfs(i)==True:
                    return False

        return True
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=[[] for _ in range(numCourses)]
        indegree_array=[0 for _ in range(numCourses)]
        
        q=deque()

        for u,v in prerequisites:
            adj_list[v].append(u)
            indegree_array[u]+=1
        
        for i in range(len(indegree_array)):
            if indegree_array[i]==0:
                q.append(i)

        topo=[]

        while(q):
            node=q.popleft()
            topo.append(node)
            for neighbour in adj_list[node]:
                indegree_array[neighbour]-=1
                if indegree_array[neighbour]==0:
                    q.append(neighbour)

        if len(topo)==numCourses:
            return topo
        else:
            return []
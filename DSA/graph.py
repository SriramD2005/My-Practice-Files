from collections import defaultdict,deque
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def dfs(self,start):
        visited=set()
        stack=[]
        stack.append(start)
        while stack:
            node=stack.pop()
            if node not in visited:
                print(node,end=' ')
                visited.add(node)
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        print()
    def bfs(self,start):
        visited=set()
        queue=[]
        queue.append(start)
        while queue:
            node=queue.pop(0)
            if node not in visited:
                print(node,end=' ')
                visited.add(node)
            for i in self.graph[node]:
                if i not in visited:
                    queue.append(i)
                    
gr=graph()
gr.add(1,2)
gr.add(2,3)
gr.add(1,4)
gr.add(4,1)
gr.dfs(1)
gr.bfs(1)


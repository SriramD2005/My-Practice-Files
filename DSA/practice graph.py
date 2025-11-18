from collections import deque,defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add_edge(self,u,v):
        self.graph[u].append(v)
        
    def bfs(self,start):
        visited=set()
        queue=deque([start])
        while queue:
            
            vertex=queue.popleft()
            if vertex not in visited:
                print(vertex,end=' ')
                visited.add(vertex)
            for i in self.graph[vertex]:
                if i not in visited:
                    queue.append(i)
        print()
    def dfs(self,start):
        visited=set()
        stack=[start]
        while stack:
            vertex=stack.pop()
            if vertex not in visited:
                print(vertex,end=' ')
                visited.add(vertex)
            for i in reversed(self.graph[vertex]):
                if i not in visited:
                    stack.append(i)
g=graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,1)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(3,5)
g.add_edge(3,4)
g.add_edge(4,3)
g.add_edge(4,6)
g.add_edge(5,2)
g.add_edge(5,3)
g.add_edge(5,6)
g.add_edge(6,5)
g.add_edge(6,4)
print("bfs")
g.bfs(1)
print('dfs')
g.dfs(1)

from collections import defaultdict
from collections import deque
def dfsTopoUtil(v, visited, graph, stack):
    if visited[v]:
        return
    visited[v] = True
    for neighbour in graph[v]:
        if not visited[neighbour]:        
            dfsTopoUtil(neighbour, visited, graph,stack)
    stack.append(v)
def dfs_topo(graph):
    stack = []
    visited = [False for i in range(len(graph))]
    for node in graph.keys():
        dfsTopoUtil(node, visited, graph, stack)
    print(stack[::-1])
def khanTopoSort(vertices, edges):
    inDegrees = {v:0 for v in vertices}
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        inDegrees[v] += 1
    queue = deque([i for i in vertices if inDegrees[i] == 0])
    topo_order = []
    while queue:
        curr = queue.popleft()
        topo_order.append(curr)
        for neighbour in graph[curr]:
            inDegrees[neighbour] -= 1
            if inDegrees[neighbour] == 0:
                queue.append(neighbour)
    if len(topo_order) != len(vertices):
        raise Exception("the graph got cycle")
    return topo_order

if __name__ == "__main__":
    graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
    }
    print("DFS:")
    dfs_topo(graph)
    print("TOPOLOGICAL SORT")
    print(khanTopoSort([0,1,2,3,4,5,6,7],[
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5)
    ]))
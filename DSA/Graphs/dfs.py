#Adjacency list based
graph = {
    'A':['B', 'C'],
    'B':['A', 'E'],
    'C':['A', 'E', 'D'],
    'D':['C'],
    'E':['B', 'C']
}
def dfs(graph, start, visited):
    if start in visited:
        return
    visited.add(start)
    print(start, end = " -> ")
    for neighbour in graph[start]:
        dfs(graph, neighbour, visited)
dfs(graph, 'A', set())
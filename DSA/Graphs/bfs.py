from collections import deque
def bfs(graph, queue, visited):
    queue = deque(queue)
    queueElements = set(queue)
    while len(queue) != 0:
        curr = queue.popleft()
        visited.add(curr)
        for neighbour in graph[curr]:
            if (neighbour not in visited and neighbour not in queueElements):
                queue.append(neighbour) 
                queueElements.add(neighbour)
        print(curr, end = ' -> ')
graph = {
    'A':['B', 'C'],
    'B':['A', 'E'],
    'C':['A', 'E', 'D'],
    'D':['C'],
    'E':['B', 'C']
}
bfs(graph, ['A'], set())
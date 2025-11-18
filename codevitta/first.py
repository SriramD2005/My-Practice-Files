class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
    def setParent(self, parent):
        self.parent = parent
    def getParent(self):
        return self.parent

def bfs(start, destination, graph, visited):
    queue = [start]
    visited.add(start.value)
    while queue:
        current = queue.pop(0)
        if current.value == destination:
            path = []
            while current is not None:
                path.append(current.value)
                current = current.getParent()
            return path[::-1]
        for neighbor in graph.get(current.value, []):
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor_node = Node(neighbor, current)
                queue.append(neighbor_node)
    return None
def shortest_path():
    N, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    scout1, scout2 = map(int, input().split())
    destination = int(input().strip())
    visited1 = set()
    visited1.add(scout2)
    path1 = bfs(Node(scout1), destination, graph, visited1)
    if path1 is None:
        print("Impossible", end="")
        return
    print("path1:", path1)
    visited2 = set(path1[:-1])  # exclude destination
    visited2.add(scout1)        # block scout1’s start
    print(visited2)
    path2 = bfs(Node(scout2), destination, graph, visited2)
    if path2 is None:
        print("Impossible", end="")
        return

    count1 = len(path1) - 1
    count2 = len(path2) - 1
    print(count1 + count2, end="")

if __name__ == "__main__":
    shortest_path()
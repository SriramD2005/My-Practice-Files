import heapq
def minFileAccess(files):
    heapq.heapify(files)
    first = 0
    second = 0
    print(files)
    cost = 0
    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        cost += first + second
        heapq.heappush(files, first + second)
    return cost
print(minFileAccess([4, 8, 6, 12]))
import heapq

class MinPQ(object):
    def __init__(self):
        self.heap = []

    def pop(self):
        return heapq.heappop(self.heap)

    def push(self, priority, element):
        heapq.heappush(self.heap, (priority, element))

    def empty(self):
        return self.heap == []

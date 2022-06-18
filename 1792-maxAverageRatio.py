import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        stack = []
        heapq.heapify(stack)
        for i in classes:
            heapq.heappush(stack, (((i[0] / i[1]) - 1) / (i[1] + 1), i[0], i[1]))
        for i in range(extraStudents):
            rate, a, b = heapq.heappop(stack)
            if 1 - rate <= 10 ** (-6):
                return 1
            a += 1
            b += 1
            heapq.heappush(stack, (((a / b) - 1) / (b + 1), a, b))

        ans = 0

        for i in stack:
            ans += i[1] / i[2]

        return ans / len(stack)

s = Solution()
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
print(s.maxAverageRatio(classes, extraStudents))
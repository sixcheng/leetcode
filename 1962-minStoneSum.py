import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # 优先队列，大顶堆
        stack = []
        heapq.heapify(stack)
        for p in piles:
            heapq.heappush(stack, -p)
        for i in range(k):
            pile = -heapq.heappop(stack)
            pile = pile - int(pile/2)
            heapq.heappush(stack, -pile)
        return -sum(stack)

s = Solution()
piles = [5,4,9]
k = 2
print(s.minStoneSum(piles, k))
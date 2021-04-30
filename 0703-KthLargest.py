# -*- coding:utf-8 -*-
"""

Created on 2021/4/10
author：sixiaocheng
Description: 
"""

"""
703. 数据流中的第 K 大元素
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。


示例：

输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


提示：
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
最多调用 add 方法 104 次
题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
"""


class Heap(object):
    def __init__(self):
        """
        初始化，创建一个小顶堆
        :param desc:
        """
        self.heap = []
        # for i in range(len(nums)):
        #     self.push(nums[i])

    @property
    def size(self):
        return len(self.heap)

    def top(self):
        if self.size:
            return self.heap[0]
        return None

    def push(self, item):
        """
        入堆
        1、添加到堆末尾
        2、调整位置
        :param item:
        :return:
        """
        self.heap.append(item)
        self._sift_up(self.size - 1)

    def pop(self):
        """
        出堆
        1、弹出堆顶
        2、调整位置
        :return:
        """
        num = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return num

    def _sift_down(self, idx):
        while idx * 2 + 1 < self.size:
            new_idx = idx
            left = idx * 2 + 1
            right = idx * 2 + 2
            if self.heap[idx] > self.heap[left]:
                new_idx = left
            if right < self.size and self.heap[right] < self.heap[new_idx]:
                new_idx = right
            if new_idx == idx:
                break
            self.heap[idx], self.heap[new_idx] = self.heap[new_idx], self.heap[idx]
            idx = new_idx

    def _sift_up(self, idx):
        while idx:
            new_idx = (idx - 1) // 2
            if self.heap[idx] > self.heap[new_idx]:
                break
            self.heap[idx], self.heap[new_idx] = self.heap[new_idx], self.heap[idx]
            idx = new_idx


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = Heap()
        self.k = k
        for num in nums:
            self.heap.push(num)
            if self.heap.size > k:
                self.heap.pop()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.heap.push(val)
        if self.heap.size > self.k:
            self.heap.pop()
        return self.heap.top()


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))

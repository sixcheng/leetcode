from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        # 如果k为1时，只要返回cardPointetrs第一项和最后一项中的最大值即可
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])

        # left和right之间的区间k长度的滑动窗口，我们先取最右边的一种可能性
        left, right = len(cardPoints) - k, len(cardPoints) - 1

        temp = sum(cardPoints[left:right + 1])
        max_score = temp

        # 接下来就进行滑动求窗口和即可，注意当left等于0时就要停止循环了，因为我们是先移动指针再计算窗口
        # 如果left等于0时还继续循环，窗口和就会计算[1:1+k]的和了，左指针不能指到1
        while left != 0:
            # 当左指针或者右指针超过索引最大值时要和cardPointers的长度取模，指针就等于0了
            # 目的是维护一个长度为k的滑动窗口
            left = (left + 1) % len(cardPoints)
            right = (right + 1) % len(cardPoints)
            temp -= cardPoints[left - 1]
            temp += cardPoints[right]
            max_score = max(max_score, temp)

        return max_score


s = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(s.maxScore(cardPoints, k))
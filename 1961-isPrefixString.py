from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        char = ""
        for word in words:
            char += word
            if char == s:
                return True
        return False


so = Solution()
s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
print(so.isPrefixString(s, words))
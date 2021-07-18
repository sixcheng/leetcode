# -*- coding:utf-8 -*-
"""

Created on 2021/7/18
author：sixiaocheng
Description: 
"""


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        def count(itera):
            ans = [0] * 26
            for letter in itera:
                ans[ord(letter) - ord('a')] += 1
            return ans

        target = count(''.join([s.lower() for s in licensePlate if s.isalpha()]))
        new_words = []
        for word in words:
            if all((x1 <= x2 for x1, x2 in zip(target, count(word)))):
                new_words.append(word)
        new_words.sort(key=lambda word:len(word))
        return new_words[0]

s = Solution()
print(s.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]))

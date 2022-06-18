class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


s = Solution()
print(s.isPalindrome(12121))
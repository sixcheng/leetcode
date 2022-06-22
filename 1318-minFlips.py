class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            bit_a, bit_b, bit_c = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            if bit_c == 0:
                ans += bit_a + bit_b
            else:
                ans += int(bit_a + bit_b == 0)
        return ans


a = 2
b = 6
c = 5
s = Solution()
print(s.minFlips(a, b, c))

"""
2022.6.22魔镜，吃饼干
"""

# f(n) 吃n个饼的总方法数
# g(n) 连续2次吃1块饼吃到n块的方法数
# f(n) = f(n-1) + g(n-2)  # f(n-1)表示最后一次吃一个饼的方法数，g(n-2)表示最后一次吃2个饼的方法数，并且之前2次吃饼的个数都为1
# g(n) = f(n-2)  # f(n-2)表示最后一次吃2个饼的方法数
# g(n-2) = f(n-4)
# f(n) = f(n-1)+f(n-4)

# --------------
#  饼数  | 方法数
#   1   |   1
#   2   |   2
#   3   |   3
#   4   |   4
#   5   |   5
#   6   |   7
# --------------
# 时间复杂度On
# 空间复杂度O1,只需要维护几个变量
def eat_cookie(n):
    print("n =", n)
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    first = 1
    second = 2
    third = 3
    fourth = 4
    # 更新需要用到的数
    for i in range(5, n + 1):
        fifth = first + fourth
        first = second
        second = third
        third = fourth
        fourth = fifth
    return fourth


n = 20
print(eat_cookie(n))

#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根 
#
# https://leetcode.cn/problems/sqrtx/description/
#
# algorithms
# Easy (38.51%)
# Likes:    1513
# Dislikes: 0
# Total Accepted:    859.7K
# Total Submissions: 2.2M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 4
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)
    
        """
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

        """
# @lc code=end


#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#
# https://leetcode.cn/problems/add-binary/description/
#
# algorithms
# Easy (53.35%)
# Likes:    961
# Dislikes: 0
# Total Accepted:    302.9K
# Total Submissions: 567.7K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入:a = "11", b = "1"
# 输出："100"
# 
# 示例 2：
# 
# 
# 输入：a = "1010", b = "1011"
# 输出："10101"
# 
# 
# 
# 提示：
# 
# 
# 1 <= a.length, b.length <= 10^4
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零
# 
# 
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        
        我们可以设计这样的算法来计算：

            把 a 和 b 转换成整型数字 x 和 y，在接下来的过程中，x 保存结果，y 保存进位。
            当进位不为 0 时
                计算当前 x 和 y 的无进位相加结果：answer = x ^ y
                计算当前 x 和 y 的进位：carry = (x & y) << 1
                完成本次循环，更新 x = answer，y = carry
            返回 x 的二进制形式

        
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

        """
        # 使用倒叙的指针
        # x, y = len(a) - 1, len(b) - 1
        # result = []
        # l = 0
        # while x >= 0 and y >= 0:
        #     tmp = a[x] + b[y] + l
        #     if tmp < 2:
        #         result.append(str(tmp))
        #         l = 0
        #     else:
        #         result.append(str(0))
        #         l = 1
        #     x -= 1
        #     y -= 1
        # result = ''.join(result[::-1])
        # if x > 0:
        #     result = a[0:x] + result
        # if y > 0:
        #     result = b[0:y] + result
        # return result
        """_summary_
        (2, 2)
        (0, 4)
        (4, 0)
        Returns:
            _type_: _description_
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y # 11 ^ 01 = 10   / 10 ^ 10 = 00 
            carry = (x & y) << 1 # 11 & 01 = 01 << 10 / = 100
            x, y = answer, carry
            print(x, y)
        return bin(x)[2:]

        
# @lc code=end


#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# test-algorithms
# Easy (45.79%)
# Likes:    1057
# Dislikes: 0
# Total Accepted:    528.9K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        倒序遍历、整除、取模（取余）
        """
        level = 0
        i = len(digits) - 1
        t = 1
        while i >= 0:
            # 每一位数据加上 1 + 进位
            tmp = digits[i] + t + level
            # 当前位置保留加和的个位数
            digits[i] = tmp % 10
            # 加和的十位数，让他进位
            level = tmp // 10
            # 如果加和没有大于10 就不用继续处理了
            if level == 0:
                break
            t = 0
            i -= 1
        if level > 0:
            # 这里需要注意的是拼接的问题
            digits.insert(0, level)
        return digits
        
        
        
# @lc code=end


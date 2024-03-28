#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# algorithms
# Easy (75.68%)
# Likes:    1127
# Dislikes: 0
# Total Accepted:    485.8K
# Total Submissions: 641.8K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 
# 
# 示例 2:
# 
# 
# 输入: numRows = 1
# 输出: [[1]]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        # 这里控制的是行数
        for i in range(2, numRows + 1):
            pre_data = result[i - 2]
            cur_data = [1 for _ in range(i)]
            cur_i = 1
            while cur_i <= i - 2:
                cur_data[cur_i] = pre_data[cur_i - 1] + pre_data[cur_i]
                cur_i += 1
            result.append(cur_data)
        return result
        
# @lc code=end


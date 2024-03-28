#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#
# https://leetcode.cn/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (68.95%)
# Likes:    531
# Dislikes: 0
# Total Accepted:    300.5K
# Total Submissions: 435.8K
# Testcase Example:  '3'
#
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
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
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 
# 
# 示例 2:
# 
# 
# 输入: rowIndex = 0
# 输出: [1]
# 
# 
# 示例 3:
# 
# 
# 输入: rowIndex = 1
# 输出: [1,1]
# 
# 
# 
# 
# 提示:
# 
# 
# 0 
# 
# 
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？
# 
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # result = [[1]]
        # # 这里控制的是行数
        # for i in range(2, rowIndex + 2):
        #     pre_data = result[i - 2]
        #     cur_data = [1 for _ in range(i)]
        #     cur_i = 1
        #     while cur_i <= i - 2:
        #         cur_data[cur_i] = pre_data[cur_i - 1] + pre_data[cur_i]
        #         cur_i += 1
        #     result.append(cur_data)
        # return result[rowIndex]
        
        result = [1 for _ in range(rowIndex + 1)]
        # 这里控制行
        for i in range(3, rowIndex + 2):
            l = i - 1 - 1
            # 这里控制每行的数据
            while l > 0:
                result[l] = result[l] + result[l-1]
                l -= 1
        return result
# @lc code=end


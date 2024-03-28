#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel 表列序号
#
# https://leetcode.cn/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (71.45%)
# Likes:    406
# Dislikes: 0
# Total Accepted:    180.2K
# Total Submissions: 252.1K
# Testcase Example:  '"A"'
#
# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。
# 
# 例如：
# 
# 
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# 
# 
# 
# 示例 1:
# 
# 
# 输入: columnTitle = "A"
# 输出: 1
# 
# 
# 示例 2:
# 
# 
# 输入: columnTitle = "AB"
# 输出: 28
# 
# 
# 示例 3:
# 
# 
# 输入: columnTitle = "ZY"
# 输出: 701
# 
# 
# 
# 提示：
# 
# 
# 1 <= columnTitle.length <= 7
# columnTitle 仅由大写英文组成
# columnTitle 在范围 ["A", "FXSHRXW"] 内
# 
# 
#

import string

# @lc code=start
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        map_case = string.ascii_uppercase
        result = 0
        tmp = 1
        for i in columnTitle[::-1]:
            result += (map_case.index(i) + 1) * tmp
            tmp *= 26
        return result

# @lc code=end


#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#
# https://leetcode.cn/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (44.45%)
# Likes:    679
# Dislikes: 0
# Total Accepted:    153K
# Total Submissions: 343.6K
# Testcase Example:  '1'
#
# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
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
# 
# 示例 1：
# 
# 
# 输入：columnNumber = 1
# 输出："A"
# 
# 
# 示例 2：
# 
# 
# 输入：columnNumber = 28
# 输出："AB"
# 
# 
# 示例 3：
# 
# 
# 输入：columnNumber = 701
# 输出："ZY"
# 
# 
# 示例 4：
# 
# 
# 输入：columnNumber = 2147483647
# 输出："FXSHRXW"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

import string

# @lc code=start
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        
        采用"除2取余，逆序排列"法
        
        【算法描述】
            Step1.[取余] 用指定自然数n除以26，得到一个余数m。如果m = 0，置m←26。
            Step2.[转换为字符] 将m映射为字符c,映射规则是{1-26}->{A-Z}。然后将c拼接到26进制值s的左边，也就是置s←c + s。
            Step3.[去余降幂] 置n←(n–m)/26。如果n > 0，则回到Step1继续执行，否则进入Step4。
            Step4.[结束] 返回s。
        """
        map_case = string.ascii_uppercase
        result = ''
        while columnNumber > 0:
            mod = columnNumber % 26
            if mod == 0:
                mod = 26
            result = map_case[mod - 1] + result
            columnNumber = (columnNumber - mod) / 26
        return result
        
# @lc code=end


#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (37.84%)
# Likes:    6884
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 4.1M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s == s[::-1]:
            return s
        
        
        
# @lc code=end


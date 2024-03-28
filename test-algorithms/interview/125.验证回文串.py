#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
# https://leetcode.cn/problems/valid-palindrome/description/
#
# test-algorithms
# Easy (46.90%)
# Likes:    554
# Dislikes: 0
# Total Accepted:    385.7K
# Total Submissions: 822.2K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串
# 
# 
# 示例 2:
# 
# 
# 输入: "race a car"
# 输出: false
# 解释："raceacar" 不是回文串
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 字符串 s 由 ASCII 字符组成
# 
# 
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, data):
        """
        :type s: str
        :rtype: bool
        """
        if data == '':
            return True
        str_list = list(data)
        l, r = 0, len(str_list) - 1
        while l < r:
            # 判断字符串是否只包含数字和字母的函数为 isalnum()
            while not str_list[l].isalnum() and l < r:
                l += 1
            while not str_list[r].isalnum() and l < r:
                r -= 1
            if str(str_list[l]).lower() == str(str_list[r]).lower():
                l += 1
                r -= 1
                continue
            return False
        return True
# @lc code=end


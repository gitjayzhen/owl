#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#
# https://leetcode.cn/problems/length-of-last-word/description/
#
# test-algorithms
# Easy (40.81%)
# Likes:    483
# Dislikes: 0
# Total Accepted:    349K
# Total Submissions: 851.8K
# Testcase Example:  '"Hello World"'
#
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
# 
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "Hello World"
# 输出：5
# 解释：最后一个单词是“World”，长度为5。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "   fly me   to   the moon  "
# 输出：4
# 解释：最后一个单词是“moon”，长度为4。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "luffy is still joyboy"
# 输出：6
# 解释：最后一个单词是长度为6的“joyboy”。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词
# 
# 
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        
        指针倒叙遍历
        """
        # 1. 不使用内置方法 strip()
        # i = len(s) - 1
        # result = 0
        # while i >= 0:
        #     if s[i] == ' ' and result == 0:
        #         i -= 1
        #         continue
        #     elif s[i] == ' ' and result > 0:
        #         break
        #     result += 1
        #     i -= 1
        
        # 2. 使用内置方法
        # result = 0
        # s = s.strip()
        # i = len(s) - 1
        # while i >= 0:
        #     if s[i] == ' ':
        #         break
        #     result += 1
        #     i -= 1
        
        # 3. 不使用循环
        s = s.strip()
        tmp = s.split(' ')
        result = len(tmp[-1])
        
        return result
                            
            
            
# @lc code=end


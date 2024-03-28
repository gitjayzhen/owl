#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# test-algorithms
# Easy (44.63%)
# Likes:    3427
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "()"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "()[]{}"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(]"
# 输出：false
# 
# 
# 示例 4：
# 
# 
# 输入：s = "([)]"
# 输出：false
# 
# 
# 示例 5：
# 
# 
# 输入：s = "{[]}"
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由括号 '()[]{}' 组成
# 
# 
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        堆栈来进行消消乐
        """
        flag = { '(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            tmp = flag.get(i)
            if not stack:
                stack.append(tmp)
                continue
            if tmp == stack[-1]:
                stack.pop()
            else:
                stack.append(flag.get(i))
        return not stack
# @lc code=end


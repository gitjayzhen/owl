#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#
# https://leetcode.cn/problems/implement-strstr/description/
#
# test-algorithms
# Easy (41.11%)
# Likes:    1525
# Dislikes: 0
# Total Accepted:    700.1K
# Total Submissions: 1.7M
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
# 开始）。如果不存在，则返回  -1 。
# 
# 说明：
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf()
# 定义相符。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：haystack = "hello", needle = "ll"
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
# 
# 
#

# @lc code=start


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        
        滑动窗口
        """
        # 利用切片滑动索引，去匹配数据
        left, right = 0, len(needle)
        h_len = len(haystack)
        while right <= h_len:
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1
                
        
# @lc code=end


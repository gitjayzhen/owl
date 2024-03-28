#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (43.35%)
# Likes:    2159
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.3M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 
# 
# 示例 2：
# 
# 
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
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
        """
        index = 0
        n_len = len(needle)
        n_index = 0
        # 当 haystack 遍历完了，或者找到了目标 needle 就结束
        while index < len(haystack) and n_index < n_len:
            if haystack[index] == needle[n_index]:
                index += 1
                n_index += 1
            else:
                # 如果匹配过程中不相等了，就撤回一段已经遍历 needle 的长度
                index = index - n_index + 1
                n_index = 0
        # 如果是找到了第一额匹配的，n_index 应该等于 needle 的长度
        # 然后对应出现的开始下标，等于这个时候的 index 减去 needle 的长度
        return index - n_len if n_index == n_len else -1 
# @lc code=end


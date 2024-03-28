#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# test-algorithms
# Easy (42.74%)
# Likes:    2369
# Dislikes: 0
# Total Accepted:    895K
# Total Submissions: 2.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        https://leetcode.cn/problems/longest-common-prefix/solution/duo-chong-si-lu-qiu-jie-by-powcai-2/
        :type strs: List[str]
        :rtype: str
        
        数据结构
        """
        res = ""
        # zip 然后利用 set 集合
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

# @lc code=end


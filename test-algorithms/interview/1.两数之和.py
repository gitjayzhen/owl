#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#  target = a + b
#

# @lc code=start


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 利用 dict 的能力
        item_map = {}
        for index, value in enumerate(nums):
            tmp = target - value
            if tmp in item_map:
                return [item_map.get(tmp), index]
            item_map[value] = index
        return []

# @lc code=end


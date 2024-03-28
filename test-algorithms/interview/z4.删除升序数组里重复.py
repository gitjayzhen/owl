#!/usr/evn/bin python
# -*- coding=utf-8 -*-

"""
原地删除升序数组里重复的数字，并返回去重后的数组长度和数组
"""


def get_filter_list(nums):
    if not nums:
        return 0, []
    index = 0
    current = nums[index]
    while index < len(nums) - 1:
        if nums[index + 1] == current:
            nums.pop(index + 1)
            continue
        index += 1
        current = nums[index]
    return len(nums), nums


def length_of_longest_sub_string(s: str) -> str:
    left, right = 0, 1
    result = s[0]
    while right < len(s):
        while s[right] == s[right-1] and right < len(s) - 1:
            right += 1
        result = s[left:right] if right - left > len(result) else result
        left = right
        right += 1
        print(result, s[left:right], left, right)
    return result


if __name__ == '__main__':
    # print(get_filter_list([1, 1, 2, 2, 2, 2, 2, 5, 6, 6]))
    # print(get_filter_list([1, 1, 2, 3, 3, 4, 4, 5, 6, 6]))

    print(length_of_longest_sub_string('xxxxxdxxdddddwddddedddwdddd'))

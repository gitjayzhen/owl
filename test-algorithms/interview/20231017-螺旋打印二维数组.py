# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: 20231017-螺旋打印二维数组.py
@time: 2023/10/19 14:33
"""


def spiral_print(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    result = []

    while top <= bottom and left <= right:
        # Traverse top row
        result.extend(matrix[top][left:right + 1])
        top += 1

        # Traverse right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


if __name__ == '__main__':
    # 示例测试
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = spiral_print(matrix)
    print(result)

# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: test_opencv.py
@time: 2023/7/25 16:28
"""

import cv2

# 读取图像
image = cv2.imread('/Users/jayzhen/Desktop/Energy Consumption.png')

# 绘制矩形
start_point = (100, 100)
end_point = (300, 300)
color = (0, 255, 0)  # BGR颜色格式，这里使用绿色
thickness = 2
cv2.rectangle(image, start_point, end_point, color, thickness)

# 绘制圆形
center_coordinates = (200, 200)
radius = 50
cv2.circle(image, center_coordinates, radius, color, thickness)

# 绘制线段
start_point = (100, 400)
end_point = (300, 400)
cv2.line(image, start_point, end_point, color, thickness)

# 显示标记后的图像
cv2.imshow('Marked Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

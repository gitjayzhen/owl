# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: organize_files.py
@time: 2023/7/25 16:05
"""
import filecmp
import os
import shutil
import hashlib


def is_images_equal(a, b):
    from PIL import Image
    import numpy as np
    image1 = Image.open(a)
    image2 = Image.open(b)

    array1 = np.array(image1)
    array2 = np.array(image2)
    if np.array_equal(array1, array2):
        print("图片相等")
        return True
    else:
        print("图片不相等")
        return False


def is_images_equal_by_cv(a, b):
    import cv2
    image1 = cv2.imread(a)
    image2 = cv2.imread(b)

    difference = cv2.subtract(image1, image2)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("图片相等")
        return True
    else:
        print("图片不相等")
        return False


def is_images_base_info_equal(a, b):
    image1_path = a
    image2_path = b

    if (os.path.basename(image1_path) == os.path.basename(image2_path)) and \
            (os.path.getsize(image1_path) == os.path.getsize(image2_path)) and \
            filecmp.cmp(image1_path, image2_path):
        print("图片相等")
        return True
    else:
        print("图片不相等")
        return False


def get_file_hash(file_path):
    """
    计算文件的哈希值
    """
    with open(file_path, 'rb') as f:
        content = f.read()
        file_hash = hashlib.md5(content).hexdigest()
    return file_hash


def is_video_file(file_path):
    """
    检查文件是否为视频文件
    """
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv']  # 常见视频文件格式的扩展名列表
    _, ext = os.path.splitext(file_path)
    return ext.lower() in video_extensions


def organize_files(source_dirs, duplicate_dest, unique_dest):
    """
    整理文件
    """

    if not os.path.exists(duplicate_dest):
        os.makedirs(duplicate_dest)
    if not os.path.exists(unique_dest):
        os.makedirs(unique_dest)

    # 用于存储已经处理过的文件的哈希值和移动后的路径
    processed_files = {}

    # 用于存储重复的文件
    duplicate_files = []

    # 将不重复的文件移动到指定目录，并保留原文件的路径映射
    for source_dir in source_dirs:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = get_file_hash(file_path)
                print(file_path)
                if file_hash not in processed_files:
                    if is_video_file(file_path):
                        # dest_path = os.path.join(unique_dest, 'video', os.path.relpath(file_path, source_dir))
                        dest_path = os.path.join(unique_dest, 'video', os.path.basename(file_path))
                    else:
                        dest_path = os.path.join(unique_dest, 'image', os.path.basename(file_path))

                    dest_dir = os.path.dirname(dest_path)
                    os.makedirs(dest_dir, exist_ok=True)
                    shutil.move(file_path, dest_path)
                    processed_files[file_hash] = dest_path
                else:
                    shutil.move(file_path, os.path.join(duplicate_dest, os.path.basename(file_path)))
                    duplicate_files.append((file_path, processed_files[file_hash]))
    print(processed_files)
    print(duplicate_files)


if __name__ == '__main__':
    # 设置源文件夹路径
    source_dirs = [
        '/Users/jayzhen/20230620-icloud',
        # 可以继续添加其他源文件夹路径
    ]

    # 设置存放重复文件的目标文件夹路径
    duplicate_dest = '/Users/jayzhen/20230620/duplicate_dest'

    # 设置存放不重复文件的目标文件夹路径
    unique_dest = '/Users/jayzhen/20230620/unique_dest'

    # 执行整理文件操作
    organize_files(source_dirs, duplicate_dest, unique_dest)

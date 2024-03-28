def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print("排序后的数组:", arr)

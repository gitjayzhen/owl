
def length_of_longest_sub_string(s: str) -> str:
    left, right = 0, 1
    result = s[0]
    while right < len(s):
        while s[right] == s[right-1] and right < len(s) - 1:
            right += 1
        result = s[left:right] if right - left > len(result) else result
        left = right
        right += 1
        # print(result, s[left:right], left, right)
    return result


if __name__ == '__main__':
    print(length_of_longest_sub_string('xxxxxdxxdddddwddddedddwdddd'))


def check_string(data):
    if data == '':
        return True
    str_list = list(data)
    l, r = 0, len(str_list) - 1
    while l < r:
        # 判断字符串是否只包含数字和字母的函数为 isalnum()
        while not str_list[l].isalnum():
            l += 1
        while not str_list[r].isalnum():
            r -= 1
        if str(str_list[l]).lower() == str(str_list[r]).lower():
            l += 1
            r -= 1
            continue
        return False
    return True
    
    
#    if s == '':
#         return True
#     l, r = 0, len(s) - 1
#     while l < r:
#         # 判断字符串是否只包含数字和字母的函数为 isalnum()
#         while l < r and not s[l].isalnum():
#             l += 1
#         while l < r and not s[r].isalnum():
#             r -= 1
#         if str(s[l]).lower() == str(s[r]).lower():
#             l += 1
#             r -= 1
#             continue
#         return False
#     return True


if __name__ == "__main__":
    print(check_string("A man, a plan, a canal: Panama"))
    print(check_string("race a car"))
    
    
    # # 首先通过filter函数剔除字符串中的非字母和数字
    # # 通过join函数将结果串联起来，并返回小写
    # string = ''.join(filter(str.isalnum, s)).lower()
    # # 通过比较字符串和逆序是否相等，判断是否为字符串
    # return string == string[::-1]
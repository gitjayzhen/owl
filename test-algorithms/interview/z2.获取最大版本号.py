
def get_max_version(version_list):
    """求版本号中的最大版本号

    Args:
        version_list (_type_): 版本号列表

    Returns:
        _type_: 返回最大的那个版本号
    """
    if not version_list:
        return ''
    result = version_list[0]
    for version in version_list[1:]:
        i_len, res_len = len(version), len(result)
        max_len = max(i_len, res_len)
        n = 0
        while n < max_len:
            a = version[n] if n < i_len else 0
            b = result[n] if n < res_len else 0
            if a != '.' and b != '.' and int(a) > int(b):
                result = version
                break
            n += 1
    return result

print(get_max_version(['6.2.0', '6.3.1', '6.3.1.2', '6.3.1.0']))
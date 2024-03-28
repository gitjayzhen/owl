from decimal import Decimal
import random

# [0, 1) round Decimal(random.random() * _max / 2).quantize(Decimal("0.00"))
# 群发红包

def get_data(size, member):
    result = []
    _min = 0.01
    _max = size - member * _min
    consume = 0.0
    for _ in range(member - 1):
        tmp = round(random.random() * _max, 2)
        tmp = tmp if tmp != 0 else _min
        consume += tmp
        result.append(tmp)
        _max = round(_max - tmp, 2) if _max - tmp > 0 else 0.01
    print(size, _max, consume)
    result.append(round(size - consume, 2))
    return result


data = get_data(100, 10)
result = 0.0
for i in data:
    result += i
print(result, data)

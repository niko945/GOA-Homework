import math
def square_or_square_root(arr):
    result = []
    for num in arr:
        root = math.isqrt(num)
        if root * root == num:
            result.append(root)
        else:
            result.append(num * num)
    return result




def sum_mix(arr):
    return sum(int(x) for x in arr)
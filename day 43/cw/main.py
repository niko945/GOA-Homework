def descending_order(num):
    num_str = str(num)
    
    digits = list(num_str)
    digits.sort(reverse=True)
    
    sorted_num_str = ''.join(digits)
    result = int(sorted_num_str)
    return result


    
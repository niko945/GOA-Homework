def get_middle(s):
    length = len(s)
    
    
    if length % 2 == 1:
        
        middle_index = length // 2
        return s[middle_index]
    else:
        
        middle_left = (length // 2) - 1
        middle_right = length // 2
        return s[middle_left] + s[middle_right]
    


def xo(s):
    s = s.lower()
    
    x_count = s.count('x')
    
    o_count = s.count('o')
    
    return x_count == o_count


def to_jaden_case(string):
    words = string.split()
    
    capitalized_words = []
    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)
    
    jaden_case_string = ' '.join(capitalized_words)
    
    return jaden_case_string


def find_short(s):
    words = s.split()
    
    shortest_length = len(words[0])
    
    for word in words:
        if len(word) < shortest_length:
            shortest_length = len(word)
    
    return shortest_length



def accum(st):
    result = []
    
    for i in range(len(st)):
        letter = st[i]
        part = letter.upper() + letter.lower() * i
        result.append(part)
    
    return '-'.join(result)


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
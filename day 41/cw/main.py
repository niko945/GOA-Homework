def is_palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s == s[::-1]



def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)


def reverse_seq(n):
    return list(range(n, 0, -1))
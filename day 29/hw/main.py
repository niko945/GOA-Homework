def sum_of_odds(numbers):
    return sum(num for num in numbers if num % 2 != 0)

# Example usage:
# my_list = [1, 2, 3, 4, 5]
# print(sum_of_odds(my_list))  # Output: 9
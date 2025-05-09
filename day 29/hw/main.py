def sum_of_odds(numbers):
    return sum(num for num in numbers if num % 2 != 0)

def filter_four_letter_names(names):
        return [name for name in names if len(name) == 4]

def divisible_by_three_and_five(numbers):
            return [num for num in numbers if num % 3 == 0 and num % 5 == 0]


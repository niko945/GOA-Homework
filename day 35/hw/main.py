# Custom ფუნქციები არის მომხმარებლის მიერ შექმნილი ფუნქციები, რომლებიც გარკვეულ ამოცანებს ასრულებენ.

def num(a, b):
    return a + b


def check_even(num):
    if num % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

def micro(num):
    return num ** 2

def to_upper(text):
    return text.upper()


def name(saxeli, gvari):
    print(f"სახელი: {saxeli}, გვარი: {gvari}")
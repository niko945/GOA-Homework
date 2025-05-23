my_surname = "mdivani"

user_surname = input("Please enter your surname: ")


if my_surname.lower() == user_surname.lower():
    print("Our surnames are similar.")
else:
    print("We have different surnames.")



food = ["chips", "soda", "candy", "burger"]

    
food.pop(0)  
food.append("salad") 

food.pop(0)  
food.append("water")  

food.pop(0) 
food.append("fruit") 

food.pop(0) 
food.append("grilled chicken")  

print("Final food list:", food)


my_name = "nika"

user_name = input("Please enter your name: ")

if my_name[0].lower() == user_name[0].lower() and my_name[-1].lower() == user_name[-1].lower():
    print(2)
elif my_name[0].lower() == user_name[0].lower() or my_name[-1].lower() == user_name[-1].lower():
    print(1)
else:
    print(0)
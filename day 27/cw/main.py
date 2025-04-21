def my_function(fnum, lnum):
  print(fnum + " " + lnum)
my_function("5", "6")


def hello(fname):
  print(fname + " " + "heloo")
hello("nika")


def name(fname):
  print(fname + " " + "გამარჯობა")
name("dadu")
name("luka")
name("saba")



#replace = შეუძლია მოცემულ ცვლადს შეცვალოს მერორე ცვლადით
num = "5"

x = num.replace("5", "8")

print(x)

car = "I like merc"

x = car.replace("merc", "BmW")

print(x)



#.UPPER -  ის ასოს აქცევს დიდად
#.LOWER - ის დიდ ასოებს აქცევს პატარა ასოებათ

txt = "hello"

x = txt.upper()

print(x)


txt = "HELLO"

x = txt.lower()

print(x)




#find - შეუძლია ცვლადში იპოვოს სიტყვა რასაც ეტყვი რომ გიპოვოს

txt = "მე მიყვარს ბანანი."

x = txt.find("ბანანი")

print(x)



#capitalize - ის პირველ ასოს აქცევს დიდიად

txt = "welcome to my life."

x = txt.capitalize()

print (x)

# swapcase - აკეთებს დიდი ასოების შემდეგ რომ არის პატარა ასოები შემდეგ 
# ისინი ცვლიან და პატარები ხდებიან დიდები და დიდები რაც იყო ხდება პატარა
txt = "Heloo My Name Is Nika"


x = txt.swapcase()

print(x)
# 1)
# input —-> პროგრამაში მომხმარებლისგან ინფორმაციი მიღება.
# output —- > ეკრანზე ინფორმაციის ჩვენება.

# 2)
value = input("write an input: ")
print(type(value))

# 3)
name = "Saba"
city = "Tbilisi"
faw_car = "BMW"
faw_fruit = "Apple"
faw_color = "Blue"

age = 14
year = 2025
points = 100
days = 7
height_cm = 170

weight = 55.5
temperature = 36.6
price = 19.99
speed = 12.4
score = 88.8

# 4)
name = "Saba" 
age = 14 
height = 1.70

print(type(name))
print(type(age))
print(type(height))

# 5)
word1 = input("write  the first word: ")
word2 = input("write the second word: ")
sentence = word1 + " " + word2
print(sentence)

# 6)
num1 = float(input("write the first number: "))
num2 = float(input("write the second number: "))
num3 = float(input("write the third number:" ))
num4 = float(input("write the fourth number:" ))
num5 = float(input("write the fifth number:" ))
average = (num1 + num2 + num3 + num4 + num5) / 5
print("the average of this numbers are ", average)

# 7)
name = input("writhe your name: ")
surname = input("writhe your surname: ")
age = input("writhe your age: ")
height = input("writhe your height: ")
weight = input("write your weight: ")
print("My name is", name, surname + ", I am", age, "years old,", "my height is", height, "cm and I weigh", weight, "kg.")
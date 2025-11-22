# 1)

# ==   ტოლია
# !=   არ არის ტოლი
# >    მეტია
# <    ნაკლებია
# >=   მეტია ან ტოლია
# <=   ნაკლებია ან ტოლია

print(5 == 5)
print(10 == 3)
print("hi" == "hi")
print(2 + 2 == 4)
print(True == True)

print(5 != 3)
print(10 != 10)
print("a" != "b")
print(4 != 2 + 3)
print(False != True)

print(5 > 3)
print(10 > 20)
print(7 > 7)
print(100 > 50)
print(-1 > -5)

print(3 < 5)
print(20 < 10)
print(7 < 7)
print(-2 < 4)
print(0 < 1)

print(5 >= 5)
print(10 >= 3)
print(4 >= 10)
print(2 >= 2)
print(-1 >= -3)

print(5 <= 6)
print(10 <= 2)
print(7 <= 7)
print(-3 <= -1)
print(0 <= 0)

# 2)

# and → ორივე პირობა უნდა იყოს True
# or → საკმარისია ერთი პირობა True იყოს
# not → აბრუნებს პირიქით მნიშვნელობას

# 3)

print(5 > 2 and 10 > 5)
print(3 == 3 and 4 < 1)
print(True and False)

print(5 > 10 or 3 < 4)
print(2 == 2 or 2 == 3)
print(False or False)

print(not True)
print(not (5 > 3))
print(not (10 == 10))

# 4)

my_number = 20
user_num = int(input("Enter a number: "))

if user_num > my_number:
    print("Your number is greater.")
else:
    print("Your number is not greater.")

# 5)

my_name = "Saba"
user_name = input("Enter your name: ")

if user_name == my_name:
    print("The name matches exactly.")
else:
    print("The name does not match.")

# 6)

age = int(input("Enter your age: "))

if age > 18:
    print("You are older than 18.")
else:
    print("You are not older than 18.")
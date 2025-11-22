# 1)
# Boolean არის ტიპი, რომელიც მხოლოდ True ან False მნიშვნელობას იღებს.
# მაგალითად: 5 > 3 -> True, 2 > 4 -> False


# 2)
# Binary code არის კომპიუტერის ენა 0-ებითა და 1-ებით.
# 1 = ON, 0 = OFF

# 3)
# bool() გადაკეთებს რაღაცას True ან False-ში
# მაგალითად: bool(5) = True, bool(0) = False

# 4)
a = 10
b = 20
print(a == b)

# 5)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("The first number is bigger")
elif x < y:
    print("The second number is bigger")
else:
    print("The numbers are equal")

# 6)
word = input("Enter a word: ")
print(word == "Python")

# 7)
num = int(input("Enter a number: "))
print(num > 100)

# 8)
password = input("Enter password: ")
print(password == "Python123")

# 9)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a > b)
print(a < b)
print(a == b)

# 10)
s1 = input("Enter first word: ")
s2 = input("Enter second word: ")
s3 = input("Enter third word: ")
s4 = input("Enter fourth word: ")
s5 = input("Enter fifth word: ")
result = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5
print(result)

# 11)
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))
avg = (n1 + n2 + n3 + n4) / 4
print(avg)

# 12)
a = 10
b = 5.7
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 13)
s1 = "Hello"
s2 = "hello"
print(s1 == s2)

# 14)
x1 = "40"
x2 = "20"
x3 = "15"
x4 = "25"
sum_all = int(x1) + int(x2) + int(x3) + int(x4)
print(sum_all)

# 115)
a = 30
b = 40
c = 50
print(int(a), int(b), int(c))
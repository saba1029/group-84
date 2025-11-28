# 1.
5 > 2
10 == 10
7 != 3
4 <= 4
(True and True)

3 > 10
5 == 6
8 < 2
9 <= 1
(False or False)

# 2.
# Sequencing - ეს არის პროგრამის ნაბიჯ-ნაბიჯ შესრულება ზუსტად იმ მიმდევრობით, როგორც კოდში წერია, მაგალითად: ზემოდან ქვემოთ
# Iteration - როცა ერთი და იგივე კოდი მეორდება რამდენჯერმე.
# Selection - არჩევანი პირობებზე დამოკიდებულებით.

# 3.
print("Hello")
print("How are you?")
print("Goodbye")
# ეს არის sequencing, რადგან კოდი ზუსტად იმ რიგით დაიწერება, რა მიყოლებითაც წერია წერია: ჯერ Hello, მერე How are you?, მერე Goodbye.

# 4.
# for loop არის ციკლი, რომელიც ერთსა და იმავე კოდს ასრულებს რამდენჯერმე. მაგალითად: რამის გამეორება, სიაზე გავლა, range() შორის წვდომა და ასე შემდეგ.

# 5.
# range() ფუნქციას გადაეცემა რიცხვები, მაგალითად range(5) ნიშნავს შექმნას რიცხვები 0-დან 4-მდე. for loop გადის ამ რიცხვებზე და თითოეულზე ასრულებს კოდს.

# 6.
for i in range(5):
    print("BMW")

# 7.
for i in range(100):
    print("Elizbarashvili")

# 8.
for i in range(46):
    print("Blue")

# 9.
for i in range(32):
    print("S")

# 10.
a = input("Enter your word 1: ")
b = input("Enter your word 2: ")
c = input("Enter your word 3: ")
d = int(input("Enter the number: "))

result = a + b + c + str(d)
print(result)

# 11.
a = 10
b = "Hello"
c = 3.14
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 12.
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
num4 = int(input("Number 4: "))

print("Sum:", num1 + num2 + num3 + num4)
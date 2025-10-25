#integer ეს არის მთელი რიცხვი. გამოიყენება, როცა გვჭირდება მთლიანი რიცხვები.
#float ეს არის ათწილადი. გამოიყენება ზუსტი მნიშვნელობებისთვის, როცა საჭიროა წერტილის შემდეგი ციფრებიც.
#string ეს არის ტექსტი რომელიც ბრჭყალებშია მოქცეულიგამოიყენება ტექსტის შესანახად.

a = float(input(10))
b = float(input(20))
c = float(input(30))
average = (a + b + c) / 3
print("avearage is ", average)

a = float(input(213))
b = float(input(928))
sum =  a + b
print("ორი რიცხვის ჯამია:", sum)

my_name = input("saba")
little_sister = input("nia")
big_sister = input("nini")
mother_name = input("teo")
father_name = input("giorgi")
sentence = "my name is " + my_name + ", my big sisters name is " + big_sister +   ", my little sisters name is " + little_sister +   ", my mothers name is " + mother_name + ", my fathers name is — " + father_name + "."
print(sentence)
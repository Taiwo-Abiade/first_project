import math
print("Hello World")
print("*"*10)
print("Hesychia To The World ")
print(10*5)
print("Alexsmith" + "Samsmith")
Name = "Taiwo"
Age = "15"
Class = "Done With School"
# using of input
name = ("john smith ")
age = 20
status = ("new patient")
print(name, age, status)


print(Name)
print(Age)
print(Class)
Taiwo = "Hello_world"
print(Taiwo)
mul = 15*10
print(mul)
Div = 300/5
print(Div)
Student_Count = 1000
Taiwo
course = "Abiade_Taiwo"
print(len(course))
print(course[0:5])
Taiwo = " python\n_this"
print(Taiwo)
# joining of two strings
first = "Taiwo"
last = "kenny"
full = first + " " + last
print(full)
first0 = 'yusuf'
last0 = 'yusuf'
full0 = f"(first0) (last0)"
print(full)
var = "kenny"
var2 = "taiwo"
full1 = f"{len(var)} {2 + 2}"
print(full.upper())
print(full.lower())
print(full)
print(full.find("wo"))
print(full.replace("T", "f"))
print("pro" in full)
print("pro" not in full)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))
vol = "taiwo"
print(type(vol))
bag = 30

# example on if or else statment
if bag < 50:
    print("True")
elif bag < 40:
    print("yes")


else:
    print("False")
 # more example on the if or else statemet
age = 22
if age >= 18:
    print('eligable')
elif age == 17:
    print('which month')
else:
    print("not eligable")

    # using the and or not operator
high_income = True
good_credit = True
if high_income and good_credit:
    print("eligable")
else:
    print("not_eligable")
    high_income = False
# using or
good_credit = True
if high_income or good_credit:
    print("eligable")
else:
    print("not_eligable")

    # using  not
high_income = False
good_credit = True
student = False
if not student:
    print("eligable")
else:
    print("not_eligable")
    # example of the three
high_income = True
good_credit = False
student = False
if (high_income or good_credit) and not student:
    print("eligable")
else:
    print("not_eligable")


    #trying if and else statment 
weight = int (input ('weight :'))
unit = input('(L)bs or (k)bs:')
if unit.upper() =="L":
    converter = unit * 0.45
    print (f" you are {converter}kilos")
else:
    unit.upper =='(k)g'
    converter = unit / 0.45
    print (f"you are {converter}pounds")

    # another complex example
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and student or not student:
    print("eligable")
else:
    print("not_eligable")


high_income = False
good_credit = True
student = True
if high_income and good_credit and student:
    print("eligable")
else:
    print("not_eligable")

# if age should be 18 and 65
age = 17
if age >= 18 and age < 65:
    print("eligabel")
elif age == 17:
    print('under_consideration')




# my experiment.txt
CFP = ("charge full price")
users_price = float(input("price:"))
items = int(input('how many items are you getting :'))
total_cost = items * price
if total_cost > 10000:
    print("you would be given 10% discount")
    print(f"your total is @{total_cost}")
else:
    print(f"your total is @{total_cost}")
    print(CFP)



# mathematical way to write the program
age = 22
if 18 <= age < 65:
    print("eligable")

    # introduction  to loop
for number in range(5):
    print("attempt", number)
    for number in range(1, 4):
        print("attempt", (number + 1), (number * "."))
        break
# example using loops
    for number in range(1, 10,  2, ):
        print("attempt", number, (number*'.'))
        break
# creating complex loops
    Successful = False
    for number in range(3):
        print("attempt")
    if Successful:
        print("Successful")
        break
    else:
        print("atttempted 3 times  and no result")

# using loops diffrently
for x in range(5):
    for y in range(2):
        print(f"({x}, {y})")
        break
# introduction to while loop
number = 10
while number > 0:
    print(number)
    number //= 2
    break

    # forever loop
    number = 5
while number > 0:
    print("hesychia_is_always_right")
    break


# trying to use while loops in maths
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numnbers")


# creating a variable with the def fuction `
def greeen():
    print("hello there")
    print("whats up")


greeen()

# creating a variable with the def fuction * 2 `


def greeen(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("whats up")


greeen("mosh", "hammedani")


# taiwo project #
def taiwo(x, y):
    return x * y


answer = taiwo(10, 12)
final_answer = answer / 60
print(final_answer)


# taiwo project.txt 1
taiwo_age = 16
kenny_age = 16
cutoff_mark = 150
waec_mark = 30
if taiwo_age and kenny_age == 16 and cutoff_mark > 60:
    if True and waec_mark > 29:
        print("you are good to go")
    print("their waec and jamb should be fowarded to lasu portal")
elif taiwo_age and kenny_age == 15 or 17:
    print("can go for jupeb")

else:
    print("they are not of age or did not meet the requiured cutoff mark")

# creating a variable with the def fuction * 2 `


def greeen(name):
    print(f"hi {name}")
    print("whats up")


print(greeen("hesychia"))


# my txt.experiment


def his_green(a, b):
    return a * b


answer = his_green(4, 5)
final_answer = answer + 10
print(final_answer)


# trying to multiply
def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 3, 4, 5))


# my actual test
def create(input):
    if (input % 5 == 0) and (input % 3 == 0):
        print("fizzbuzz")
    elif input % 5 == 0:
        print("buzz")
    elif input % 3 == 0:
        print("fizz")
    else:
        print(input)


# creating a guessing game
correct_pass = 3
guess = 0
guess_count = 2
while guess < guess_count:
    count = int(input('guess!'))
    guess += 1
    if count == correct_pass:
        print("thats  good ")
        break
else:
    print('you lost')
    # creating a car game 
command = ""
while command != "quit":
    command = input(">").lower()
    if command == "start":
        print("the car started")
    elif command == 'stop':
        print("the car stopped")
    elif command == "help":
        print("""
start - to start the car 
stop - to stop the car 
quit - to stop game 
        """)
    else:
        break
# modifying  a car game
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is alredy started ")
        else:
            started = True
            print(" car started")

    elif command == 'stop':
        if not started:
            print("car i alredy stopped ")
        else:
            started = False
            print("the car stopped")
    elif command == "help":
        print("""
start - to start the car ~
stop - to stop the car 
quit - to stop game 
        """)
    elif command == "quit":
        break

    else:
        print("sorry i dont understand ")


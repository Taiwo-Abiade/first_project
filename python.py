
price = 10_000
has_good_payment = True
if has_good_payment:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"down_payment:{down_payment}")


high_income = True
good_credit = True
if high_income and good_credit:
    print("eligable for loan ")


temperature = 50
if temperature > 30:
    print("its a hot day")
elif temperature < 10:
    print("its a cold day")
else:
    print("its neither cold nor hot")


name = "taiwo"
if (len(name)) < 3:
    print("nmae must be at list 3 character long")
elif (len(name)) > 50:
    print("name can be a maximum of 50")
else:
    print("name looks good ")
# my experiment.txt

users_price = float(input("price:"))
items = int(input('how many items are you getting :'))
total_cost = items * price
if total_cost > 10_000:
    print("you would be given 10% discount")
    print(f"your total is {total_cost}")

else:
    print(f"your total is @{total_cost}")
    print("charge_full_price")




i = 1
while i <= 5:
    print ("i is less than 5")
correct_pin = 1234
balance = 10000
trial = 0
trial_count = 3

while trial < trial_count:
    pin = int(input("pin:"))
    trial += 1
    if pin == correct_pin:
        print("login successful")
        print("""
Welcome to your ATM

1. check Balance
2. Deposit money
3. Withdraw money
4. Exit
   """)
    else:
        print("incorrect pin")
if trial < trial_count:
    print("Try Again")
else:
    print("you have used all your attempt")
    print("loading...")
    print("loading...")
    print(' Access denied')

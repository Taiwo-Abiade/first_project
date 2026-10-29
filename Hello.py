# taiwo project.txt 1
taiwo_age = 12
kenny_age = 21
cutoff_mark = 150
waec_mark = 60
if taiwo_age and kenny_age >= 16 and cutoff_mark >=60:
    if True and waec_mark > 29:
        print("you are good to go")
    print("their waec and jamb should be fowarded to lasu portal")
if taiwo_age and kenny_age == 15:
    print("can go for jupeb")

else:
    print("they are not of age or did not meet the requiured cutoff mark")
    while True:
        mark = i











        Age = 16
jambcutoff_mark = 150
waec_mark = 60

trial = 0
trial_count = 2

# waec = int(input("waec score >"))
# jamb = int(input("jamb score >"))
# candidate_age = int(input("your age >"))


while trial < trial_count:

    trial += 1
    waec = int(input("waec score >"))
    #jamb = int(input("jamb score >"))
    if waec > waec_mark and jamb > jambcutoff_mark:
            print("""
your waec result has been checked and you passed
for further info check your jamb
    """)
            print("""
your jamb result has been checked and found creditable 
proceed to jamb  caps and fill in the required
                     """)
            break
    elif waec < waec_mark and jamb < jambcutoff_mark:
        print(""" 
loading ...
loading ...
you did not reach the required court off mark
sorry you can try again next year
        """)
    if trial == trial_count:
        print("used up trial try again in an hour time")
    else:
         print ("try again")
         break












      # candidate_age = int(input("your age >")
         

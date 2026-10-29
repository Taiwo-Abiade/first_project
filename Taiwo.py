Age = 16
jambcutoff_mark = 150
waec_cutoff_mark = 60

# MACX_NO_OF_TRIES = 2
trial = 0
trial_count = 2

# waec = int(input("waec score >"))
# jamb = int(input("jamb score >"))
# candidate_age = int(input("your age >"))


while trial < trial_count:

    trial += 1
    waec = int(input("waec score >"))
    #jamb = int(input("jamb score >"))
    if waec > waec_cutoff_mark:
            print("""
your waec result has been checked and you passed
for further info check your jamb
    """)

     
    elif waec < waec_cutoff_mark:
        print(""" 
loading ...
loading ...
you did not reach the required court off mark
sorry you can try again next year
        """)
    if trial == trial_count and False :
        print("used up trial try again in an hour time with your cridentials ready to upload")
        break


    if True:
         jamb =int (input("jamb score  >" ))
         if jamb > jambcutoff_mark:
              print("""
your jamb result has been checked and found creditable 
proceed to jamb  caps and fill in the required
                     """)
         print("would you like to proceed to jamb caps >")
         jamb_caps = (input("y/n"))
         if jamb_caps == "y".lower:
              print("you would be redirected to jamb caps in a while")
              













      # candidate_age = int(input("your age >")
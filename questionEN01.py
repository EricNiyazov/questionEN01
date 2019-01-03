
test = False
q1 = print("what's 9 + 10")
grade = 0
rage = 0
print(" ")
print("1. 19 ")
print("2. 21 ")
print("3. an old meme that was never funny ")
print("4. 69420 ")

while test == False:
    try:
        a1 = int(input(" "))
        if a1 == 1:
            print ("ok very good on fun freddy")
            grade += 1
            test = True
        elif 4 >= a1 > 1:
            print("bro. r u dumb its basic math")
            test = True
        elif a1 > 4:
            print ("no answers more then 4 duh")
        else:
            print ("no answers less then 1 duh")
    except ValueError:
        print("answer must be a integer 1,2,3 or 4")   
print("your grade is",grade,)

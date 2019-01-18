def main():
     #problem1()
    #problem2()
     #problem3()
    problem4()


#Create a function with two variables. One should equal “My name is: “
# and the other should equal your actual name.
# Print the two variables in one print message.

def problem1():
    var1 = "My name is"
    var2 = "Betty"
    print(var1 + " " + var2)


#Create a function to ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not
# enough extra credit.” If they entered more than 20 print
# “That’s too much extra credit”.

def problem2():
    extraCredit = int(input("How much extra credit?"))
    if (extraCredit<5):
        print("That's not enough extra credit.")
    elif (extraCredit>20):
        print("That's too much extra credit.")


#Create a function to ask a user to enter a password. Enter a password.
# Ask user to reenter password. Check to see if they are correct.

def problem3():

     userInput1 = input("Enter a password")
     userInput2 = input("Re-enter password")
     if userInput1 == userInput2:
         print("Access granted")


#Create a function to ask for two card numbers. If it equals 21 print BLACKJACK!,
# if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”

def problem4():
    var1 = int(input("Enter card number"))
    var2 = int(input("Enter card number"))
    cardSum = (var1 + var2)
    if cardSum == 21:
        print("BLACKJACK!")
    elif cardSum > 21:
        print("BUST!")
    elif cardSum < 21:
        print("The total is " + cardSum)

main()







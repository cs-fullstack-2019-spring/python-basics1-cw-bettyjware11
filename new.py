def problem2():
    extraCredit = int(input("How much extra credit?"))
    if (extraCredit < 5):
        print("That's not enough extra credit.")
    if (extraCredit > 20):
        print("That's too much extra credit.")
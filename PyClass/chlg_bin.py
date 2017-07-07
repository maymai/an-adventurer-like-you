"""
Create a program that will take one number and return its binary equivalent.
Max - 65535
"""
def binarise():
    dec = input("Choose a number: ")
    check = 0
    while check == 0:
        try:
            reminder = int(dec)
        except ValueError:
            dec = input("It nust be a number, try again:")
        else:
            break
    power = 0
    binnum = []
    while reminder > 0:
        if 2 ** power == reminder:
            print("2 ** {0} = {1}".format(power, reminder))
            binnum.append(power)
            print("Reminder = {0} - {1} = {2}".format(reminder, str(2 ** power), str(reminder - 2 ** power)))
            reminder -= 2 ** power
            power = 0
        elif 2 ** power > reminder:
            print("2 ** {0} > {1}".format(power, reminder))
            binnum.append(power - 1)
            print("Reminder = {0} - {1} = {2}".format(reminder, str(2 ** (power - 1)), str(reminder - 2 ** (power - 1))))
            reminder -= 2 ** (power - 1)
            power = 0
        elif 2 ** power < reminder:
            power += 1
    total = 0
    for i in binnum:
        total += 10 ** i
    print("{0} in binary is {1}".format(dec, total))

binarise()

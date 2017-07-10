"""
Write a small program to ask for a name and age.
When both values have been entered, check if the person is 18-30 years old.
If so, welcome them, otherwise, refuse them entry.
"""
def entry(name, age):
    try:
        age = int(age)
    except:
        print("Your age must be a number")
        age = input("Please enter your age:")
        entry(name, age)
    else:
        if 18 <= age <= 30:
            print("Hello {0}, Welcome!".format(name))
            return True
        elif age < 18:
            print("Sorry, please come back in {0} years.".format(str(18-age)))
            return False
        else:
            print("Sorry, it's time you grow up.")
            return False

name = input("Please enter your name:")
age = input("How old are you, {0}?".format(name))
entry(name, age)

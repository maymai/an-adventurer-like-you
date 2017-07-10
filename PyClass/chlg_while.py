"""
Create a number guessing game that generates a random number
and the user has to guess the number.
Allow for as many attempts as required, with indecations of higher or lower.
Inserting "0" quits the game.
## Extra ##
Create a high score!
"""
import random
import pickle

def numguess():
    try:
        with open("top5", "rb") as top5:
            cache = pickle.load(top5)
    except FileNotFoundError:
        cache = {}
    print("High scores per max number:")
    for i in cache:
        print("{0} => {1}".format(i, str(cache[i])))
    maxnum = (input("I will choose a number between 1 and "))
    attempts = 0
    guess = ""
    while guess != 0:
        ok_guess = 0
        if attempts == 0:
            ok_max = 0
            while ok_max == 0:
                try:
                    maxnum = int(maxnum)
                except:
                    print("It must be a number! Try again.")
                    maxnum = input("I will choose a number between 1 and ")
                    continue
                else:
                    if maxnum > 0:
                        ok_max = 1
                    else:
                        print("It can't be zero! Try again.")
                        maxnum = input("I will choose a number between 1 and ")
                        continue
            answer = random.randint(1, maxnum)
            print("I'm thinking of a number between 1 and {0}. Can you guess it?".format(maxnum))
        attempts += 1
        guess = input("Guess a number: ")
        while ok_guess == 0:
            try:
                guess = int(guess)
            except:
                print("It must be a number! Try again!\nTo give up enter '0'.")
                guess = input("Guess a number: ")
            else:
                ok_guess = 1
        if guess > answer:
            print("Too high! Guess lower! Try again.")
            continue
        elif guess < answer and guess != 0:
            print("Too low! Guess higher! Try again.")
            continue
        elif guess == 0:
            print("Thank you for playing!")
            continue
        elif guess == answer:
            print("Congratulations!! You win with {0} attempts!! \o/ ".format(str(attempts)))
            name = input("Leave your name on the Hall of Fame: ")
            try:
                cache[str(maxnum)].update({name:"{0}".format(str(attempts))})
            except KeyError:
                cache[str(maxnum)] = {name:"{0}".format(str(attempts))}
            if len(cache[str(maxnum)]) >= 5:
                x = 0
                y = 0
                for n in cache[str(maxnum)]:
                    if x == 0 or cache[str(maxnum)][n] >= x:
                        x = cache[str(maxnum)][n]
                        y = n
                if x != 0:
                    cache[str(maxnum)].pop(y)
            with open("top5", "wb") as top5:
                pickle.dump(cache, top5)
            attempts = 0

numguess()

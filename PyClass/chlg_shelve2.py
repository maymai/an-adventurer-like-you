"""
Load data from shelve file to run the aventure game.
 """
import shelve

areas = shelve.open("areas")
movements = shelve.open("movements")
history = ["room"]
current = "room"
print(areas[current]["description"][0])
while True:
    current_movements = areas[current]["exits"].keys()
    area_exits = ", ".join(current_movements)
    direction = input("What do you do? ").lower()
    print("--------------------------------------------------\n" + direction.capitalize())
    if "quit" in direction.lower():
        print("Thank you for playing.")
        break
    word_check = 0
    for word in direction.split():
        if word == "help" or direction == "":
            word_check = 1
            print("You may go {0}. To quit, enter 'quit'.".format(area_exits))
        elif word in movements:
            word_check = 1
            new_current = areas[current]["exits"].get(movements[word])
            if new_current:
                current = new_current
                history.append(current)
                if history.count(current) > (len(areas[current]["description"]) - 1):
                    sit = len(areas[current]["description"]) - 1
                else:
                    sit = history.count(current) - 1
                print(areas[current]["description"][sit])
            else:
                print("You can't do that. You can go {0}.".format(area_exits))
    if word_check == 0:
        print("Sorry, you can't do that. You can go {0}.".format(area_exits))
areas.close()
movements.close()

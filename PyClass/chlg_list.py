"""
Monty Python's Spam ske:
Create a menu and enquire for an item without spam.
If the item has spam, ask if it's possible to have it without spam.
"""
menu = [["egg", "spam", "bacon"], ["egg", "spam"], ["egg", "bacon", "spam"], \
            ["egg", "bacon", "sausage", "spam"], ["spam", "bacon", "sausage", "spam"], ["spam", "egg", "spam", "spam", "bacon", "spam"],\
            ["egg", "sausage", "bacon"], ["spam", "egg", "sausage", "spam"]]
print("Today's Menu:")
for item in menu:
    food = "//"
    for i in item[:-1]:
        food += i.capitalize() + ", "
    food = food.rstrip(", ")
    food += " and {0}//".format(item[-1].capitalize())
    print(food)
print("-" * 20)
for item in menu:
    if "spam" not in item:
        total = len(item)
        good_food = ""
        for i in item:
            if item.index(i) == len(item) - 1:
                good_food = good_food.rstrip(", ")
                good_food += " and {0}, please.".format(i)
            else:
                good_food += i + ", "
        print("I would like some " + good_food)
        break
    else:
        count = 0
        not_spam = []
        for food in item:
            if "spam" in food:
                count += 1
            else:
                not_spam.append(food)
        good_food = ""
        spam = ""
        for i in not_spam:
            if len(not_spam) == 1:
                good_food = i
                break
            elif not_spam.index(i) == len(not_spam) - 1:
                good_food = good_food.rstrip(", ")
                good_food += " and {0}".format(i)
            else:
                good_food += i + ", "
        if count > 1:
            spam = "spam, " * (count - 1)
            spam += "and spam"
        elif count == 1:
            spam = "spam"
        print("Could I have {0} without {1}?".format(good_food, spam))
        print("Eww! No, you couldn't!")

"""
Do a for loop using iter() instead
"""
phrase = input("Please enter a sentence:")
items = phrase.split()
it_items = iter(items)
for n in range(len(items)):
    print(next(it_items))
 

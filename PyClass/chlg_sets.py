"""
Return non-vowel character from a string in alphabetical order.
"""
vowelset = frozenset("aiueo")
consonantset = frozenset("bcdfghjklmnpqrstvwxyz")
message = (input("Please enter a message: ")).lower()
voweless_message = set(message).difference(vowelset).intersection(consonantset)
print(sorted(voweless_message))

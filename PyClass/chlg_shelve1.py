"""
Create a shelve file for the adventure game.
"""
import shelve

areas = shelve.open("areas")
areas["room"] = {"description": ["You are in a messy, badly lit room. \nThe only source of light is a computer blinking on a command line and a door. \nThere is another door in the room, closed.", "You are back in the bedroom."], "exits": {"west": "bathroom", "south": "living room"}}
areas["bathroom"] = {"description": ["It stinks in here. You can identify a toilet and what looks like a bathtub. \nThe bathtub is filled with dirty clothes.", "You are back in the bathroom."], "exits": {"east": "room"}}
areas["living room"] = {"description": ["This room is nicer than the rest. Light comes in through bare windows on the walls south and east. \nAn old couch sits in the middle of the otherwise empty room.", "You are back in the living room."], "exits": {"north": "room", "west": "kitchen", "south": "street"}}
areas["kitchen"] = {"description": ["You find yourself in a kitchen. No dishes and no food on sight. \nIt looks like the fridge has been turned off for some time.", "You are back in the kitchen."], "exits": {"east": "living room"}}
areas["street"] = {"description": ["You leave the house into the street. The door locks behind you. \nCars are parked on the pavement, others on garages. \nNo person in sight.", "You are back on the street."], "exits": {"east": "forest", "west": "mountains", "south": "beach"}}
areas["forest"] = {"description": ["You take one of the cars and follow the road east. \
                                                     \nSoon the trees you could see every mile or so becomes more regular, until they turn into a forest. \
                                                     \nThe paved road ends and becomes a dirt trail. The forest becomes denser with every mile. \
                                                     \nYou are thinking of turning back, but then the car makes a noise and starts to lose speed. \
                                                     \nSmoke fills the air, the car refuses to turn back on.", "You are back at the forest."], "exits": {"south": "beach"}}
areas["mountains"] = {"description": ["You take one of the cars and follow the road uphill. \nHigh pine trees are everywhere. The car starts making noises and loses speed. \nYou are out of petrol.", "You are back at the mountains."], "exits": {"south": "beach"}}
areas["beach"] = {"description": ["After walking for what seems to be an eternity, you start hearing a pleasant sound of waves. \
                                                     \nThe sea spreads in front of you. You take off your shoes and feel the soft, warm sand under your feet. \
                                                     \nA few cars seems to be parked at the coast.", "You are back on the beach."], "exits": {"east": "forest", "west": "mountains", "north": "street"}}
areas.close()
movements = shelve.open("movements")
movements["west"] = "west"
movements["east"] = "east"
movements["south"] = "south"
movements["north"] = "north"
movements["w"] = "west"
movements["e"] = "east"
movements["s"] = "south"
movements["n"] = "north"
movements.close()

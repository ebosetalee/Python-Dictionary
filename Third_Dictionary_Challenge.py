# This involves nesting dictionaries.
# This is another way in which the previous game can be organised. YOUR MISSION (If you choose to accept it):
# Change the code to make it work.
# Below is the complete program, but with the locations dictionary modified so that everything is in a single dictionary.
# N.B: The code has some errors, thats what you need to fix!!!
# You'll be changing just 4 lines of code. 

locations = {
  0: {"desc": "You are sitting in front of a computer learning Python",
      "exits": {},
      "namedExits":{}},
  1: {"desc": "You are standing at the end of a ROAD before a small brick building",
      "exits": {"W": 2, "E" : 3, "N" : 5, "S" : 4, "Q" : 0},
      "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
  2: {"desc": "You are at the top of a HILL",
      "exits": {"N": 5, "Q" : 0},
      "namedExits": {"5": 5}},
  3: {"desc": "You are inside a BUILDING, a well house for a small stream",
      "exits": {"W": 1, "Q" : 0},
      "namedExits": {"1": 1}},
  4: {"desc": "You are in a VALLEY beside a stream",
      "exits": {"N": 1, "W" : 2, "Q" : 0},
      "namedExits": {"1": 1, "2": 2}},
  5: {"desc": "You are in a FOREST",
      "exits": {"W": 2, "S" : 1, "Q" : 0},
      "namedExits": {"2": 2, "1": 1}}
}
vocabulary = {
  "QUIT": "Q",
  "NORTH": "N",
  "SOUTH": "S",
  "EAST": "E",
  "WEST": "W",
  "ROAD": "1",
  "HILL": "2",
  "BUILDING": "3",
  "VALLEY": "4",
  "FOREST": "5"} 

loc = 1
while True:
  availableExits = ", ".join(locations[loc]["exits"].keys())
  print(locations[loc]["desc"])
#   print(list(locations[loc]["exits"].keys())) # For checking purposes. 

  

  if loc == 0:
    break 
  else:
      allExits =locations[loc]["exits"].copy()
      allExits.update(locations[loc]["namedExits"])
    # exits[loc].update(namedExits) #using only this will cause an issue as .join in line 42 requires a string not int.

  direction = input("Available exits are "+ availableExits + " choose one only please  ").upper() 
  print()
  if len(direction) > 1: 
      words = direction.split()
      for word in words:
          if word in vocabulary:
              direction = vocabulary[word]

  if direction in allExits: # we changed from exits[loc] to allExits
    loc = allExits[direction] 
  else:
    print("You cannot go in that direction")
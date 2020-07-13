# Coming from Dictionary_game, we are with our original exits, so we'd add a new dictionary which is a dictionary of dictionaries 
# that contains those numbers we removed.
locations = {
  0: "You are sitting in front of a computer learning Python",
  1: "You are standing at the end of a ROAD before a small brick building",
  2: "You are at the top of a HILL",
  3: "You are inside a BUILDING, a well house for a small stream",
  4: "You are in a VALLEY beside a stream",
  5: "You are in a FOREST"}

exits = {
  0: {"Q": 0},
  1: {"W": 2, "E" : 3, "N" : 5, "S" : 4, "Q" : 0},
  2: {"N": 5, "Q" : 0},
  3: {"W": 1, "Q" : 0},
  4: {"N": 1, "W" : 2, "Q" : 0},
  5: {"W": 2, "S" : 1, "Q" : 0}}

namedExits = {
    1: {"2": 2, "3": 3, "5": 5, "4": 4},
    2: {"5": 5},
    3: {"1": 1},
    4: {"1": 1, "2": 2},
    5: {"2": 2, "1": 1}}
# We'll create a combined directory by taking a copy of the location's exits dictionary and updating it to include the appropraite
# named exits. However, this will be useless if the player quits, thus we'll add an else to loacte quit i.e location 0 

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
  availableExits = ", ".join(exits[loc].keys())
  
  print(locations[loc])

  if loc == 0:
    break 
  else:
      allExits = exits[loc].copy()
      allExits.update(namedExits[loc])
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
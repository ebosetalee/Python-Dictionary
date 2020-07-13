# We are changing the user interface of this game; the players can enter the name of the location instead of the direction.
# Thus, we'll extend the vocabulary to include the location names such as hill etc 
locations = {
  0: "You are sitting in front of a computer learning Python",
  1: "You are standing at the end of a ROAD before a small brick building",
  2: "You are at the top of a HILL",
  3: "You are inside a BUILDING, a well house for a small stream",
  4: "You are in a VALLEY beside a stream",
  5: "You are in a FOREST"}

exits = {
  0: {"Q": 0},
  1: {"W": 2, "2": 2, "E" : 3, "3": 3, "N" : 5, "5": 5, "S" : 4, "4": 4, "Q" : 0},
  2: {"N": 5, "5": 5, "Q" : 0},
  3: {"W": 1, "1": 1, "Q" : 0},
  4: {"N": 1, "1": 1, "W": 2, "2": 2, "Q" : 0},
  5: {"W": 2, "2": 2, "S": 1, "1": 1, "Q" : 0}}

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
# We can't used the direction as the value, thus to use the location value and we'll need to update the exits dictionary.
# the issue is numbers get to show when printing the available exits; Thus, we need to store the named destination in a seperate
# dictionary and combine them at the point we check the players input.


loc = 1
while True:
  availableExits = ", ".join(exits[loc].keys())
  
  print(locations[loc])

  if loc == 0:
    break 
  
  direction = input("Available exits are "+ availableExits + " choose one only please  ").upper() 
  # Parse the user input, using our vocabulary dictionary if necessary i.e the input is greater than 1
  if len(direction) > 1: # more than one letter, so check vocabulary
      words = direction.split()
      for word in words:
          if word in vocabulary:
              direction = vocabulary[word]

  if direction in exits[loc]:
    loc = exits[loc][direction] 
  else:
    print("You cannot go in that direction")
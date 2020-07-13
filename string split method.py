# A Split command will seperate a string into a list containing all the parts of the string, these parts are seperated by the deliminiter
# of our choice which will be a space. If a deliminiter isn't used the default will be space. However, commas, colon etc can be used.
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

vocabulary = {
  "QUIT": "Q",
  "NORTH": "N",
  "SOUTH": "S",
  "EAST": "E",
  "WEST": "W"} 

# print(locations[0].split()) # this separates it into a list containing the number of words 
# print(locations[3].split(",")) # this gives a list containing two items because it splits based on the comma deliminiter
# print(" ".join(locations[0].split())) # this splits the texts and spaces; and then join to cancatenate the string with spaces so back to the original string.
# This shows how split works

# With split method, we can rewrite the program to work the correct way around, so we can check the players input against the 
# vocabulary instead of checking the vocabulary against the input as seen in Dictionary challenge 1.

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
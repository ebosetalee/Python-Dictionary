# Modify the program so that exits are a dictionary rather than a list,
# with the keys being the number of the locations and the values being dictionaries holding the exits (as they do at present).
# No change should be needed to the actual code
# Once it is working, create another dictionary that contains words that players may use. These words will be the keys,
# and their values will be a single letter that the program can use to determine which way to go. 

# locations = {
#   0: "You are sitting in front of a computer learning Python",
#   1: "You are standing at the end of a ROAD before a small brick building",
#   2: "You are at the top of a HILL",
#   3: "You are inside a BUILDING, a well house for a small stream",
#   4: "You are in a VALLEY beside a stream",
#   5: "You are in a FOREST"}

# exits = [
#   {"Q": 0},
#   {"W": 2, "E" : 3, "N" : 5, "S" : 4, "Q" : 0},
#   {"N": 5, "Q" : 0},
#   {"W": 1, "Q" : 0},
#   {"N": 1, "W" : 2, "Q" : 0},
#   {"W": 2, "S" : 1, "Q" : 0}]

# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#     print(locations[loc])

#   if loc == 0:
#     break 

#   direction = input("Available exits are "+ availableExits + " ").upper() 
#   print()
#   if direction in exits[loc]:
#     loc = exits[loc][direction] 
#   else:
#     print("You cannot go in that direction")

# SOLUTION
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
  5: {"W": 2, "S" : 1, "Q" : 0}} # this is the first part of the question; converted from list to dictionary.

# For the second part of the question:
# For the players to type more thn one word, we need a list of words which the game uses
# in order for the words to be typed to have meaning in the game. check Dictionary_game2


vocabulary = {
  "QUIT": "Q",
  "NORTH": "N",
  "SOUTH": "S",
  "EAST": "E",
  "WEST": "W"} # we've assigned the variable to the dictionary in vocabulary

loc = 1
while True:
  availableExits = ", ".join(exits[loc].keys())
  
  print(locations[loc])

  if loc == 0:
    break 
  
  direction = input("Available exits are "+ availableExits + "choose one only please  ").upper() 
  print()
  # Parse the user input, using our vocabulary dictionary if necessary i.e the input is greater than 1
  if len(direction) > 1: # more than one letter, so check vocabulary
    for word in vocabulary: #does it contain a word we know?
      if word in direction:
        direction = vocabulary[word]

  if direction in exits[loc]:
    loc = exits[loc][direction] 
  else:
    print("You cannot go in that direction")

# this is a fairly flexible way for players to specify which direction they want to go.
# a list is better because a dictionary of dictonaries may look confusing until you understand the concept.
# This way of iterting through to find a word that is in the vocabulary isnt efficient a better way is to check each word that the 
# player has typed to see if it is in the vocabulary. This can be done by breaking out the input that the player type to individual
# sequence of characters seperated by spaces. This is done by SPLIT which is the opposite of Join.\
# A Split command will seperate a string into a list containing all the parts of the string that are seperated by the deliminiter
# of our choice which will be a space
# check file string split method.

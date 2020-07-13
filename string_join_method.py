# Another string method is Join and string is immutable: this means is not all efficient to cancatenate string in a loop.
# Every time you cancatenate a string to an existing string, a new string has to be created and if its done in a loop it is expensive and slow.
# The String join method is there to help which takes a sequence and produce a new string from it and seperated from the string the join was called upon

myList = ["a", "b","c","d"]

newString = ""
# for c in myList:
#   newString += c + ", "
#   print(newString)
# this is inefficient as it ends with a comma. 
# Then, the use of Augumented Assignment (used to update the variable in place where possible) isn't gonna help because strings 
# are immutable then the use of join instead; seen below:
newString = ", ".join(myList) + "."
print(newString) # added the fullstop for experiment.

print("-" * 40)
# Another example in which any sequence type can be used insted of a list 
# we can parse another string.
letters = "abcdefghijklmnopqrstuvwxyz"
# newStrings = "" #this is not necessary but can be used if intending to make a loop

newStrings = ", ".join(letters) + "."
print(newStrings)

numbers = "1234567890"
newsstring =" mississippi ".join(numbers) # you can also make it in a loop and still get the exact thing
print(newsstring)

# to cancatenate the keys of a dictionary to give a string. As seen below:
# we'll use dictionaries to store locations in a basic adventure game and store the value exits in 
# another and link the two together, so the players can move from one location to another.
locations = {
  0: "You are sitting in front of a computer learning Python",
  1: "You are standing at the end of a ROAD before a small brick building",
  2: "You are at the top of a HILL",
  3: "You are inside a BUILDING, a well house for a small stream",
  4: "You are in a VALLEY beside a stream",
  5: "You are in a FOREST"}
# we need to represent the value exits for each location (5 possible exits: North, south, east and 
# west plus quit to exit the game.) Thus, the directions are the key and the values are the location we end up

# Next dictionary is the exits
exits = [
  {"Q": 0},
  {"W": 2, "E" : 3, "N" : 5, "S" : 4, "Q" : 0},
  {"N": 5, "Q" : 0},
  {"W": 1, "Q" : 0},
  {"N": 1, "W" : 2, "Q" : 0},
  {"W": 2, "S" : 1, "Q" : 0}]
# the exits is represented with a list of dictionary objects which contains one dictionary for each location 
# It is done this way so we can index it. However, this isn't the best representation for the exits, for example
# we can use a dictionary with the key being the location number and the exits being in tuple or another dictionary: check Dictionary Challenge1

# A loop should allow the player to keep entering directions until it choses to quit and each time
# we enter the loop it should display direcions and possible exits 
loc = 1
while True:
  availableExits = "" # these 3 lines can be changed due to cancatenating a string to a loop
  for direction in exits[loc].keys():
    availableExits += direction + ", "
  # availableExits = ", ".join(exits[loc].keys()) # this is better and removes the comma at the end unfortunately doesn't add space but seen below
  print(locations[loc])

  if loc == 0:
    break # the program will keep looping until the location is 0 and the game ends

  direction = input("Available exits are "+ availableExits + " ").upper() # direction is used instead of exist because python will read exit as quit and end the game
  print()
  if direction in exits[loc]:# when a direction is chosen we check if the key exists in the appropriate dictionary from list of exits
    loc = exits[loc][direction] # then we use the key to retrieve the next location if it does exists. 
    #This is used as an index into the exits list to retrieve the dictionary containing the available exits for that location
  else:
    print("You cannot go in that direction")
# if .get is used, we have to check the values before we can retrieve the next direction
# there is a slight problem in this operation because of the reliance on the order of the keys and if there's alot location
# it could get tedious to place each in the direct order or number 
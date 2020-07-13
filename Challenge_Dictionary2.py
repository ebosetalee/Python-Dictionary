# Update method - allows to combine 2 dictionaries and
# Copy method - to create a copy of the dictionary.

fruit = {"orange": "a sweet, orange, citrus fruit",
  "apple": "Good for making Cider", 
  "lemon": "A sour, yellow citrus fruit",
  "grape": "A small, sweet fruit growing in bunches", 
  "lime": "A sour, green citrus fruit"}
print(fruit)

veg = {"cabbage": "Every child's favorite",
       "sprouts": "mmmmmm, lovely",
       "spinach": "can I have some fruit, please"}
print(veg)

# veg.update(fruit) #adding the fruit dictionary to the veg dictionary 
# #note: It doesn't return a new dictionary nor new object
# print(veg)
# print(fruit.update(veg)) # when this is added, line 16 will give us none to emphasise that it doesn't create a new dictionary

# To create a new dictionary wthout modifying the other one, the better option is copy method.
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
# this can be useful in our game 
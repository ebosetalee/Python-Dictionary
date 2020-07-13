# An unordered collection of data that doesnt contain duplicates.
# Unlike a dictionary, items aren't accessed via a key. It must have immutable objects.
# A set in pythen 2.6 is different from python 3 using curly brackets.

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals) #This is similar to dictionaries

for animal in farm_animals:
    print(animal)

print("-" * 40)

wild_animals = set(["lion", "tiger", "hare", "panther", "elephant"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# we can have a sorted sets using sorted()
print(sorted(wild_animals))
# The difference method can also be used using - or .difference
# Theres also the .difference_update method  which doesn't return a new set.
even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even-squares))

print("-" * 40)

print("Squares minus Even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

# print(squares.difference(even)) # this shows in curly braces
# print(squares - even)

print("-" * 40) # how .difference_update works
even.difference_update(squares)
print(sorted(even))

#symmetric difference (opposite of intersection) and .symmetric_difference_update 

# discard and remove
squares.discard(4)
squares.remove(16)
squares.discard(8) # No error does nothing
print(squares)
# If we try something to show why remove is used other than discard:
try:
    squares.remove(8)
except KeyError:
    print("The Item 8 is not a member of the set")

# .issubset and .issuperset i.e a set in another or vice versa respectively.
if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("Even is a superset of squares")
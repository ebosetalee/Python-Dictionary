# Set object is an unordered collection of distinct hashable objects; every element is unique(no duplicates).
# An object is hashable if it has a hash value which never changes during its lifetime and can be compared 
# to other objects. Hashability makes an object usuable as a dictionary key and set member.
# common uses of set include membership testing, removing duplicates from a sequence, and computing mathematical
# operations such as intersection, union, difference, and symmtric difference. 
# set supports x in set, len(set), and for x in set but not indexing, slicing, or other sequence like behaviour
# Two built in set typres: set and frozenset and sets are mutable.
# in set, you can change it by add() or update() and remove() or discard(). 
# Thus not hashable unlike frozenset which cannot be changed.
# sets() or by {}, and frozenset([,]) are created this way.
mySets = {1.0, 2,'Hello',2.0, 3, 4.0}
print(mySets)
#  
a = set([1,1,2,3,5,8,13])
# set(a)
print(a)
# Note a set cannot have a mutable element like list, set, or dictionary but can have a tuple, string, int, float
b = tuple(a)
sans = set(b)
print(sans)
# we can make a set from a list
c = set([1,2,3,2])
print(c)
# to create an empty set use set() not {} as it creates a dict.
d = set()
# check the data type of d 
print(type(d)) # oh wow this is used to print data type: <class 'data type'>
# The update method can take tuples, list, strings or other sets as its arguement.
# Note that duplicates are avoided in sets, indexing e.g c[0] or c[0:1]
# .add() or .update()
d.add(2)
print(d)
d.update([3,4],[1,9],{6,7,8})
# int isn't iterable so without putting 3,4 in [] 0r {} its ouput is error
print(d)
# .discard()in using this, if the element isnt in the set, it remains unchanged; or .remove() but using this
# will raise a error in such condition.
d.discard(2)
print(d)
# d.remove(2)
# print(d) # error cause 2 is no longer in d
d.discard(2)
print(d)
# we can remove and return a random element from a set using .pop()
# we can clear the set using .clear()
e = set("Hello beautiful World")
print(e.pop())
print(e.clear())
# to remove a value instead of returning like pop will, use .del()
# del e("W") #it works only on lists and since a set cannot be a list, theres error cause it requires indexing

# As stated earlier, set can used to carry out maths operations:
# Union is a joint set of all elemets from two sets e.g f,g and is performed using | symbol or .union()
f = {1,2,3,4,5,6}
g = {4,5,6,7,8,9}
print(f|g) # or
print(f.union(g)) # or
print(g.union(f))
# Intersection of f and g is a set of elements that are common in both sets; using & symbol or .intersection()
print(f & g)
print(f.intersection(g))
# difference of f and g(f-g) is set of elements that are only in f and not in g,(g - f) vice versa; using - 
# symbol or .differene().
print(f - g)
print(f.difference(g)) 
print(g - f)
print(g.difference(f))
# symmetric difference of f and g is the elements found in f and g except those common in them; using ^ symbol
# or .symmetric_difference().
print(f ^ g)
print(f.symmetric_difference(g)) 

# DIFFERENT PYTHON SEET METODS
# .copy(); returns a copy of the set NOTE: copy takes no arguments
# .difference_update(); removes all elements of another set from this set
# .intersection_update(); updates itself with the intersection of itself and another
# .isdisjoint(); returns TRUE if two sets have a null intersection
# .issubset(); return TRUE if another set contains this set
# .issuperset(); return TRUE if this set contains another set 
# .symmetric_difference_update(); updates the set with the symmetric difference of itself and another
# .update(); updates itself with the union of itself and another 

# SET MEMBERSHIP TEST
# We can test if an item is in a set or not, using the word "in" or "not in
my_set = set("apple")
print('a' in my_set) # output true cause a is there
print('p' not in my_set) # output false cause p is in the set

# Iterate through a set: Using a for loop
for letter in my_set:
    print(letter)
# Built in functions with set: all(), any(), enumerate(), len(), min(), max(), sorted(), sum().
# all(): return TRUE if all elements of the set are true(or if the set is empty).
# any(): return TRUE if any element of the set is true. if the set is empty, FALSE.
# enumerate(): return an enumerate object. it contains the index and value of all the items of set as a pair.
# sorted(): return a new sorted list from elements in the set(does not sort the set itself).
# sum(): return the sum of all elements in the set

# FROZENSET:
# It has the same characteristics of a set, but its elements cannot be changed once assigned; and are immutable
# created using frozenset().
# frozenset supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(),
# symmetric_difference() and Union. BUT NOT add() or remove().  
#!runscript

# Let's print our starburst flavors!
flavors = ["cherry", "orange", "strawberry", "lemon", "apple"]

for flavor in flavors:
    print(flavor + " is a starburst flavor.")

######################
# 99 Bottles of Beer #
######################

# Using a for loop like we just did to print starburst flavors, we're going to
# print the full lyrics to 99 Bottles of Beer.

# First, we'll need to create our list of numbers, like we did with our list of
# flavors. Rather than writing out all the numbers, we'll assemble the list with
# a while loop:

# create a list of numbers:
x = 9
bottles = []
while x > 0:
    bottles.append(x)
    x -= 1

# print the lyrics to 99 bottles of beer:
for bottle in bottles:
    print(str(bottle) + " bottles of beer on the wall,")
    print(str(bottle) + " bottles of beer,")
    print("take one down, pass it around,")
    print(str(bottle-1) + " bottles of beer on the wall!")

# Can we do this with a while loop?
bottle = 9
while bottle > 0:
    print(str(bottle) + " bottles of beer on the wall,")
    print(str(bottle) + " bottles of beer,")
    print("take one down, pass it around,")
    bottle -= 1
    print(str(bottle) + " bottles of beer on the wall!")

# Let's put that in a function!

def bottles_lyrics():
    bottle = 9
    while bottle > 0:
        print(str(bottle) + " bottles of beer on the wall,")
        print(str(bottle) + " bottles of beer,")
        print("take one down, pass it around,")
        bottle -= 1
        print(str(bottle) + " bottles of beer on the wall!")
    return None

# Functions are a way of putting code in boxes for easy re-use. Because they're
# meant to be used over and over, they don't run until they're *called*. You
# call a function like this:

bottles_lyrics()

# What really makes functions powerful, however, is being able to run different
# objects through them. We do this by *passing in* objects. The function then
# acts on those objects and *returns* a result. Let's rewrite bottles_lyrics()
# so that it takes the number of bottles as an argument:

def bottles_lyrics2(bottle):
    # because we're 'passing in' bottlecount as an argument,
    # we no longer need to define it inside the function.

    while bottle > 0:
        print(str(bottle) + " bottles of beer on the wall,")
        print(str(bottle) + " bottles of beer,")
        print("take one down, pass it around,")
        bottle -= 1
        print(str(bottle) + " bottles of beer on the wall!")
    return None

# We call the function with the argument like this:
bottles_lyrics2(99)

# Let's add a default value!

def bottles_lyrics3(bottle = 99):
    # now, if someone doesn't include a number when they call the function,
    # the function will assume they want 99 bottles.

    while bottle > 0:
        print(str(bottle) + " bottles of beer on the wall,")
        print(str(bottle) + " bottles of beer,")
        print("take one down, pass it around,")
        bottle -= 1
        print(str(bottle) + " bottles of beer on the wall!")
    return None

# Including a default value makes an argument *optional*.

# Shortcut: the range function:
bottles = range(99, 0, -1)
# The range funtion creates the list of numbers for us. It takes 3 arguments:
# The number to start counting at, the number to stop counting at, and the
# interval--how far to jump between numbers in the range. We want to start at
# bottlecount, end at 0, and include every number in between. (so our interval
# is -1). This brings us back to the for loop:

def bottles_lyrics4(bottlecount = 99):
    for bottle in range(bottlecount, 0, -1):
        print(str(bottle) + " bottles of beer on the wall,")
        print(str(bottle) + " bottles of beer,")
        print("take one down, pass it around,")
        print(str(bottle-1) + " bottles of beer on the wall!")
    return None

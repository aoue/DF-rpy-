

init python:

    class dungeon():
        def __init__(self):
            #make the dungeon crawler interface (just images of interconnecting rooms, where each room is an image button and it shows up if you've explored it, and is clickable if you're adjacent. use a 2d array for this too.)

            self.threat = 0 #the longer you're in a dungeon, the higher the threat. the higher the threat, the stronger the monsters and the better the loot.

            #big grid, similar to the map, where the item in the grid correspond to some kind of room. e.g.:
            #0: no room
            #1: single passeway
            #2: dead end room
            #3: room with three exits
            #etc.
            #^we could do it this way, i'm just not sure how could it is.

            self.map = [
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 3, 5, 2, 1],
                [0, 0, 1, 1, 4]
            ]

            #^here's an example. not too hard to read. for random generation, all we need is a function to generate an int, keeping in mind some things so we don't hit the gold all the time/find all dead ends. no problem.

            #if we don't want to scroll:
            # -just set up the map so an entire floor fits on one screen. if we want to go beyond that, we can add more floors.
            # +this also lets the player know what direction to go in, etc.

            #when generating rooms, we just keep track of a maximum y and x so we don't go off the edge. in the room generation function, if we're about to go off the edge, then the room must be a dead end. kind of cool.


    class room():
        def __init__(self):
            self.bg = "" #image background for vn portion stuff that happen in here.
            self.type = 0 #what the shape of the room is.
            self.doors = 0 #how many entrances/exits the room has.
            self.loot = 0 #int corresponding to an item.



        def generate(self):
            #generates a new room. takes some imput:
            # -current unexplored hallways (to avoid dead ends)
            # -
            pass

        def rest(self):
            #what happens when the player decides to rest here
            pass

        def encounter(self):
            #generate an encounter for the room.
            pass

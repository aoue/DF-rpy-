
#rooms are inside dungeons
init python:
    class room():
        def __init__(self, x, y, (a,b,c,d)):
            self.bg = "" #image background for vn portion stuff that happen in here. or as a battle background?
            self.explored = 0 #0: unexplored. 1: explored
            self.x = x #room's  x coordinate in the larger map
            self.y = y #room's y coordinate in the larger map
            self.connect = (a,b,c,d) #four tuple. represents hallways. clockwise from 12 o'clock.
            self.dis_x = 150 * (x+1) #x display position for the room
            self.dis_y = 90 * (y+1) #y display position for the room
            self.descr = "Room {}, {}".format(x, y) #description
            self.rounds = -1 #how many rounds a fight in here will last.
            self.dc = 2 #how many units can be deployed in this room's fight.

            self.fight = 1 #0: no fighting. 1: yes fighting.

            self.doors = 0 #how many entrances/exits the room has.
            self.loot = 0 #int corresponding to a table with a chance for certain items, whatever.

        #getters
        def get_explored(self):
            return self.explored
        def get_x(self):
            return self.x
        def get_y(self):
            return self.y
        def get_dis_x(self):
            return self.dis_x
        def get_dis_y(self):
            return self.dis_y
        def get_descr(self):
            return self.descr
        def get_rounds(self):
            return self.rounds
        def get_dc(self):
            return self.dc
        def get_fight(self):
            return self.fight
        def get_connect(self):
            return self.connect
        #setters
        def set_explored(self, x):
            self.explored = x
        def set_type(self, x):
            self.type = x

        #useful
        def get_baddies(self, dungeon):
            #needs dungeon to get threat level
            baddie1 = unit_jowler(0, "jowler", (0, 3), 1)
            
            enemylist = [baddie1]#, baddie2]
            return enemylist
        def do_event(self, dungeon):
            #does an event. text stuff.
            #jump to a label.
            pass
            #renpy.call("room", dungeon)

    class event_room(room):
        def __init__(self, x, y, (a,b,c,d)):
            self.bg = "" #image background for vn portion stuff that happen in here. or as a battle background?
            self.explored = 0 #0: unexplored. 1: explored
            self.x = x #room's  x coordinate in the larger map
            self.y = y #room's y coordinate in the larger map
            self.connect = (a,b,c,d) #four tuple. represents hallways. clockwise from 12 o'clock.
            self.dis_x = 150 * (x+1) #x display position for the room
            self.dis_y = 90 * (y+1) #y display position for the room
            self.descr = "Room {}, {}".format(x, y) #description
            self.rounds = 0 #how many rounds a fight in here will last.
            self.dc = 0 #how many units can be deployed in this room's fight.
            self.fight = 0 #0:no fighting. 1:yes fighting.
            self.doors = 0 #how many entrances/exits the room has.
            self.loot = 0 #int corresponding to a table with a chance for certain items, whatever.

        def get_baddies(self, dungeon):
            pass
        def do_event(self, dungeon):
            #does an event. text stuff.
            #jump to a label.

            renpy.call("room", dungeon)






























##eof

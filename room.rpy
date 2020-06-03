
#rooms are inside dungeons
init python:
    class Room():
        def __init__(self, x, y, (a,b,c,d)):
            self.bg = "" #image background for vn portion stuff that happen in here. or as a battle background?
            self.icon = "" #small image that shows on the dungeon map.
            self.explored = 0 #0: unexplored. 1: explored
            self.x = x #room's  x coordinate in the larger map
            self.y = y #room's y coordinate in the larger map
            self.connect = (a,b,c,d) #four tuple. represents hallways. clockwise from 12 o'clock.
            self.dis_x = 150 * (x+1) #x display position for the room
            self.dis_y = 90 * (y+1) #y display position for the room
            self.descr = "Room {}, {}".format(x, y) #description
            self.rounds = 0 #how many rounds a fight in here will last.
            self.dc = 0 #how many units can be deployed in this room's fight.
            self.fight = 0 #0: no fighting. 1: yes fighting.
            self.loot = 0 #int corresponding to a table with a chance for certain items, whatever.
            self.room_label = "room" #event that is called when walking into the room, yo.
            #room menu
            self.poi = 0 #point of interest. 1: yes, 0: no. it's a unique event.
            self.poi_label = "" #name of the label the poi button goes to.
            self.has_action = 1
            self.action_title = "room_action"

            self.is_exit = 0 #int. 0: is not an entrance, 1: is an entrance.

        #getters
        def get_is_exit(self):
            return self.is_exit
        def get_room_label(self):
            return self.room_label
        def get_icon(self):
            return self.icon
        def get_has_action(self):
            return self.has_action
        def get_action_title(self):
            return self.action_title
        def get_poi(self):
            return self.poi
        def get_poi_label(self):
            return self.poi_label
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
            #return list of enemy units
            pass
        def do_event(self, dungeon):
            #jump to a label.
            #renpy.call("room", dungeon)
            pass
        def room_action(self, dungeon):
            #repeatable events in the room. i.e. heal, exit.
            pass
        def poi_event(self, dungeon):
            pass

    # -- EVENT ROOMS -- ##
    class Exit_room(Room):
        #exits from the dungeon
        def __init__(self, x, y, (a,b,c,d)):
            self.bg = ""
            self.icon = "exit_icon"
            self.explored = 0
            self.x = x
            self.y = y
            self.connect = (a,b,c,d)
            self.dis_x = 150 * (x+1)
            self.dis_y = 90 * (y+1)
            self.descr = "Room {}, {}".format(x, y)
            self.rounds = 0
            self.dc = 0
            self.fight = 0
            self.loot = 0

            self.room_label = "room"
            self.poi = 0
            self.poi_label = ""
            self.has_action = 1
            self.action_title = "exit room"

            self.is_exit = 1

        def do_event(self, dungeon):
            renpy.call(self.get_room_label(), dungeon)
        def room_action(self, dungeon):
            #dungeon.exit_dungeon()
            pass

    class Fullheal_room(Room):
        #heals all units in the party to full health.
        def __init__(self, x, y, (a,b,c,d)):
            self.bg = ""
            self.icon = "fullheal_icon"
            self.explored = 0
            self.x = x
            self.y = y
            self.connect = (a,b,c,d)
            self.dis_x = 150 * (x+1)
            self.dis_y = 90 * (y+1)
            self.descr = "Room {}, {}".format(x, y)
            self.rounds = 0
            self.dc = 0
            self.fight = 0
            self.loot = 0
            self.is_exit = 0


            self.room_label = "room"
            self.poi = 0
            self.poi_label = ""
            self.has_action = 1
            self.action_title = "fullheal room"

        def do_event(self, dungeon):
            renpy.call(self.get_room_label(), dungeon)
        def room_action(self, dungeon):
            for unit in dungeon.get_party():
                unit.set_hp(unit.get_hpmax())
                unit.set_energy(unit.get_energymax())

    class Event_room(Room):
        def __init__(self, x, y, (a,b,c,d)):
            self.bg = ""
            self.icon = "event_icon"
            self.explored = 0
            self.x = x
            self.y = y
            self.connect = (a,b,c,d)
            self.dis_x = 150 * (x+1)
            self.dis_y = 90 * (y+1)
            self.descr = "Room {}, {}".format(x, y)
            self.rounds = 0
            self.dc = 0
            self.fight = 0
            self.loot = 0

            self.room_label = "room"
            self.poi = 0
            self.poi_label = ""
            self.has_action = 1
            self.action_title = "event room"
            self.is_exit = 0

        def do_event(self, dungeon):
            if self.get_explored() == 1:
                renpy.call(self.get_room_label(), dungeon)

    ## -- COMBAT ROOMS -- ##
    class Combat_room(Room):
        def __init__(self, x, y, (a,b,c,d)):
            self.bg = ""
            self.icon = "fight_icon"
            self.explored = 0
            self.x = x
            self.y = y
            self.connect = (a,b,c,d)
            self.dis_x = 150 * (x+1)
            self.dis_y = 90 * (y+1)
            self.descr = "Room {}, {}".format(x, y)
            self.rounds = -1
            self.dc = 2
            self.fight = 1
            self.loot = 0

            self.room_label = "room"
            self.poi = 0
            self.poi_label = ""
            self.has_action = 0
            self.is_exit = 0


        def get_baddies(self, dungeon):
            #needs dungeon to get threat level
            baddie1 = Unit_jowler(0, "jowler", (0, 3), 1)

            enemylist = [baddie1]
            return enemylist


































##eof

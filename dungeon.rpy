

init python:

#dungeons are for crawling

    class dungeon():
        def __init__(self, overworld):
            #make the dungeon crawler interface (just images of interconnecting rooms, where each room is an image button and it shows up if you've explored it, and is clickable if you're adjacent. use a 2d array for this too.)
            self.master = overworld #presides over the dungeon
            self.bg = "dungeon_bg" #""
            self.threat = 0 #the longer you're in a dungeon, the higher the threat. the higher the threat, the stronger the monsters and the better the loot.


            self.entrance = event_room(1,0,(0,1,1,0)) #where the entrance is. party starst here, exits here.
            self.entrance.set_explored(1)
            self.spot_x = self.entrance.get_x() #where the player's x is at
            self.spot_y = self.entrance.get_y() #where the player's y is at


            self.map = [
                [None, self.entrance, event_room(2,0,(0,0,1,1))],
                [room(0,1,(0,1,1,0)), room(1,1,(1,0,0,1)), room(2,1,(1,0,1,0))],
                [room(0,2,(1,1,0,0)), room(1,2,(0,1,1,1)), room(2,2,(1,0,1,1))],
                [None, room(1,3,(1,0,1,0)), room(2,3,(1,0,0,0))],
                [None, room(1,4,(1,0,1,0)), None],
                [None, room(1,5,(0,0,0,0)), None]
            ]

            self.party = [] #all the units player brought
            self.hold = [[],[],[]] #unit,x,y of ppl that were deployed last. x and y at the time they were deployed.

        #getters
        def get_master(self):
            return self.master
        def get_party(self):
            return self.party
        def get_hold(self):
            return self.hold
        def get_bg(self):
            return self.bg
        def get_threat(self):
            return self.threat
        def get_spot(self):
            return self.spot_x, self.spot_y
        def get_x(self):
            return self.spot_x
        def get_y(self):
            return self.spot_y
        def get_map(self):
            return self.map
        def get_entrance(self):
            return self.entrance

        #setters
        def set_party(self, party):
            self.party = party
        def set_x(self, x):
            self.spot_x = x
        def set_y(self, y):
            self.spot_y = y

        #useful functions
        def move_spot(self, x, y):
            self.set_x(x)
            self.set_y(y)
            self.find_room().set_explored(1)

            if self.find_room().get_fight() == 1:
                renpy.invoke_in_new_context(self.encounter, self.find_room())
            else:
                self.find_room().do_event(self)

        def find_room(self):
            #finds the room the party is in
            return self.get_map()[self.get_y()][self.get_x()]
        def remember_hold(self, nl):
            self.hold[0] = nl
            for x in range(0, len(self.hold[0])):
                self.hold[1].append(nl[x].get_point().get_x())
                self.hold[2].append(nl[x].get_point().get_y())
        def show_dungeon(self): #(self, floor)
            renpy.call_screen("dungeon_map", self, self.get_map(), self.get_spot())
        def encounter(self, room):
            #room.do_event(self)

            #if room.get_fight() == 1:
            el = room.get_baddies(self)
            #else:
                #self.move_spot(room.get_x(), room.get_y())
                #room.set_explored(1)
                #return

            allow_save = False
            allow_load = False

            deployer = deployment(room.get_dc(), self.get_party())
            if not self.get_hold()[0]:
                deployer.deploy()
                self.remember_hold(deployer.get_player())
            else:
                deployer.remember_deployment(self.get_hold()[0], self.get_hold()[1], self.get_hold()[2])
                self.remember_hold(deployer.get_player())

            battle_ins = battle(room.get_rounds(), deployer.get_player(), el, "battlefield0")
            battle_ins.combat_round()

            for unit in self.get_party():
                unit.post_battle()

            allow_save = True
            allow_load = True

            renpy.call("room", self)




#for calling a battle from nothing.











##eof

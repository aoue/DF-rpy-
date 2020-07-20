

init python:

#dungeons are for crawling.
#each dungeon needs its own class. the map of the dungeon and the monsterlist, etc, are all in the dungeon's init.

    class Dungeon(): #really, a dungeon should accept a few arguments.
        def __init__(self, master):
            self.master = master #overworld instance that called and presides over the dungeon.
            self.bg = "dungeon_bg" #image name

            self.entrance = Exit_room(1,0,(0,1,1,0)) #where the entrance is. party starts here, exits here.
            self.entrance.set_explored(1)
            self.spot_x = self.entrance.get_x() #where the player's x is at
            self.spot_y = self.entrance.get_y() #where the player's y is at

            self.monsterlist = [(0,0), (1,10), (2,3), (3,5)] #the threat necessary for the enemy to be faced in a random encounter
            self.threat = 1 #the longer you're in a dungeon, the higher the threat. the higher the threat, the stronger the monsters generated from random encounters.

            self.map = [
                [None, self.entrance, Fullheal_room(2,0,(0,0,1,1))],
                [Combat_room(0,1,(0,1,1,0)), Combat_room(1,1,(1,0,0,1)), Event_room(2,1,(1,0,1,0))],
                [Combat_room(0,2,(1,1,0,0)), Combat_room(1,2,(0,1,1,1)), Event_room(2,2,(1,0,1,1))],
                [None, Event_room(1,3,(1,0,1,0)), Event_room(2,3,(1,0,0,0))],
                [None, Event_room(1,4,(1,0,1,0)), None],
                [None, Event_room(1,5,(0,0,0,0)), None]
            ]

            self.party = [] #all the units player brought
            self.hold = [[],[],[]] #unit,x,y of ppl that were deployed last. x and y at the time they were deployed.

        #getters
        def get_monsterlist(self):
            return self.monsterlist
        def get_threat(self):
            return self.threat
        def get_master(self):
            return self.master
        def get_party(self):
            return self.party
        def get_hold(self):
            return self.hold
        def get_bg(self):
            return self.bg

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
        def set_threat(self, threat):
            self.threat = threat
        def set_party(self, party):
            self.party = party
        def set_x(self, x):
            self.spot_x = x
        def set_y(self, y):
            self.spot_y = y

        #useful functions
        def spawn_monster(self, type, dummymap):
            #type is the kind of monster that should be spawned. each dungeon will need its own.
            #below is an example from dungeon_0
            if type == 0: #jowler
                baddie = Unit_jowler(0, "jowler", dummymap.random_empty(), 1)

            elif type == 1: #groskel
                baddie = Unit_groskel(0, "groskel", dummymap.random_empty(), 0)

            elif type == 2: #spitter
                baddie = Unit_spitter(0, "spitter", dummymap.random_empty(), 1)

            elif type == 3: #frother
                baddie = Unit_frother(0, "frother", dummymap.random_empty(), 1)

            return baddie


        def exit_dungeon(self):
            #leaves dungeon. returns control to the overworld.
            self.get_master().set_in_dungeon(2)

            self.set_threat(1) #or something like this. reduce the threat in some way.

            #for every room,
            for i in range (0, len(self.get_map())):
                for room in self.get_map()[i]:
                    if room != None:
                        if room.get_charges() >= 0:
                            room.set_charges(min(room.get_charges() + 1, room.get_chargemax()))


            renpy.call("test_dungeon_entrance")

        def move_spot(self, x, y):
            self.set_x(x)
            self.set_y(y)

            if self.find_room().get_explored() == 0:
                self.find_room().set_explored(1)
                self.find_room().do_event(self)

                #self.find_room().do_event(self)
                #if self.find_room().get_fight() == 1:
                #    renpy.invoke_in_new_context(self.encounter, self.find_room())


        def find_room(self):
            #finds the room the party is in
            return self.get_map()[self.get_y()][self.get_x()]
        def remember_hold(self, nl):
            self.hold = [[],[],[]]
            for x in range(0, len(nl)):
                self.hold[0].append(nl[x])
                self.hold[1].append(nl[x].get_point().get_x())
                self.hold[2].append(nl[x].get_point().get_y())
        def show_dungeon(self): #(self, floor)
            renpy.hide_screen("dungeon_map")
            renpy.call_screen("dungeon_map", self, self.get_map())
            #renpy.hide_screen("dungeon_map")
        def encounter(self, room):
            el = room.get_baddies(self)

            allow_save = False
            allow_load = False

            deployer = Deployment(room.get_dc(), self.get_party())
            if not self.get_hold()[0]:
                deployer.deploy()
                self.remember_hold(deployer.get_player())
            else:
                deployer.remember_deployment(self.get_hold()[0], self.get_hold()[1], self.get_hold()[2])
                self.remember_hold(deployer.get_player())

            battle_ins = Battle(room.get_rounds(), self.get_party(), deployer.get_player(), el, "battlefield0", self.get_master().get_inventory())
            battle_ins.combat_round()

            self.set_threat(self.get_threat()+1) #idk what it should be really. should it be dependent on how fast you won the battle?

            #post battle. every unit in the party gets exp.
            #showlist = []
            #for unit in self.get_party():
            #    unit.post_battle()
            #    unit.get_foc().level_up(unit, battle_ins.get_total_exp(), showlist)
            #
            #    renpy.show_screen("level_up", showlist) #shows the level up screen

            #assign loot




            allow_save = True
            allow_load = True

        def find_trouble(self):
            #generates an encounter based on the dungeon and the threat level.
            pass

        def out_of_battle_units(self):
            #renpy.call_screen("oob_unit_tab", self)
            renpy.show_screen("oob_unit_tab", self)
        def out_of_battle_skills(self, unit):
            renpy.hide_screen("oob_move_select")
            renpy.show_screen("oob_move_select", self, unit)
        def out_of_battle_target(self, unit, move):
            renpy.hide_screen("oob_target_select")
            renpy.show_screen("oob_target_select", self, unit, move)

    class Dungeon_0(Dungeon):
        #this is the dungeon from the prologue.
        def __init__(self, master):
            self.master = master #overworld instance that called and presides over the dungeon.
            self.bg = "dungeon_bg" #image name

            self.entrance = Exit_room(1,0,(0,1,1,0)) #where the entrance is. party starts here, exits here.
            self.entrance.set_explored(1)
            self.spot_x = self.entrance.get_x() #where the player's x is at
            self.spot_y = self.entrance.get_y() #where the player's y is at

            self.monsterlist = [(0,0), (1,10), (2,3), (3,5)] #the threat necessary for the enemy to be faced in a random encounter
            self.threat = 1 #the longer you're in a dungeon, the higher the threat. the higher the threat, the stronger the monsters generated from random encounters.

            self.map = [
                [None, self.entrance, Fullheal_room(2,0,(0,0,1,1))],
                [Combat_room(0,1,(0,1,1,0)), Combat_room(1,1,(1,0,0,1)), Event_room(2,1,(1,0,1,0))],
                [Combat_room(0,2,(1,1,0,0)), Combat_room(1,2,(0,1,1,1)), Event_room(2,2,(1,0,1,1))],
                [None, Event_room(1,3,(1,0,1,0)), Event_room(2,3,(1,0,0,0))],
                [None, Event_room(1,4,(1,0,1,0)), None],
                [None, Event_room(1,5,(0,0,0,0)), None]
            ]

            self.party = [] #all the units player brought
            self.hold = [[],[],[]] #unit,x,y of ppl that were deployed last. x and y at the time they were deployed.

        def spawn_monster(self, type, dummymap):
            #type is the kind of monster that should be spawned. each dungeon will need its own.
            if type == 0: #jowler
                baddie = Unit_jowler(0, "jowler", dummymap.random_empty(), 1)

            elif type == 1: #groskel
                baddie = Unit_groskel(0, "groskel", dummymap.random_empty(), 0)

            elif type == 2: #spitter
                baddie = Unit_spitter(0, "spitter", dummymap.random_empty(), 1)

            elif type == 3: #frother
                baddie = Unit_frother(0, "frother", dummymap.random_empty(), 1)

            return baddie



#for calling a battle from nothing.











##eof

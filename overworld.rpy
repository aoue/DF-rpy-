#method:

#map nav for act I.
#here's how it works:
#-- when the screen is called, it is given arguments. These are:
#-first arg: list of booleans that determine whether a location is unlocked.
#-second arg: list of str label names that should be jumped to. paired one-to-one with first list.
#update the lists with each call.

#-----ACT I index-----#
#a certain item in the list always corresponds to the same physical location. It is as follows:
# [0] = Chere Hotel (hotel)
# [1] = Backstreet (becomes nai's office after first visit)
# [2] = Saint Hope's (slums)
# [4] =
# [3] =
# [5] =
# [6] =
# [7] =
# etc

init python:
    #overworld map
    class overworld():
        def __init__(self):
            self.chapter = 0 #str. from 0 (prologue) to 8 (chapter 8). master key to control everything else.

            self.party = [] #all units in the party.
            self.party_bg = "party_bg"
            self.view = 0 #which unit we are looking at right now.
            self.inventory = inventory()

            #--- lists of lists. each list inside corresponds to a chapter. all preset images in here. ---#
            self.unlocked = [[1, 1]] #whether the location can trigger an event.
            self.jumps = [["fail", "test_dungeon_entrance"]] #str of the label we're jumping to.
            self.descr = [["nice place", "test dungeon"]] #str description on hover.
            self.images = [["face_boy", "dungeon_icon"]] #normal image for a location
            self.hovers = [["face_boy_hover", "dungeon_icon_h"]] #hover image for a location
            self.positions = [[(300, 400), (600, 500)]] #position for a location
            self.bg = [["bg_chapter1"]] #the background image.

            self.direction = direction()

            self.dungeon_prologue = dungeon(self) #prologue dungeon
            self.dungeons = [[self.dungeon_prologue]] #dungeons for each chapter

        #setters
        def set_view(self, view):
            self.view = view

        #getters.
        def get_chapter(self):
            return self.chapter
        def get_direction(self):
            return self.direction
        def get_party(self):
            return self.party
        def get_party_bg(self):
            return self.party_bg
        def get_view(self):
            return self.view
        def get_inventory(self):
            return self.inventory
        #getters automatically return the chapter's list inside the larger list
        def set_view(self, view):
            self.view = view
        def get_unlocked(self):
            return self.unlocked[self.get_chapter()]
        def get_jumps(self):
            return self.jumps[self.get_chapter()]
        def get_descr(self):
            return self.descr[self.get_chapter()]
        def get_images(self):
            return self.images[self.get_chapter()]
        def get_hovers(self):
            return self.hovers[self.get_chapter()]
        def get_positions(self):
            return self.positions[self.get_chapter()]
        def get_bg(self):
            return self.bg[self.get_chapter()]
        def get_dungeons(self, x):
            return self.dungeons[self.get_chapter()][x]

        ## -- useful functions -- ##
        #party management
        def join_party(self, unit):
            self.get_party().append(unit)
            #centered text? unit.get_name() joins the party!
        def leave_party(self, unit):
            self.get_party().remove(unit)
            #centered text? unit.get_name() leaves the party!
        def party_view(self):
            renpy.show_screen("inventory_view", self.get_inventory().get_arm(), self.get_party()[self.get_view()].get_equip_types()[0])
            renpy.show_screen("move_view", self.get_party()[self.get_view()].get_movelist())
            renpy.call_screen("party_view", self.get_party(), self.get_view(), self)
        def next_party_unit(self, i):
            self.set_view(self.get_view() + i)

            if self.get_view() >= len(self.get_party()):
                self.set_view(0)
            elif self.get_view() < 0:
                self.set_view(len(self.get_party())-1)

            self.party_view()

        #inventory management
        def change_inventory_view(self, i):
            if i == 0:
                viewlist = self.get_inventory().get_arm()
            elif i == 1:
                viewlist = self.get_inventory().get_wea()
            elif i == 2:
                viewlist = self.get_inventory().get_acc()
            else:
                viewlist = self.get_inventory().get_ite()
            renpy.show_screen("inventory_view", viewlist, self.get_party()[self.get_view()].get_equip_types()[i])
        def swap_gear(self, unit, flag):
            new_gear = renpy.invoke_in_new_context(self.gear_view, flag, unit)

            if new_gear == 0: #cancel button
                return

            self.get_inventory().remove_gear(new_gear)

            #put previously equipped gear into inventory and equip new gear
            if flag == 1:
                self.get_inventory().add_gear(unit.get_armour())
                unit.set_armour(new_gear)
            elif flag == 2:
                self.get_inventory().add_gear(unit.get_weapon())
                unit.set_weapon(new_gear)
            else:
                self.get_inventory().add_gear(unit.get_acc())
                unit.set_acc(new_gear)
        def gear_view(self, flag, unit):
            renpy.show(self.get_party_bg())
            renpy.show_screen("party_view", self.get_party(), self.get_view(), self)
            if flag == 1:
                viewlist = ow.get_inventory().get_arm()
                equip_type = unit.get_equip_types()[0]
            elif flag == 2:
                viewlist = ow.get_inventory().get_wea()
                equip_type = unit.get_equip_types()[1]
            elif flag == 3:
                viewlist = ow.get_inventory().get_acc()
                equip_type = unit.get_equip_types()[2]

            new_gear = renpy.call_screen("gear_swap", viewlist, equip_type)

            renpy.hide(self.get_party_bg())
            return new_gear
        def gear_browse(self, gear):
            renpy.show_screen("gear_browse", gear)

        #move management
        def put_move(self, unit, spot, rank):
            new_move = renpy.invoke_in_new_context(self.move_view, unit, rank)
            if new_move == 0:
                return
            unit.get_movelist().remove(new_move)
            unit.get_moves()[spot] = new_move
        def swap_move(self, unit, spot, rank):
            new_move = renpy.invoke_in_new_context(self.move_view, unit, rank)
            if new_move == 0: #cancel button
                return

            unit.get_movelist().append(unit.get_moves()[spot])
            unit.get_movelist().remove(new_move)
            unit.get_moves()[spot] = new_move
        def move_view(self, unit, rank):
            renpy.show(self.get_party_bg())
            renpy.show_screen("party_view", self.get_party(), self.get_view(), self)
            new_move = renpy.call_screen("move_swap", unit.get_movelist(), rank)
            renpy.hide(self.get_party_bg())
            return new_move
        def move_browse(self, move):
            renpy.show_screen("move_browse", move)

        #direction
        def change_direction_view(self, chapter, state):
            renpy.invoke_in_new_context(self.direction_view, chapter, state)
        def direction_view(self, chapter, state):
            self.quest_view(self.get_direction().get_last_viewed())
            renpy.call_screen("chapter_view", chapter, state, self)
        def quest_view(self, quest):
            self.get_direction().set_last_viewed(quest)
            renpy.show_screen("quest_view", quest)





        #big shows
        def show_ow_helpers(self):
            renpy.transition(dissolve)
            renpy.show_screen("overworld_helpers", self)
        def show_overworld(self):
            renpy.call_screen("overworld_map", self.get_unlocked(), self.get_jumps(), self.get_descr(), self.get_images(), self.get_hovers(), self.get_positions(), self)
        def show_dungeon(self): #(self, floor)
            #for a dungeon 0. it will have to be preset.
            self.get_dungeons(0).set_party(self.get_party())
            self.get_dungeons(0).show_dungeon()
        def show_party(self):
            renpy.invoke_in_new_context(self.party_view)
        def show_direction(self):
            self.quest_view(self.get_direction().get_last_viewed())
            renpy.invoke_in_new_context(self.direction_view, self.get_chapter(), 0)


        def show_hub(self):
            pass












##eof

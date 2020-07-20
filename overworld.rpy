

#location icon offset: 54, 72

#overworld map bgs:
#-bg prologue
#-bg office
#-bg chp0
#-bg chp1
#-etc


#the overworld maps we see a lot of:
#city: shows when 0 is passed into show_overworld
# -apartment
# -dpt store
# -ice rink
# -etc

#hq: shows when 1 is passed into show_overworld
# -mueler's station
# -tori's office
# -crafting person. one of the workers at the crafting area

#cherespoir: shows when 2 is passed into show_overworld



init 2 python:
    #overworld map
    class Overworld():
        def __init__(self):
            self.chapter = 0 #int. from 0 (prologue) to 8 (chapter 8). master key to control everything else.
            self.timeofday = 0 #int. 0: morning, 1:noon, etc

            self.party = [] #all units in the party.
            self.party_bg = "party_bg"
            self.view = 0 #which unit we are looking at right now.
            self.inventory = Inventory()

            #--- lists of lists. each list inside corresponds to a chapter. all preset images in here. ---#


            ## -- Add only once it's actually implemented -- ##
            self.ow_routes = [Route_ms_0()]
            self.hq_routes = [Route_ms_0()] #mueler, tori, control, crafting, hospital.
            self.cherespoir_routes = [Route_ms_0(), Route_hill(), Route_store(), Route_square(), Route_lab(), Route_radio()] #friday, payton
            self.routes = [self.ow_routes, self.hq_routes, self.cherespoir_routes]

            self.bg = [["city_map"],["hq_map"], ["cherespoir_map_day", "cherespoir_map_night"]] #the background image.

            self.direction = Direction()

            self.in_dungeon = 0 #int. 0: in dungeon, 1: not in dungeon.
            self.dungeon_prologue = Dungeon_0(self) #prologue dungeon
            self.dungeons = [[self.dungeon_prologue]] #dungeons by each chapter. Lose access to old dungeons in new chapters.

        #setters
        def set_view(self, x):
            self.view = x
        def set_chapter(self, x):
            self.chapter = x
        def set_timeofday(self, x):
            self.timeofday = x

        #getters
        def get_timeofday(self):
            return self.timeofday
        def get_routes(self):
            return self.routes
        def get_in_dungeon(self):
            return self.in_dungeon
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
        def get_bg(self, x):
            return self.bg[x][self.get_timeofday()]
        def get_dungeons(self, x):
            return self.dungeons[self.get_chapter()][x]

        #setters
        def set_in_dungeon(self, x):
            self.in_dungeon = x

        ## -- useful functions -- ##
        #party management
        def join_party(self, unit):
            self.get_party().append(unit)
            #centered text? unit.get_name() joins the party.
        def leave_party(self, unit):
            self.get_party().remove(unit)
            #centered text? unit.get_name() has left the party.
        def party_view(self, i):
            renpy.show_screen("inventory_view", self.get_inventory().get_arm(), self.get_party()[i].get_equip_types()[0])
            renpy.show_screen("move_view", self.get_party()[i].get_movelist())
            renpy.call_screen("party_view", self.get_party(), i, self)
        def next_party_unit(self, i):
            self.set_view(self.get_view() + i)

            if self.get_view() >= len(self.get_party()):
                self.set_view(0)
            elif self.get_view() < 0:
                self.set_view(len(self.get_party())-1)

            self.party_view(self.get_view())

        #inventory management
        def change_inventory_view(self, i):
            if i == 0:
                viewlist = self.get_inventory().get_arm()
            elif i == 1:
                viewlist = self.get_inventory().get_wea()
            elif i == 2:
                viewlist = self.get_inventory().get_acc()
            renpy.show_screen("inventory_view", viewlist, self.get_party()[self.get_view()].get_equip_types()[i])
        def swap_gear(self, unit, flag):

            if flag == 1:
                old_passive = unit.get_armour().get_passive()
            elif flag == 2:
                old_passive = unit.get_weapon().get_passive()
            elif flag == 3:
                old_passive = unit.get_acc().get_passive()


            new_gear = renpy.invoke_in_new_context(self.gear_view, flag, unit)

            if new_gear == 0: #cancel button
                return
            elif new_gear == -1: #unequip
                if flag == 1:
                    if unit.get_armour().get_type() != 0:
                        self.get_inventory().add_gear(unit.get_armour())
                    unit.set_armour(None_armour())

                elif flag == 2:
                    if unit.get_weapon().get_type() != 0:
                        self.get_inventory().add_gear(unit.get_weapon())
                    unit.set_weapon(None_weapon())

                elif flag == 3:
                    if unit.get_acc().get_type() != 0:
                        self.get_inventory().add_gear(unit.get_acc())
                    unit.set_acc(None_accessory())

            else:
                self.get_inventory().remove_gear(new_gear)
                #put previously equipped gear into inventory and equip new gear
                if flag == 1:
                    if unit.get_armour().get_type() != 0:
                        self.get_inventory().add_gear(unit.get_armour())
                    unit.set_armour(new_gear)
                elif flag == 2:
                    if unit.get_weapon().get_type() != 0:
                        self.get_inventory().add_gear(unit.get_weapon())
                    unit.set_weapon(new_gear)
                elif flag == 3:
                    if unit.get_acc().get_type() != 0:
                        self.get_inventory().add_gear(unit.get_acc())
                    unit.set_acc(new_gear)
            unit.post_battle()

            #check if unit's passive should also be removed
            if unit.get_passive()[1] == old_passive:
                unit.set_passive(1, Passive())
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
            if new_move == 0 or new_move == -1:
                return
            unit.get_moves()[spot] = new_move
            unit.get_movelist().remove(new_move)
            #renpy.hide_screen("move_browse")
        def swap_move(self, unit, spot, rank):
            new_move = renpy.invoke_in_new_context(self.move_view, unit, rank)
            if new_move == 0: #cancel button
                return
            unit.get_movelist().append(unit.get_moves()[spot])
            if new_move == -1:
                unit.get_moves()[spot] = None
            else:
                unit.get_moves()[spot] = new_move
                unit.get_movelist().remove(new_move)
        def move_view(self, unit, rank):
            renpy.show(self.get_party_bg())
            renpy.show_screen("party_view", self.get_party(), self.get_view(), self)
            new_move = renpy.call_screen("move_swap", unit.get_movelist(), rank)
            renpy.hide(self.get_party_bg())
            return new_move
        def move_browse(self, move):
            renpy.show_screen("move_browse", move)

        #passive management
        def swap_passive(self, unit, x):

            if x == 0: #intrinsic passive swap
                pl = copy_list(unit.get_passivelist())
            else:
                pl = []
                if unit.get_armour().get_passive() != 0:
                    pl.append(unit.get_armour().get_passive())
                if unit.get_weapon().get_passive() != 0:
                    pl.append(unit.get_weapon().get_passive())
                if unit.get_acc().get_passive() != 0:
                    pl.append(unit.get_acc().get_passive())

            if unit.get_passive()[x] in pl:
                pl.remove(unit.get_passive()) #swap this to remove all occurences of the equipped passive in pl

            new_passive = renpy.invoke_in_new_context(self.passive_view, pl)

            if new_passive == 0: #cancel
                return
            elif new_passive == -1: #unequipped
                unit.set_passive(x, Passive())
                return
            unit.set_passive(x, new_passive)
        def passive_browse(self, passive):
            renpy.show_screen("passive_browse", passive)
        def passive_view(self, pl):
            renpy.show(self.get_party_bg())
            renpy.show_screen("party_view", self.get_party(), self.get_view(), self)
            new_passive = renpy.call_screen("passive_swap", pl)
            renpy.hide(self.get_party_bg())
            return new_passive

        #direction
        def change_direction_view(self, chapter):
            renpy.invoke_in_new_context(self.direction_view, chapter)
        def direction_view(self, chapter):
            self.quest_view(self.get_direction().get_last_viewed())
            renpy.call_screen("chapter_view", chapter, self)
        def quest_view(self, quest):
            renpy.hide_screen("quest_view")
            self.get_direction().set_last_viewed(quest)
            renpy.show_screen("quest_view", quest)

        #big shows
        def show_tooltip(self, descr, loc, images):
            renpy.transition(dissolve)
            renpy.show_screen("overworld_tooltip", descr, loc, images)
        def show_ow_helpers(self):
            renpy.transition(dissolve)
            renpy.show_screen("overworld_helpers", self)
        def show_overworld(self, chapter):
            renpy.retain_after_load()
            self.set_in_dungeon(0)
            renpy.call_screen("overworld_map", self, chapter)
        def show_dungeon(self): #(self, floor)
            #for a dungeon 0. it will have to be preset.
            self.set_in_dungeon(1)
            self.get_dungeons(0).set_party(self.get_party())
            self.get_dungeons(0).show_dungeon()
        def show_party(self, i):
            renpy.invoke_in_new_context(self.party_view, i)
        def show_party_step(self):
            renpy.transition(dissolve)
            renpy.show_screen("party_step", self)
        def show_inventory_step(self):
            renpy.transition(dissolve)
            renpy.show_screen("inventory_view_proper", self)
        def show_direction(self):
            renpy.transition(dissolve)
            self.quest_view(self.get_direction().get_last_viewed())
            renpy.invoke_in_new_context(self.direction_view, self.get_chapter())
            renpy.hide_screen("quest_view")


        def show_hub(self):
            pass












##eof


init -2 python:
    allow_save = True


    ##save testing stuff##
    #config.use_cpickle = False # <-- if saving breaks again, uncomment this line.

    #--- BATTLE ---#
    class Map():
        def __init__(self, nl):
            #self.map = [[None]*5, [None]*5] #the grid. fill a certain spot with a unit child object
            self.map = [[None]*5, [None]*5, [None]*5, [None]*5, [None]*5] #the grid. fill a certain spot with a unit child object.

            #set up the grid based on the units passed in
            for unit in nl:
                self.place_unit(unit)

        #getters
        def get_map(self):
            return self.map
        def get_ul(self):
            return self.ul
        #useful functions
        def remove_unit(self, unit):
            #finds the unit's spot, and sets it to None.

            for i in range(0, unit.get_point().get_gros()[0]):
                for x in range(0, unit.get_point().get_gros()[1]):
                    self.get_map()[unit.get_point().get_x()+i][unit.get_point().get_y()+x] = None

        def place_unit(self, unit):
            #first look for the unit. if it's in the list, set the list object to none
            #index returns the 'index' of the unit we're looking for. so set = none by index

            for i in range(0, unit.get_point().get_gros()[0]):
                for x in range(0, unit.get_point().get_gros()[1]):
                    self.get_map()[unit.get_point().get_x()+i][unit.get_point().get_y()+x] = unit

        def search_map(self, dtuple):
            unit = self.get_map()[dtuple[0]][dtuple[1]]
            return unit

        def random_empty(self):
            #returns a random empty position
            while True:
                x = renpy.random.randint(0, 4)
                y = renpy.random.randint(0, 4)

                if self.search_map((x,y)) == None:
                    return x,y


    class Battle():
        def __init__(self, rounds, party, pl, el, bg, inventory):
            self.rounds = rounds #number of rounds the battle will last. negative for infinite.
            self.bg = bg
            self.phase = ""
            self.party = party #all the units in the player's party. necessary for exp and subs.
            self.pl = pl #all the currently active units
            self.el = el
            self.pable = 0
            self.eable = 0
            self.ableleft = 0
            self.last_turn = 1
            self.allymap = Map(pl)
            self.enemymap = Map(el)
            self.totalexp = 0
            self.inventory = inventory
            self.totalloot = []

        #getters
        def get_totalloot(self):
            return self.totalloot
        def get_inventory(self):
            return self.inventory
        def get_party(self):
            return self.party
        def get_rounds(self):
            return self.rounds
        def get_bg(self):
            return self.bg
        def get_phase(self):
            return self.phase
        def get_pl(self):
            return self.pl
        def get_el(self):
            return self.el
        def get_pable(self):
            return self.pable
        def get_eable(self):
            return self.eable
        def get_ableleft(self):
            return self.ableleft
        def get_last_turn(self):
            return self.last_turn
        def get_allymap(self):
            return self.allymap
        def get_enemymap(self):
            return self.enemymap
        def get_totalexp(self):
            return self.totalexp
        #setters
        def set_rounds(self, rounds):
            self.rounds = rounds
        def set_bg(self, bg):
            self.bg = bg
        def set_phase(self, phase):
            self.phase = phase
        def set_pable(self, pable):
            self.pable = pable
        def set_eable(self, eable):
            self.eable = eable
        def set_ableleft(self, ableleft):
            self.ableleft = ableleft
        def set_last_turn(self, last):
            self.last_turn = last
        def set_totalexp(self, exp):
            self.totalexp = exp
        #--during battle
        def move_browse_b(self, move):
            renpy.show_screen("move_browse_b", move)
        def calc_pable(self):
            pable = 0
            for i in range(0, len(self.get_pl())):
                pable += self.get_pl()[i].get_able()
            return pable
        def calc_eable(self):
            eable = 0
            for i in range(0, len(self.get_el())):
                eable += self.get_el()[i].get_able()
            return eable
        def calc_turns(self):
            self.set_pable(self.calc_pable())
            self.set_eable(self.calc_eable())
            self.set_ableleft(self.get_pable() + self.get_eable())
        def is_battle_over(self):
            if self.get_rounds() == 0:
                renpy.say(None, "Time elapsed.")
                return 1
            elif all(obj.get_ooa() == 1 for obj in self.get_pl()) or all(obj2.get_ooa() == 1 for obj2 in self.get_el()):
                renpy.say(None, "All units on one side defeated. Battle has ended.")
                return 1
            else:
                return 0
        def refresh_visuals(self):
            renpy.show_screen("combatinfo", self.get_pl(), self.get_el(), self.get_pable(), self.get_eable(), self.get_rounds(), self.get_phase())
            renpy.show_screen("show_units", self.get_pl(), self.get_el())

        #--settings
        def prebattle_settings(self):
            config.rollback_enabled = False
            renpy.scene()
            renpy.show(self.get_bg())



        def postbattle_settings(self):
            renpy.block_rollback()
            config.rollback_enabled = True
            renpy.hide_screen("show_units")
            renpy.hide_screen("combatinfo")
            renpy.hide(self.get_bg())

            #level up stuff
            showlist = []
            for unit in self.get_party():
                unit.post_battle()
                unit.get_foc().level_up(unit, self.get_totalexp(), showlist)

                 #shows the level up screen, so the player knows what's going on behind the scenes.

            #loot stuff
            showlist2 = [0]
            for loot in self.get_totalloot(): #loot is a tuple.
                if loot == None:
                    pass
                elif renpy.random.randint(0,100) + loot[-1] > 100:
                    if len(loot) == 3: #add money
                        money = renpy.random.randint(loot[0], loot[1])
                        self.get_inventory().add_money(money)
                        showlist2[0] += money
                    else: #add gear object
                        self.get_inventory().add_gear(loot[0])
                        showlist2.append(loot[0])


            renpy.show_screen("level_up", showlist, showlist2)

            renpy.pause()
            renpy.hide_screen("level_up")

        def game_over(self):
            pass
            #show options:
            #redo battle?
            #return to title?

        #--combat round. uses everything
        def unit_dots(self):
            showlist = [] #list of tuples: (unit, damage)

            for unit in self.get_pl():
                if unit.get_stance().get_dot() != 0:
                    tup = (unit, int(unit.get_stance().get_dot()*unit.get_hpmax_actual()))
                    showlist.append(tup)

            for unit in self.get_el():
                if unit.get_stance().get_dot() != 0:
                    tup = (unit, int(unit.get_stance().get_dot()*unit.get_hpmax_actual()))
                    showlist.append(tup)

            if len(showlist) > 0:
                renpy.show_screen("show_dot", showlist)
        def new_round(self):
            renpy.say(None, "new round")

            self.unit_dots()

            for unit in self.get_pl():
                if unit.get_ooa() == 0:
                    unit.set_able(unit.get_ablemax_actual()) #regain able
                    unit.set_turn_over(0)
                    unit.get_stance().refresh_stamina(unit) #restam
                    unit.get_stance().round_start(unit, self)

                    for p in unit.get_passive():
                        if p.get_check() == 0:
                            p.exert()

            for unit in self.get_el():
                if unit.get_ooa() == 0:
                    unit.set_able(unit.get_ablemax_actual()) #regain able
                    unit.get_stance().refresh_stamina(unit) #restam
                    unit.get_stance().round_start(unit, self)

                    for p in unit.get_passive():
                        if p.get_check() == 0:
                            p.exert()
        def player_turn(self):
            #choose unit
            #choose move
            #cancel if you're unsatisfied

            while True:
                chosen = renpy.call_screen("order_unit", self.get_pl())
                renpy.call_screen("pick_move", chosen, self)
                self.calc_turns()
                self.refresh_visuals()

                if chosen.get_turn_over() == 1:
                    return
        def enemy_turn(self):
            chosen = None
            nl = copy_list(self.get_el())
            #calc priority of each unit. the one with the highest priority will be
            for eunit in nl:
                if eunit.get_ooa() == 0 and eunit.get_able() > 0:
                    max = eunit.calc_priority(self.get_el())
                    chosen = eunit
                    nl.remove(eunit)
                    break
            for eunit in nl:
                if eunit.get_ooa() == 0 and eunit.get_able() > 0:
                    x = eunit.calc_priority(self.get_el())
                    if max < x:
                        max = x
                        chosen = eunit
            chosen.take_turn(self.get_el(), self.get_pl(), self)

        def combat_round(self):
            self.prebattle_settings()

            for unit in self.get_el():
                self.get_enemymap().place_unit(unit)
            for unit in self.get_pl():
                self.get_allymap().place_unit(unit)

            while self.get_rounds != 0: #for the whole fight
                self.calc_turns()

                while self.get_ableleft() > 0: #for one round

                    if (self.get_pable() > 0 and self.get_last_turn() == 1) or (self.get_pable() > 0 and self.get_eable() == 0): #player turn
                        self.set_phase("act")
                        self.refresh_visuals()

                        self.player_turn()

                        self.set_last_turn(0)

                    if self.is_battle_over() == 1:
                        self.postbattle_settings()
                        return

                    if (self.get_eable() > 0 and self.get_last_turn() == 0) or (self.get_eable() > 0 and self.get_pable() == 0): #enemy turn
                        self.set_phase("vile")
                        self.refresh_visuals()

                        self.enemy_turn()

                        self.calc_turns()
                        self.refresh_visuals()

                        self.set_last_turn(1)

                    if self.is_battle_over() == 1:
                        self.postbattle_settings()
                        return

                self.set_rounds(self.get_rounds()-1) #proceed to next round
                if self.is_battle_over() == 1:
                    self.postbattle_settings()
                    return

                self.new_round() #reset for next round


            self.postbattle_settings()


#reinforcement placing function



#target picking functions

    def enemy_highlighter(unit, cmove, row, column):
        renpy.show_screen("enemy_highlight_extra", unit, cmove, row, column)
    def ally_highlighter(unit, cmove, row, column):
        renpy.show_screen("ally_highlight_extra", unit, cmove, row, column)
    def hide_highlighter():
        renpy.hide_screen("enemy_highlight_extra")
        renpy.hide_screen("ally_highlight_extra")
    def call_highlight_e(unit, cmove, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("enemy_highlight", unit, cmove, battle)
        return sq
    def call_highlight_a(unit, cmove, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("ally_highlight", unit, cmove, battle)
        return sq
    def call_highlight_walk(unit, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("walk_highlight", unit, battle)
        return sq







#eof

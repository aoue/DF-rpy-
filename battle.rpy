
init -2 python:
    import random
    allow_save = True

    #--- BATTLE ---
    class map():
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

        def remove_unit(self, unit):
            #finds the unit's spot, and sets it to None.
            self.get_map()[unit.get_point().get_x()][unit.get_point().get_y()] = None

        def place_unit(self, unit):
            #first look for the unit. if it's in the list, set the list object to none
            #index returns the 'index' of the unit we're looking for. so set = none by index
            self.get_map()[unit.get_point().get_x()][unit.get_point().get_y()] = unit

        def search_map(self, dtuple):
            unit = self.get_map()[dtuple[0]][dtuple[1]]
            return unit


    class battle():
        def __init__(self, rounds, pl, el, bg):
            self.rounds = rounds #number of rounds the battle will last. negative for infinite.
            self.bg = bg
            self.phase = ""
            self.pl = pl
            self.el = el
            pable = 0
            eable = 0
            ableleft = 0
            self.allymap = map(pl)
            self.enemymap = map(el)

        #getters
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
        def get_allymap(self):
            return self.allymap
        def get_enemymap(self):
            return self.enemymap
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
        #--during battle
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
        def new_round(self):
            renpy.say(None, "new round")
            for unit in self.get_pl():
                if unit.get_ooa() == 0:
                    unit.set_able(unit.get_ablemax()) #refresh able
                    unit.get_stance().refresh_stamina(unit) #restam

            for unit in self.get_el():
                if unit.get_ooa() == 0:
                    unit.set_able(unit.get_ablemax())
                    unit.get_stance().refresh_stamina(unit) #restam
        #--settings
        def prebattle_settings(self):
            config.rollback_enabled = False
            renpy.scene()
            renpy.show(self.get_bg())
        def postbattle_settings(self):
            renpy.block_rollback()
            config.rollback_enabled = True
            renpy.hide_screen("combatinfo")
        def game_over(self):
            pass
            #return to title screen

        #--combat round. uses everything
        def player_turn(self):
            #show available moves.
            #click on move. pick target location.
            #resolve damage, etc.
            chosen = renpy.call_screen("order_unit", self.get_pl())
            chosen.get_stance().turn_start(chosen)
            renpy.call_screen("pick_move", chosen, self)


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

            chosen.get_stance().turn_start(chosen)
            chosen.take_turn(self.get_el(), self.get_pl(), self)

        def combat_round(self):
            self.prebattle_settings()

            for unit in self.get_pl():
                self.get_allymap().place_unit(unit) #a hack. this is supposed to be done in the constructor. i can't figure out for the life of me why it isn't working. it stopped a unit from using first_aid() on another unit until the targeted unit had moved.
            for unit in self.get_el():
                self.get_enemymap().place_unit(unit)

            while self.get_rounds > 0: #for the whole fight
                self.calc_turns()

                while self.get_ableleft() > 0: #for one round

                    if self.get_pable() > 0: #player turn
                        self.set_phase("act")
                        self.refresh_visuals()

                        self.player_turn()

                        self.calc_turns()
                        self.refresh_visuals()

                    if self.is_battle_over() == 1:
                        self.postbattle_settings()
                        return

                    if self.get_eable() > 0: #enemy turn
                        self.set_phase("vile")
                        self.refresh_visuals()

                        self.enemy_turn()

                        self.calc_turns()
                        self.refresh_visuals()


                    if self.is_battle_over() == 1:
                        self.postbattle_settings()
                        return

                self.set_rounds(max(self.get_rounds()-1,0)) #proceed to next round
                if self.is_battle_over() == 1:
                    self.postbattle_settings()
                    return
                self.new_round() #reset for next round


            self.postbattle_settings()


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
        sq = renpy.call_screen("enemy_highlight", unit, cmove)
        return sq
    def call_highlight_a(unit, cmove, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("ally_highlight", unit, cmove)
        return sq
    def call_highlight_walk(unit, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("walk_highlight", unit, battle)
        return sq







#eof

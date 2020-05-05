
init python:
    import random

    #--- BATTLE ---
    class map():
        def __init__(self, nl):
            #self.map = [[None]*5, [None]*5] #the grid. fill a certain spot with a unit child object
            self.map = [[None]*5, [None]*5, [None]*5, [None]*5, [None]*5] #the grid. fill a certain spot with a unit child object

            #set up the grid based on the units passed in
            for i in range(0, len(nl)):
                self.place_unit(nl[i])

        #getters
        def get_map(self):
            return self.map
        def get_ul(self):
            return self.ul

        def place_unit(self, unit):
            #places unit according to their x, y coordinates. 5x5 grid.
            #renpy.say(None, "{}, {}".format(unit.get_point().get_x(), unit.get_point().get_y()))
            self.get_map()[unit.get_point().get_x()][unit.get_point().get_y()] = unit

        def search_map(self, dtuple):
            unit = self.get_map()[dtuple[0]][dtuple[1]]

            return unit

        def move_unit(self, xi, yi, xf, yf):
            #move the unit from one map place to another.
            #find the unit by its initial coordinates (xi, yi), and place it at its final (xf, yf)
            pass

        def kill_unit(self, unit):
            #enemy unit ooa. set self.map[row][col] = None
            pass


    class battle(): #battle class. runs all the battles nice and tidily.
        def __init__(self, rounds, pl, el, bg):
            self.rounds = rounds #number of rounds the battle will last. negative for infinite.
            self.bg = bg
            self.phase = ""
            self.pl = pl
            self.el = el
            pable = 0
            eable = 0
            ableleft = 0
            self.allymap = map(self.pl)
            self.enemymap = map(self.el)

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

        def reset_round(self):
            renpy.say(None, "new round")
            self.refresh_stamina()
            for i in range(0, len(self.get_pl())):
                if self.get_pl()[i].get_ooa() == 0:
                    self.get_pl()[i].set_able(self.get_pl()[i].get_ablemax())
            for i in range(0, len(self.get_el())):
                if self.get_el()[i].get_ooa() == 0:
                    self.get_el()[i].set_able(self.get_el()[i].get_ablemax())
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
            renpy.show_screen("combatinfo", self.get_pl(), self.get_el(), self.get_pable(), self.get_eable(), self.get_ableleft(), self.get_rounds(), self.get_phase())
            renpy.show_screen("show_units", self.get_pl(), self.get_el())
        def refresh_stamina(self):
            for i in range(0, len(self.get_pl())):
                self.get_pl()[i].set_stamina(min(self.get_pl()[i].get_stamina() + self.get_pl()[i].get_restam(), self.get_pl()[i].get_staminamax()))

        #--settings
        def prebattle_settings(self):
            config.rollback_enabled = False
            renpy.scene()
            renpy.show(self.get_bg())
        def postbattle_settings(self):
            renpy.block_rollback()
            config.rollback_enabled = True
            renpy.hide_screen("combatinfo")

        #--combat round. uses everything
        def player_turn(self):
            #show available moves.
            #click on move. pick target location.
            #resolve damage, etc.
            chosen = renpy.call_screen("order_unit", self.get_pl())
            renpy.call_screen("pick_move", chosen, self)

        def enemy_turn(self):
            renpy.say(None, "enemy turn")

        def combat_round(self):
            self.prebattle_settings()

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
                        return

                    if self.get_eable() > 0: #enemy turn
                        self.set_phase("vile")
                        self.refresh_visuals()

                        self.enemy_turn()

                        self.calc_turns()
                        self.refresh_visuals()


                    if self.is_battle_over() == 1:
                        return

                self.set_rounds(max(self.get_rounds()-1,0)) #proceed to next round
                self.reset_round() #reset for next round

            self.postbattle_settings()

#standalone functions
    def call_highlight_e(unit, cmove, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("enemy_highlight", unit, cmove)
        return sq
    def call_highlight_a(unit, cmove, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("allied_highlight", unit, cmove)
        return sq
    #---- TARGETING LEGEND ----
    # 1: 1x1
    # 2: 1x2
    # 3: 1x3
    # 4: 1x4
    # 5: 1x5
    # 6: 2x1
    # 7: 2x2
    # 8: 2x3
    # 9: 2x4
    #10: 2x5
    #11: 3x1
    #12: 3x2
    #13: 3x3
    #14: 3x4
    #14: 3x5
    #15: 4x1
    #16: 4x2
    #17: 4x3
    #18: 4x4
    #19: 4x5
    #20: 5x1
    #21: 5x2
    #22: 5x3
    #23: 5x4
    #24: 5x5
    #26: cross 3x3
    #27: cross 5x5

    def enemy_highlighter(unit, cmove, row, column):
        if cmove.get_type() == 2:
            renpy.show("tile_e_hovered", at_list=[e_tile_hover(row, column-1)], zorder = 102)

        elif cmove.get_type() == 3:
            pass

    #highlighting allied grid
    def ally_highlighter(unit, cmove, row, column):
        if cmove.get_type == 2:
            renpy.show("tile_f_hovered", at_list=[a_tile_hover(row, column-1)], zorder = 102)

        elif cmove.get_type() == 3:
            pass


    def hide_highlighter(type):
        if type == 0:
            renpy.hide("tile_e_hovered")
        else:
            renpy.hide("tile_f_hovered")

    def unit_pass(unit):
        unit.set_able(0)
        unit.set_stamina(min(unit.get_stamina()+10, unit.get_staminamax()))

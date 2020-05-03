
#types of units: (combined arms)
#-squad: a group of people with some type of weapons. varies depending on weapon.
#-tank: a single or pair of tanks with some type of weapoms. varies depending on model
#-artillery: varies on model
#-mech: varies on model. tigers, dragonflys, hyenas, etc?

#--LEGEND--#
#self.name = "vile grunt"
#self.point = point(0, 0) #instance of point class. coordinates for unit's position.
#self.icon = "icon_grunt" #picture
#self.deployable = 1 #whether you can field them
#self.able = 1 #let's the unit act each round
#self.lvl = 0 #lvl, tracks stat increase and move learning. start at lvl 0.
#self.exp = 0 #the unit's exp for leveling up
#self.evo = 0 #whether the unit is in evo mode

#self.hpmax = 300 + (20 *lvl) #max hp
#self.hp = 300 + (20 *lvl)#current hp
#self.dodgemax = 10 + (1 *lvl)#max dodge
#self.dodge = 10 + (1 *lvl)#percent chance to dodge attacks.
#self.ooa = 0 #out of action. defeated.
#self.dead = 0 #dead. not a battle stat.

#self.aff = 0 #9 total. 0 through 8.
#self.physa = 80 + (3 *lvl)#physical attack
#self.physd = 80 + (3 *lvl)#physical defense
#self.maga = 80 + (1 *lvl)#magical attack
#self.magd = 80 + (2 *lvl)#magical defense
#self.stance = [0] * 5 #times however many stances there are

#self.pattern = 3 #3/3
#self.flavour = [""] * 7 # 7 of them. is set when moves are selected

#--------------------------------
#self.pattern = 0 #how many moves the unit has
# 1: 5/1
# 2: 4/2
# 3: 3/3
# 4: 2/4
# 5: 1/5

#self.affinity = 0
# 0: normal
# 1: heroic
# 2: vile
# 3: earth
# 4: ice
# 5: fire
# 6: water
# 7: lightning
# 8: metal
#--------------------------------


init python:
    #https://lemmasoft.renai.us/forums/viewtopic.php?t=19572    <-- ripped from

    class battle(): #battle class. runs all the battles nice and tidily.
        def __init__(self, rounds, pl, el, bg):
            self.rounds = rounds #number of rounds the battle will last. negative for infinite.
            self.bg = bg
            self.phase = ""
            self.pl = pl
            self.el = el
            self.allymap = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
            self.enemymap = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

        #getters
        def get_pturns(self):
            return self.pturns
        def get_eturns(self):
            return self.eturns
        def get_bg(self):
            return self.bg
        def get_rounds(self):
            return self.rounds
        def get_pl(self):
            return self.pl
        def get_el(self):
            return self.el

        def get_phase(self):
            return self.phase

        #setters
        def set_pturns(self, pturns):
            self.pturns = pturns
        def set_eturns(self, eturns):
            self.eturns = eturns
        def set_phase(self, phase):
            self.phase = phase
        def set_bg(self, bg):
            self.bg = bg
        def set_rounds(self, rounds):
            self.rounds = rounds

        #--during battle
        def calc_pturns(self):
            pturns = 0
            for i in range(0, len(self.get_pl())):
                if self.get_pl()[i].get_ooa() == 0:
                    pturns += 1
            return pturns
        def calc_eturns(self):
            eturns = 0
            for i in range(0, len(self.get_el())):
                if self.get_el()[i].get_ooa() == 0:
                    eturns += 1
            return eturns
        def reset_round(self):
            for i in range(0, len(self.get_pl())):
                if self.get_pl()[i].get_ooa() == 0:
                    self.get_pl()[i].set_able(1)
            for i in range(0, len(self.get_el())):
                if self.get_el()[i].get_ooa() == 0:
                    self.get_el()[i].set_able(1)
        def is_battle_over(self):
            if self.get_rounds() == 0:
                renpy.say(None, "Time elapsed.")
                return 1
            elif all(obj.get_ooa() == 1 for obj in self.get_pl()) or all(obj2.get_ooa() == 1 for obj2 in self.get_el()):
                renpy.say(None, "All units on one side defeated. Battle has ended.")
                return 1
            else:
                return 0
        def refresh_visuals(self, turnsleft):
            renpy.show_screen("combatinfo", self.get_pl(), self.get_el(), self.get_pturns(), self.get_eturns(), turnsleft, self.get_rounds(), self.get_phase())
            renpy.show_screen("show_units", self.get_pl(), self.get_el())

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
            renpy.call_screen("pick_move", chosen)

        def enemy_turn(self):
            renpy.say(None, "Dieee")

        def combat_round(self):
            self.prebattle_settings()

            while self.get_rounds > 0: #for the whole fight
                self.set_pturns(self.calc_pturns())
                self.set_eturns(self.calc_eturns())
                turnsleft = self.get_pturns() + self.get_eturns()

                while turnsleft > 0: #for one round

                    if self.get_pturns() > 0: #player turn
                        self.set_phase("act")
                        self.refresh_visuals(turnsleft)

                        #keep separate to help handle extra turns and whatnot.
                        #select unit. (using a screen)
                        #show unit's moves (using another screen)
                        #activate the selected move.
                        self.player_turn()

                        self.set_pturns(self.get_pturns()-1)
                        self.refresh_visuals(turnsleft)

                    turnsleft = self.get_pturns() + self.get_eturns()

                    if self.get_eturns() > 0: #enemy turn
                        self.set_phase("vile")
                        self.refresh_visuals(turnsleft)

                        #enemy thinks
                        self.enemy_turn()

                        self.set_eturns(self.get_eturns()-1)
                        self.refresh_visuals(turnsleft)

                    turnsleft = self.get_pturns() + self.get_eturns()

                if self.is_battle_over() == 1:
                    return

                self.set_rounds(max(self.get_rounds()-1,0)) #proceed to next round
                self.reset_round() #reset for next round

            self.postbattle_settings()

    class point():
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def set_x(self, x):
            self.x = x
        def set_y(self, y):
            self.y = y
        def get_x(self):
            return self.x
        def get_y(self):
            return self.y

    class move():
        def __init__(self):
            self.flavour = "{i}hit hard and fast{/i}"
            self.title = "move"
            self.rank = 0 #can be 0, 1, or 2. determines where the move can be used
            self.displayer = 0 #int in some range. tells what kind of display to be.
            self.type = 0 #for targeting. 1 through 13? each one means a different shape.
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.

        def get_flavour(self):
            return self.flavour
        def get_title(self):
            return self.title
        def get_rank(self):
            return self.rank
        def get_displayer(self):
            return self.displayer
        def get_type(self):
            return self.type
        def get_iff(self):
            return self.iff

        def effect(self):
            pass

    class hit(move):
        def __init__(self):
            self.flavour = "{i}A hit, hard and fast.{/i}"
            self.title = "Hit"
            self.rank = 1
            self.displayer = 0
            self.type = 0
            self.iff = 0

    class jumpkick(move):
        def __init__(self):
            self.flavour = "{i}Fly in from the back.{/i}"
            self.title = "Jump Kick"
            self.rank = 2
            self.displayer = 0
            self.type = 1
            self.iff = 0

    class evo_storm(move):
        def __init__(self):
            self.flavour = "{i}Storm on the horizon.{/i}"
            self.title = "Storm"
            self.rank = 0
            self.displayer = 0
            self.type = 0
            self.iff = 0


    #unit parent class
    class unit:
        #constructor:
        def __init__(self):
            self.name = "Default Entity"
            self.point = point(0,0) #instance of point class. coordinates for unit's position.
            self.icon = "mechicon_mc" #picture
            self.deployable = 1 #whether you can field them
            self.able = 1 #let's the unit act each round
            self.lvl = 0 #what level the unit's at.
            self.exp = 0 #the unit's exp for leveling up
            self.evo = 0 #whether the unit is in evo mode

            self.hpmax = 0 #max hp
            self.hp = 0 #current hp
            self.dodgemax = 30 #max dodge. always a bit higher than dodge.
            self.dodge = 20 #percent chance to dodge attacks.
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 0 # #affinity. 9 total.
            self.physa = 0 #physical attack
            self.physd = 0 #physical defense
            self.maga = 0 #magical attack
            self.magd = 0 #magical defense
            self.stance = [0] * 5 #times however many stances there are

            #moves:
            self.pattern = 3 #3/3
            self.move1 = hit(move)
            self.move2 = hit(move)
            self.move3 = hit(move)
            self.move4 = hit(move)
            self.move5 = hit(move)
            self.move6 = hit(move)
            self.move7 = hit(move)
            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]
        #getters
        def get_name(self):
            return self.name
        def get_point(self):
            return self.point
        def get_icon(self):
            return self.icon
        def get_deployable(self):
            return self.deployable
        def get_able(self):
            return self.able
        def get_lvl(self):
            return self.lvl
        def get_exp(self):
            return self.exp
        def get_evo(self):
            return self.evo
        def get_hpmax(self):
            return self.hpmax
        def get_hp(self):
            return self.hp
        def get_dodgemax(self):
            return self.dodgemax
        def get_dodge(self):
            return self.dodge
        def get_ooa(self):
            return self.ooa
        def get_dead(self):
            return self.dead
        def get_aff(self):
            return self.aff
        def get_physa(self):
            return self.physa
        def get_physd(self):
            return self.physd
        def get_maga(self):
            return self.maga
        def get_magd(self):
            return self.magd
        def get_stance(self, i):
            return self.stance[i]
        def get_pattern(self):
            return self.pattern
        def get_moves(self):
            return self.moves
        def get_flavour(self, i):
            return self.flavour[i]
        #setters
        def set_name(self, name):
            self.name = name
        def set_point(self, x, y):
            self.point.set_x(x)
            self.point.set_y(y)
        def set_icon(self, icon):
            self.icon = icon
        def set_deployable(self, deployable):
            self.deployable = deployable
        def set_able(self, able):
            self.able = able
        def set_lvl(self, lvl):
            self.lvl = lvl
        def set_exp(self, exp):
            self.exp = exp
        def set_evo(self, evo):
            self.evo = evo
        def set_hpmax(self, hpmax):
            self.hpmax = hpmax
        def set_hp(self, hp):
            self.hp = hp
        def set_dodgemax(self, dodgemax):
            self.dodgemax = dodgemax
        def set_dodge(self, dodge):
            self.dodge = dodge
        def set_ooa(self, ooa):
            self.ooa = ooa
        def set_dead(self, dead):
            self.dead = dead
        def set_aff(aff):
            self.aff = aff
        def set_physa(self, val):
            self.physa = val
        def set_physd(self, val):
            self.physd = val
        def set_maga(self, val):
            self.maga = val
        def set_magd(self, val):
            self.magd = val
        def set_stance(self, i, duration):
            self.stance[i] = duration
        def set_pattern(self, pattern):
            self.pattern = pattern
        def set_moves(self, i, move):
            self.move[i] = move
        def set_flavour(self, i, flavour):
            self.flavour[i] = flavour
        #useful functions
        def get_aff_mod(self, target, ele):
            #used in calc damage.
            #ele = affinity of the move
            aff = target.get_aff()
            #normal affinitty
            if ele == 0:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 0.75
                elif aff == 3:
                    mod = 1
                elif aff == 4:
                    mod = 1
                elif aff == 5:
                    mod = 1
                elif aff == 6:
                    mod = 1
                elif aff == 7:
                    mod = 1
                elif aff == 8:
                    mod = 0.75
            #heroic affinity
            elif ele == 1:
                if aff == 0:
                    mod = 0.75
                elif aff == 1:
                    mod = 0.5
                elif aff == 2:
                    mod = 1.5
                elif aff == 3:
                    mod = 0.75
                elif aff == 4:
                    mod = 1
                elif aff == 5:
                    mod = 1
                elif aff == 6:
                    mod = 1
                elif aff == 7:
                    mod = 1
                elif aff == 8:
                    mod = 0.75
            #vile affinity
            elif ele == 2:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 0.75
                elif aff == 2:
                    mod = 1.25
                elif aff == 3:
                    mod = 1.25
                elif aff == 4:
                    mod = 1.25
                elif aff == 5:
                    mod = 1
                elif aff == 6:
                    mod = 1.25
                elif aff == 7:
                    mod = 1.25
                elif aff == 8:
                    mod = 0.75
            #earth affinity
            elif ele == 3:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 1
                elif aff == 3:
                    mod = 0.75
                elif aff == 4:
                    mod = 1
                elif aff == 5:
                    mod = 1
                elif aff == 6:
                    mod = 1
                elif aff == 7:
                    mod = 1
                elif aff == 8:
                    mod = 1
            #ice affinity
            elif ele == 4:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 1
                elif aff == 3:
                    mod = 1
                elif aff == 4:
                    mod = 1.25
                elif aff == 5:
                    mod = 0.75
                elif aff == 6:
                    mod = 1.25
                elif aff == 7:
                    mod = 1
                elif aff == 8:
                    mod = 1
            #fire affinity
            elif ele == 5:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 1
                elif aff == 3:
                    mod = 0.5
                elif aff == 4:
                    mod = 1.25
                elif aff == 5:
                    mod = 0.75
                elif aff == 6:
                    mod = 0.5
                elif aff == 7:
                    mod = 1
                elif aff == 8:
                    mod = 1
            #water affinity
            elif ele == 6:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 1
                elif aff == 3:
                    mod = 1
                elif aff == 4:
                    mod = 0.75
                elif aff == 5:
                    mod = 1.25
                elif aff == 6:
                    mod = 0.75
                elif aff == 7:
                    mod = 1
                elif aff == 8:
                    mod = 1
            #lightning affinity
            elif ele == 7:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 0.75
                elif aff == 3:
                    mod = 0.5
                elif aff == 4:
                    mod = 0.75
                elif aff == 5:
                    mod = 1
                elif aff == 6:
                    mod = 1.25
                elif aff == 7:
                    mod = 0.75
                elif aff == 8:
                    mod = 1
            #metal affinity
            elif ele == 8:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 1
                elif aff == 3:
                    mod = 1.25
                elif aff == 4:
                    mod = 1
                elif aff == 5:
                    mod = 1
                elif aff == 6:
                    mod = 1
                elif aff == 7:
                    mod = 1
                elif aff == 8:
                    mod = 1
            return mod

        def calc_damage(self, target, type, ele):
            #self: dealer of the damage
            #target: recipient of the damage, unit child obj
            #type: physical or magical damage
            #element: affinity of the damage

            aff_mod = self.get_aff_mod(target, ele)
            variance = randint(230, 255) / 255 #10 % damage variance

            if type == 1:
                attack = self.get_physa()
                defense = target.get_physd()
            else:
                attack = self.get_maga()
                defense = target.get_magd()

            #look through damage mod stances. they affect the stats.
            #[...]

            dmg = int(((2*attack - defense) / defense) * (20 + self.get_lvl()) * aff_mod * variance)
            return dmg

        def take_damage(self, target, damage):
            #self: unit taking the damage
            #damage: an int.

            #look damage cancelling stances
            #kindara
            #shatter point
            #[...]

            target.set_hp(max(self.get_hp()-damage, 0))

            if target.get_hp() == 0:
                target.set_able(0)
                target.set_ooa(0)
                #target.set_icon("unconcious")

        def use_move(self, cmove, x, y):
            #legend:
            # cmove = the chosen move. e.g. hit. it's an object.


            #method:
            # 1. calc xc, yc
            # 2. call highlight, pass in xc, yc, targeting type. Return = a list of all the affected spots.
            # 3. for each spot on the list, find if there's a unit hiding out there. if there is, apply affect.

            #coordinate fun stuff, pass it into highlight


            #pos(275 + 125*el[i].get_point().get_x(), 5 + 65*el[i].get_point().get_y())

            #return a list of all squares affected by the highlight.
            if cmove.get_iff() == 0:
                nl = renpy.call_in_new_context("call_e_highlight", self) #choose targeted area on enemy board
                #nl = renpy.show_screen("enemy_highlight", self, cmove.get_type())
                #TODO ^when i show this screen, it hides all the other screens :(


            elif cmove.get_iff() == 1:
                nl = renpy.call_screen("ally_highlight", self) #choose targeted area on allied board
            elif cmove.get_iff() == 2:
                pass
                #nl = [...] #create the list yourself. #set area on enemy board
            elif cmove.get_iff() == 3:
                pass
                #nl = [...] #create the list yourself. ##choose targeted area on allied board

            #for each affected square,
                #if there is a unit on it,
                    #apply move effect: i.e. cmove.effect(affected unit)



            #renpy.call_screen("attack_highlight")

            #use move where it showed up

            #move the unit around according to the move's requirement.
            self.set_able(0)



    class unit_mc(unit):
        def __init__(self):
            self.name = "Mc"
            self.point = point(0, 0) #instance of point class. coordinates for unit's position.
            self.icon = "icon_mc" #picture
            self.deployable = 1 #whether you can field them
            self.able = 1 #let's the unit act each round
            self.lvl = 0 #unit's level
            self.exp = 0 #the unit's exp for leveling up
            self.evo = 0 #whether the unit is in evo mode
            self.foc = 0 #determines weighting in the level up and some moves learned.

            self.hpmax = 100 #max hp
            self.hp = 100 #current hp
            self.dodgemax = 10 #max dodge
            self.dodge = 10 #percent chance to dodge attacks.
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 0 #affinity. for super effective and stuff.
            self.physa = 100 #physical attack
            self.physd = 100 #physical defense
            self.maga = 100 #magical attack
            self.magd = 100 #magical defense
            self.stance = [0] * 5 #times however many stances there are

            #moves:
            self.pattern = 3 #3/3
            self.move1 = hit()
            self.move2 = hit()
            self.move3 = hit()
            self.move4 = jumpkick()
            self.move5 = jumpkick()
            self.move6 = jumpkick()
            self.move7 = evo_storm()
            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]

        def level_up():
            #every 10th? levelup, character must choose a 'focus.'
            #focus influences moves stat increases and moves learned.
            #stats up
            #learn moves depending on level and focus
            pass

        def move1():
            pass

    class unit_yve(unit):
        def __init__(self):
            self.name = "Yve"
            self.point = point(0, 0) #instance of point class. coordinates for unit's position.
            self.icon = "icon_yve" #picture
            self.deployable = 1 #whether you can field them
            self.able = 1 #let's the unit act each round
            self.lvl = 0
            self.exp = 0 #the unit's exp for leveling up
            self.evo = 0 #whether the unit is in evo mode

            self.hpmax = 150 #max hp
            self.hp = 150 #current hp
            self.dodgemax = 15 #max dodge
            self.dodge = 15 #percent chance to dodge attacks.
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 4 #affinity. for super effective and stuff.
            self.physa = 120 #physical attack
            self.physd = 120 #physical defense
            self.maga = 80 #magical attack
            self.magd = 100 #magical defense
            self.stance = [0] * 5 #times however many stances there are

            #moves:
            self.pattern = 2 #2/4
            self.move1 = hit()
            self.move2 = hit()
            self.move3 = hit()
            self.move4 = hit()
            self.move5 = jumpkick()
            self.move6 = jumpkick()
            self.move7 = evo_storm()
            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]

        def level_up():
            #increase a whole bunch of silly stats.
            pass

        def move1():
            pass

    class unit_grunt(unit):
        def __init__(self, lvl, name, x, y):
            self.name = name
            self.point = point(x, y) #instance of point class. coordinates for unit's position.
            self.icon = "icon_grunt" #picture
            self.deployable = 1 #whether you can field them
            self.able = 1 #let's the unit act each round
            self.lvl = lvl
            self.exp = 0 #the unit's exp for leveling up
            self.evo = 0 #whether the unit is in evo mode

            self.hpmax = 60 + (5 *lvl) #max hp
            self.hp = 60 + (5 *lvl)#current hp
            self.dodgemax = 10 + int(lvl/5)#max dodge
            self.dodge = 10 + int(lvl/5)#percent chance to dodge attacks.
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 0 # affinity. for super effective and stuff.
            self.physa = 80 + (3 *lvl)#physical attack
            self.physd = 80 + (3 *lvl)#physical defense
            self.maga = 80 + (1 *lvl)#magical attack
            self.magd = 80 + (2 *lvl)#magical defense
            self.stance = [0] * 5 #times however many stances there are

            #moves:
            self.pattern = 3 #3/3
            self.flavour = [""] * 7 # 7 of them. is set when moves are selected

        def move1():
            pass


    #initialize all the pilots objects at game launch.
    #mc_d = unit_mc(unit)
    #nai_d = unit()
    #yve_d = unit_yve(unit)



label call_e_highlight(unit):

    $nl = renpy.call_screen("enemy_highlight", unit)

    #$renpy.call_screen("enemy_highlight", unit)

    #call screen enemy_highlight(unit)


#etc





































##eof

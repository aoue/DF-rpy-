#--LEGEND--#
#self.name = "vile grunt"
#self.point = point(0, 0) #instance of point class. coordinates for unit's position.
#self.icon = "icon_grunt" #picture
#self.deployable = 1 #whether you can field them
#self.able = 1 #let's the unit act each round
#self.stamina = 50 #basically mana. some recovers each round.
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
#self.move1 = fyaya #its a child object of the move class
#self.moves = [] #its a list of every move.

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

    #--- BATTLE ---
    class map():
        def __init__(self):
            #self.map = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]] #the grid

            self.map = [[None]*5, [None]*5] #the grid. fill a certain spot with a unit child object

            self.ul = [] #unit list

        #getters
        def get_map(self):
            return self.map
        def get_ul(self):
            return self.ul

        def set_unit(self, unit):
            #take in unit. plop it in ul

            #or I could

            pass

        def move_unit(self, unit):
            #move the unit from one map place to another
            pass

        def kill_unit(self, unit):
            #enemy unit ooa. remove
            pass

        def search_allymap(self, row, col):
            unit = self.get_allymap().index(row, col)
            #
            #look through allymap and find any unit that matches these coordinates
            #For lists, there's also the index method that can sometimes be useful if you want to know where a certain element is in the list:
            #list.index(int) -> returns

            return unit

        def search_enemymap(self, row, col):
            #look through allymap and find any unit that matches these coordinates
            unit = self.get_enemymap().index(row, col)

            return unit


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
            self.allymap = map()
            self.enemymap = map()

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
                self.set_pable(self.calc_pable())
                self.set_eable(self.calc_eable())
                self.set_ableleft(self.get_pable() + self.get_eable())

                while self.get_ableleft() > 0: #for one round

                    if self.get_pable() > 0: #player turn
                        self.set_phase("act")
                        self.refresh_visuals()

                        self.player_turn()

                        self.set_pable(self.calc_pable())
                        self.refresh_visuals()

                    self.set_ableleft(self.get_pable() + self.get_eable())

                    if self.get_eable() > 0: #enemy turn
                        self.set_phase("vile")
                        self.refresh_visuals()

                        self.enemy_turn()

                        #self.set_eable(self.calc_eable())
                        self.set_eable(self.get_eable()-1) #Temporary measure until you do enemy's turn
                        self.refresh_visuals()

                    self.set_ableleft(self.get_pable() + self.get_eable())

                if self.is_battle_over() == 1:
                    return

                self.set_rounds(max(self.get_rounds()-1,0)) #proceed to next round
                self.reset_round() #reset for next round

            self.postbattle_settings()


    #--- POINT ---
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
        def get_tuple(self):
            return (self.x, self.y)


    #--- MOVES ---
    class move():
        def __init__(self):
            self.flavour = "{i}hit hard and fast{/i}"
            self.title = "move"
            self.rank = 0 #can be 0, 1, or 2. determines where the move can be used
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 0 #0 for needs total clear path. 1 for needs only clear destination.
            self.stamina_drain = 0 #the amount of stamina the unit loses using this move
            self.able_drain = 0 #the amount of able the unit loses using this move
            self.power = 0 #affects damage

        #getters
        def get_flavour(self):
            return self.flavour
        def get_title(self):
            return self.title
        def get_rank(self):
            return self.rank
        def get_type(self):
            return self.type
        def get_iff(self):
            return self.iff
        def get_clearance(self):
            return self.clearance
        def get_clearance_type(self):
            return self.clearance_type
        def get_stamina_drain(self):
            return self.stamina_drain
        def get_able_drain(self):
            return self.able_drain
        def get_power(self):
            return self.power

        #useful functions
        def translate(self, unit):
            #we do not have to worry about borders, because the player cannot click on the move if its out of bounds.
            unit.set_point(unit.get_point().get_x() + self.get_clearance()[0], unit.get_point().get_y() + self.get_clearance()[1])
        def drain(self, unit):
            unit.set_stamina(max(unit.get_stamina()-self.get_stamina_drain(), 0))
            unit.set_able(max(unit.get_able()-self.get_able_drain(), 0))

    class hit(move):
        def __init__(self):
            self.flavour = "{i}A hit, hard and fast.{/i}"
            self.title = "Hit"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 0
            self.stamina_drain = 15
            self.able_drain = 1
            self.power = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square

            #moves cost stamina and able
            self.drain(unit)

            self.translate(unit)

            #for each affected unit:
            #get total. split damage by total.
            #deal split damage to each of them.

    class jumpkick(move):
        def __init__(self):
            self.flavour = "{i}Fly in from the back.{/i}"
            self.title = "Jump Kick"
            self.rank = 2
            self.type = 2
            self.iff = 0
            self.clearance = (0,-2)
            self.clearance_type = 1
            self.stamina_drain = 20
            self.able_drain = 2
            self.power = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            self.drain(unit)

            self.translate(unit)

    class evo_storm(move):
        def __init__(self):
            self.flavour = "{i}Storm on the horizon.{/i}"
            self.title = "Storm"
            self.rank = 0
            self.type = 1
            self.iff = 2
            self.clearance = (0,0)
            self.clearance_type = 0
            self.stamina_drain = 0
            self.able_drain = 0
            self.power = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            pass


    #--- UNITS ---
    class unit:
        #constructor:
        def __init__(self):
            self.name = "Default Entity"
            self.point = point(0,0) #instance of point class. coordinates for unit's position.
            self.icon = "mechicon_mc" #picture
            self.deployable = 1 #whether you can field them
            self.ablemax = 2 #max of able
            self.able = 2 #let's the unit act each round
            self.staminamax = 50 #stamina max
            self.stamina = 50 #basically mana. some recovers each round.
            self.restam = 15 #the amount of stamina that recovers each round
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
        def get_ablemax(self):
            return self.ablemax
        def get_able(self):
            return self.able
        def get_staminamax(self):
            return self.staminamax
        def get_stamina(self):
            return self.stamina
        def get_restam(self):
            return self.restam
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
        def set_ablemax(self, ablemax):
            self.ablemax = ablemax
        def set_able(self, able):
            self.able = able
        def set_staminamax(self, staminamax):
            self.staminamax = staminamax
        def set_stamina(self, stamina):
            self.stamina = stamina
        def set_restam(self, restam):
            self.restam = restam
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
        def walk(self, grid):
            #move 1 square in any direction. respect borders, respect collision.
            #this means i need to pass in the grid, yeah

            unit.set_able(unit.get_able()-1)


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

            #there is no way to differentiate the power of a certain move. add that in to the damage formula.

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

            dmg = int(((2*attack - defense) / defense) * (20 + self.get_lvl()) * aff_mod * variance) #* move power or something
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

        def use_move(self, cmove, x, y, battle):
            #legend:
            # cmove = the chosen move. e.g. hit. it's an object.

            #pos(275 + 125*el[i].get_point().get_x(), 5 + 65*el[i].get_point().get_y())

            #returns a tuple of the (row, column) that was clicked.
            if cmove.get_iff() == 0:
                sq = renpy.invoke_in_new_context(call_highlight_e, self, cmove, battle)
            elif cmove.get_iff() == 1:
                sq = renpy.invoke_in_new_context(call_highlight_a, self, cmove, battle)

            elif cmove.get_iff() == 2:
                pass
                #nl = [...] #create the targeted spots yourself. it's a set area on enemy board.
            elif cmove.get_iff() == 3:
                pass
                #nl = [...] #create the targeted spots yourself. it affects a set area on allied board.


            #for each affected square,
                #if there is a unit on it,
                    #apply move effect: i.e. cmove.effect(affected unit)

            #this function must handle:
            # -able drain
            # -stamina drain
            # -finding targets
            # -dealing damage to targets
            cmove.exert(self, sq, battle)


    class unit_mc(unit):
        def __init__(self):
            self.name = "Mc"
            self.point = point(0, 0) #instance of point class. coordinates for unit's position.
            self.icon = "icon_mc" #picture
            self.deployable = 1 #whether you can field them
            self.ablemax = 1 #
            self.able = 1 #let's the unit act each round
            self.staminamax = 50
            self.stamina = 50 #basically mana. some recovers each round.
            self.restam = 10
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
            self.ablemax = 2
            self.able = 2 #let's the unit act each round
            self.staminamax = 60
            self.stamina = 60 #basically mana. some recovers each round.
            self.restam = 12
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
            self.ablemax = 1
            self.able = 1 #let's the unit act each round
            self.staminamax = 50
            self.stamina = 50 #basically mana. some recovers each round.
            self.restam = 5
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

    def call_highlight_e(unit, cmove, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("enemy_highlight", unit, cmove)
        return sq
    def call_highlight_a(unit, cmove, battle):
        battle.refresh_visuals()
        sq = renpy.call_screen("allied_highlight", unit, cmove)
        return sq







































##eof

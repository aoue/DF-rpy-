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

        def calc_damage(self, target, type, ele, power):
            #self: dealer of the damage
            #target: recipient of the damage, unit child obj
            #type: whether move does phys (0) or mag (1) damage
            #element: move's element (affinity). 0 through 8
            #power = move's power. int

            #there is no way to differentiate the power of a certain move. add that in to the damage formula.

            aff_mod = self.get_aff_mod(target, ele)
            spread = random.randint(216, 255) /255.0

            if type == 1:
                attack = self.get_physa()
                defense = target.get_physd()
            else:
                attack = self.get_maga()
                defense = target.get_magd()

            #look through damage mod stances. they influence attack or defense (or other stats maybe, idk)

            damage = int(((2*attack - defense) / defense) * (power + (2 * self.get_lvl())) * aff_mod * spread) #* move power or something

            #REWORK THE FORMULA
            #samples:
            #low level: hp = 150. a = 130. d = 110. dmg ~ 30-40
            #med level: hp = 500. a = 220. d = 200. dmg ~ 80-120
            #high level: hp = 1500. a = 300. d = 290. dmg ~200-400

            #low power move: 20
            #med power move: 75
            #high power move: 150




            return damage

        def take_damage(self, damage):
            #self: unit taking the damage
            #damage: an int.

            #look through damage cancelling stances
            #kindara
            #shatter point
            #[...]

            self.set_hp(max(self.get_hp()-damage, 0))

            if self.get_hp() == 0:
                self.set_able(0)
                self.set_ooa(1)
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

            #the move handles the rest
            cmove.exert(self, sq, battle)


    class unit_mc(unit):
        def __init__(self):
            self.name = "Mc"
            self.point = point(-1, -1) #instance of point class. coordinates for unit's position.
            self.icon = "icon_mc" #picture
            self.deployable = 1 #whether you can field them
            self.ablemax = 1 #
            self.able = 1 #let's the unit act each round
            self.staminamax = 50
            self.stamina = 50 #basically mana. some recovers each round.
            self.restam = 5
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
            #increase the following stats by an amount depending on:
            # -the level. e.g. if lvl mod 2 = 0, do something. if lvl mod 5 = 0, do another.
            # -the unit's focus (or no focus)

            #always increase:
            #lvl
            #hpmax and hp
            #physa
            #physd
            #maga
            #magd
            #dodgemax and dodge
            #staminamax and stamina
            #restam
            #ablemax and able

            #check if the unit learns a new move. depends of the level and on the unit's focus (or no focus)
            #check if the unit's level mod 10 == 0. if yes, call change focus screen.

            pass


    class unit_yve(unit):
        def __init__(self):
            self.name = "Yve"
            self.point = point(-1, -1) #instance of point class. coordinates for unit's position.
            self.icon = "icon_yve" #picture
            self.deployable = 1 #whether you can field them
            self.ablemax = 1
            self.able = 1 #let's the unit act each round
            self.staminamax = 50
            self.stamina = 50 #basically mana. some recovers each round.
            self.restam = 5
            self.lvl = 0
            self.exp = 0 #the unit's exp for leveling up
            self.evo = 0 #whether the unit is in evo mode

            self.hpmax = 120 #max hp
            self.hp = 120 #current hp
            self.dodgemax = 15 #max dodge
            self.dodge = 15 #percent chance to dodge attacks.
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 4 #affinity. for super effective and stuff.
            self.physa = 110 #physical attack
            self.physd = 100 #physical defense
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
            #see above
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

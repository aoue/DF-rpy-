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
#self.hitmax = 10 #for hitting dodgers
#self.hit = 10 #for hitting dodgers
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

            self.stance = stances() #unit's status effects
            self.hpmax = 0 #max hp
            self.hp = 0 #current hp
            self.dodgemax = 30 #max dodge. always a bit higher than dodge.
            self.dodge = 30 #percent chance to dodge attacks.
            self.hitmax = 20 #subtract from eenmy's dodge
            self.hit = 20 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 0 # #affinity. 9 total.
            self.physa = 0 #physical attack
            self.physd = 0 #physical defense
            self.maga = 0 #magical attack
            self.magd = 0 #magical defense

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
        def get_stance(self):
            return self.stance
        def get_hpmax(self):
            return self.hpmax
        def get_hp(self):
            return self.hp
        def get_dodgemax(self):
            return self.dodgemax
        def get_dodge(self):
            return self.dodge
        def get_hitmax(self):
            return self.hitmax
        def get_hit(self):
            return self.hit
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
        def set_hitmax(self, hitmax):
            self.hitmax = hitmax
        def set_hit(self, hit):
            self.hit = hit
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
        def level_up(self):
            #if self.get_exp() > constant * self.get_lvl():
            #   level up!
            pass

        def walk(self, battle):
            #move to an open, adjacent square. ends the unit's turn.
            sq = renpy.invoke_in_new_context(call_highlight_walk, self, battle) #tuple

            battle.get_allymap().remove_unit(self)

            self.get_point().set_x(sq[0])
            self.get_point().set_y(sq[1])
            battle.get_allymap().place_unit(self)
            self.set_able(self.get_able()-1)

        def wait(self):
            self.set_able(0)
            self.set_stamina(min(self.get_stamina()+20, self.get_staminamax()))

        def defend(self):
            #the unit must have full able points to do this.
            #regen some stam and set both physd and magd stances up.
            self.set_able(0)
            self.set_stamina(min(self.get_stamina()+20, self.get_staminamax()))

        def get_aff_mod(self, target, ele):
            #used in calc damage.
            #ele = affinity of the attacking move
            #aff = affinity of the defender

            aff = target.get_aff()
            #normal affinitty
            if ele == 0:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 0.75
                elif aff == 2:
                    mod = 0.75
                elif aff == 3:
                    mod = 0.5
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
                    mod = 0.5
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
                    mod = 1.25
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
                    mod = 1.5
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
            #electric affinity
            elif ele == 7:
                if aff == 0:
                    mod = 1
                elif aff == 1:
                    mod = 1
                elif aff == 2:
                    mod = 1
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
                    mod = 0.75
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
                    mod = 0.75
            return mod

        def calc_damage(self, target, cmove):
            #self: dealer of the damage
            #target: recipient of the damage, unit child obj
            #type: whether move does phys (0) or mag (1) damage
            #element: move's element (affinity). 0 through 8
            #power = move's power. int

            #see if we're dealing with physical or magical damage.
            if cmove.get_damage_type() == 0: #returns a tuple
                astats = self.get_stance().get_attacking_stances(self.get_physa(), self.get_hit(), cmove.get_damage_type())
                dstats = target.get_stance().get_defending_stances(target.get_physd(), target.get_dodge(), cmove.get_damage_type())
            else:
                astats = self.get_stance().get_attacking_stances(self.get_maga(), self.get_hit(), cmove.get_damage_type())
                dstats = target.get_stance().get_defending_stances(target.get_magd(), target.get_dodge(), cmove.get_damage_type())


            #even if the unit has kindara on, it will still try to dodge.
            if random.randint(1, 100) < max(dstats[1] - (astats[1] + cmove.get_hit()), 0):
                return 0 #dodge successful. returns 0 damage

            aff_mod = self.get_aff_mod(target, cmove.get_element())
            spread = random.randint(216, 255) /255.0

            #actual damage calculation
            damage = max(int(((2*astats[0] - 1.5*dstats[0]) / dstats[0]) * (cmove.get_power() + (2 * self.get_lvl())) * aff_mod * spread), 0)

            return damage

        def take_damage(self, dealer, damage):
            #self: unit taking the damage
            #dealer: unit dealing the damage
            #damage: an int.

            #look through stances: the order is important.
            if self.get_stance().get_exhausted() > 0: #if exhausted, take 1.2x damage
                damage = damage * 1.2

            if self.get_stance().get_kindara() > 0: #hit enemy will full damage. take no damage.
                self.get_stance().set_kindara(self.get_kindara() - 1)
                dealer.set_hp(max(self.get_hp()-damage, 0))
                return

            if self.get_stance().get_shatter() > 0: #if not put ooa, take no damage.
                if self.get_hp() - damage > 0:
                    self.get_stance().set_shatter(self.get_stance().get_shatter()-1)
                    return


            #unit takes damage
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



    #playable units (in order of appearance)
    class unit_yve(unit):
        def __init__(self):
            self.name = "Yve"
            self.point = point(-1, -1) #instance of point class. coordinates for unit's position.
            self.icon = "icon_yve" #picture
            self.deployable = 1 #whether you can field them
            self.ablemax = 1
            self.able = 10 #let's the unit act each round
            self.staminamax = 60
            self.stamina = 60 #basically mana. some recovers each round.
            self.restam = 10
            self.lvl = 0
            self.exp = 0 #the unit's exp for leveling up
            self.evo = 0 #whether the unit is in evo mode

            self.stance = stances() #unit's status effects
            self.hpmax = 130 #max hp
            self.hp = 130 #current hp
            self.dodgemax = 15 #max dodge
            self.dodge = 15 #percent chance to dodge attacks.
            self.hitmax = 5 #subtract from eenmy's dodge
            self.hit = 5 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 4 #affinity. for super effective and stuff.
            self.physa = 110 #physical attack
            self.physd = 100 #physical defense
            self.maga = 80 #magical attack
            self.magd = 100 #magical defense

            #moves:
            self.pattern = 2 #2/4
            self.move1 = hit()
            self.move2 = pirouette()
            self.move3 = hit()
            self.move4 = hit()
            self.move5 = skate()
            self.move6 = adrenaline() #adrenaline rush
            self.move7 = evo_storm()
            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]

        def level_up():
            #see above
            pass

    class unit_boy(unit):
        def __init__(self):
            self.name = "Boy"
            self.point = point(-1, -1) #instance of point class. coordinates for unit's position.
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

            self.stance = stances() #unit's status effects
            self.hpmax = 100 #max hp
            self.hp = 100 #current hp
            self.dodgemax = 10 #max dodge
            self.dodge = 10 #percent chance to dodge attacks.
            self.hitmax = 0 #subtract from eenmy's dodge
            self.hit = 0 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 0 #affinity. for super effective and stuff.
            self.physa = 100 #physical attack
            self.physd = 100 #physical defense
            self.maga = 100 #magical attack
            self.magd = 100 #magical defense

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



    #enemy units (in order of appearance)
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

            self.stance = stances() #unit's status effects
            self.hpmax = 60 + (5 *lvl) #max hp
            self.hp = 60 + (5 *lvl)#current hp
            self.dodgemax = 10 + int(lvl/5)#max dodge
            self.dodge = 10 + int(lvl/5)#percent chance to dodge attacks.
            self.hitmax = 0 #subtract from eenmy's dodge
            self.hit = 0 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 0 # affinity. for super effective and stuff.
            self.physa = 80 + (3 *lvl)#physical attack
            self.physd = 80 + (3 *lvl)#physical defense
            self.maga = 80 + (1 *lvl)#magical attack
            self.magd = 80 + (2 *lvl)#magical defense

            #moves:
            self.pattern = 3 #3/3
            self.flavour = [""] * 7 # 7 of them. is set when moves are selected

        def move1():
            pass




    #initialize all the units and helperss
    playerlist = []
    boy_d = unit_boy()
    yve_d = unit_yve()
    baddie = unit_grunt(0, "vile grunt", 2, 1)
    baddie2 = unit_grunt(0, "horrid grunt", 2, 2)































#eof

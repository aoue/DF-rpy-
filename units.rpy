#--------------------------------
#self.pattern #move slots
# i: front/back/wild
# 1: 4/2/1
# 2: 3/3/1
# 3: 2/4/1

#self.aff # more/less effective
# 0: normal
# 1: beast
# 2: ice
# 3: fire
# 4: lightning
# 5: earth
# 6: metal
# 7: vile
# 8: heroic
#--------------------------------

init -1 python:
    #--- POINT ---
    class Point():
        def __init__(self, x, y, (a,b)):
            self.x = x #x coordinate of top left
            self.y = y #y coordinate of top left
            self.gros = (a,b) #dimensions of the unit

        #setters
        def set_x(self, x):
            self.x = x
        def set_y(self, y):
            self.y = y

        #getters
        def get_x(self):
            return self.x
        def get_y(self):
            return self.y
        def get_gros(self):
            return self.gros
        def get_tuple(self):
            return (self.x, self.y)


    #--- UNITS ---
    class Unit:
        #constructor:
        def __init__(self):
            self.iff = 0 #which board damage/etc should be shown on. 0: ally, 1: enemy
            self.name = "Default Entity"
            self.point = Point(0,0, (1,1)) #instance of point class. coordinates for unit's position.
            self.face = "face_boy" #deploy picture
            self.face_h = "face_boy_hover" #deploy picture, hovered
            self.icon = "mechicon_mc" #picture
            self.pose = "yve_pose" #party picture. battle cut-in as well?
            self.deployable = 1 #whether you can field them
            self.ablemax = 2 #max of able
            self.able = 2 #let's the unit act each round
            self.staminamax = 50 #stamina max
            self.stamina = 50 #stamina. some recovers each round.
            self.energymax = 10 #mana. necessary for the best moves
            self.energy = 10 #does not recover each round.
            self.restam = 15 #the amount of stamina that recovers each round
            self.lvl = 0 #what level the unit's at.
            self.exp = 0 #the unit's exp for leveling up
            self.evo = 0 #whether the unit is in evo mode

            self.stance = Stances() #unit's status effects
            self.hpmax = 0 #max hp
            self.hp = 0 #current hp
            self.dodgemax = 30 #max dodge. always a bit higher than dodge.
            self.dodge = 30 #percent chance to dodge attacks.
            self.hit = 20 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.
            self.dead = 0 #dead. not a battle stat.

            self.aff = 0 # #affinity. 9 total.
            self.aff_name = "" #shown on party screen
            self.physa = 0 #physical attack
            self.physd = 0 #physical defense
            self.maga = 0 #magical attack
            self.magd = 0 #magical defense

            self.weapon = None #weapon
            self.armour = None #armour
            self.acc = None #accessory

            #moves:
            self.foc = 0 #int, means different things to different char.
            self.pattern = 3 #3/3
            self.move1 = None
            self.move2 = None
            self.move3 = None
            self.move4 = None
            self.move5 = None
            self.move6 = None
            self.move7 = None
            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]
            self.movelist = [] #all moves the unit has learned. used for equipping unequipping moves.
            self.passive = (0,0) #tuple of 2 class objects. [0] is the one of the unit's natural passive, [1] is a gear passive.
            self.passivelist = [] #it's a list of all the passives the unit knows by leveling up

        #actual getters - returns final value of the stat to simplify display and calculations
        def get_energymax_actual(self):
            return self.get_energymax() + self.get_weapon().get_energy() + self.get_armour().get_energy() + self.get_acc().get_energy()
        def get_hpmax_actual(self):
            return self.get_hpmax() + self.get_weapon().get_hp() + self.get_armour().get_hp() + self.get_acc().get_hp()
        def get_ablemax_actual(self):
            return self.get_ablemax() + self.get_weapon().get_able() + self.get_armour().get_able() + self.get_acc().get_able()
        def get_staminamax_actual(self):
            return self.get_staminamax() + self.get_weapon().get_stamina() + self.get_armour().get_stamina() + self.get_acc().get_stamina()
        def get_restam_actual(self):
            return self.get_restam() + self.get_weapon().get_restam() + self.get_armour().get_restam() + self.get_acc().get_restam()
        def get_physa_actual(self):
            return self.get_physa() + self.get_weapon().get_physa() + self.get_armour().get_physa() + self.get_acc().get_physa()
        def get_physd_actual(self):
            return self.get_physd() + self.get_weapon().get_physd() + self.get_armour().get_physd() + self.get_acc().get_physd()
        def get_maga_actual(self):
            return self.get_maga() + self.get_weapon().get_maga() + self.get_armour().get_maga() + self.get_acc().get_maga()
        def get_magd_actual(self):
            return self.get_magd() + self.get_weapon().get_magd() + self.get_armour().get_magd() + self.get_acc().get_magd()
        def get_hitmax_actual(self):
            return self.get_hit() + self.get_weapon().get_hit() + self.get_armour().get_hit() + self.get_acc().get_hit()
        def get_dodgemax_actual(self):
            return self.get_dodgemax() + self.get_weapon().get_dodge() + self.get_armour().get_dodge() + self.get_acc().get_dodge()


        #getters
        def get_passivelist(self):
            return self.passivelist
        def get_passive(self):
            return self.passive
        def get_aff_name(self):
            return self.aff_name
        def get_turn_over(self):
            return self.turn_over
        def get_iff(self):
            return self.iff
        def get_name(self):
            return self.name
        def get_point(self):
            return self.point
        def get_face(self):
            return self.face
        def get_face_h(self):
            return self.face_h
        def get_icon(self):
            return self.icon
        def get_pose(self):
            return self.pose
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
        def get_energymax(self):
            return self.energymax
        def get_energy(self):
            return self.energy
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
        def get_equip_types(self):
            return self.equip_types
        def get_weapon(self):
            return self.weapon
        def get_armour(self):
            return self.armour
        def get_acc(self):
            return self.acc
        def get_foc(self):
            return self.foc
        def get_pattern(self):
            return self.pattern
        def get_moves(self):
            return self.moves
        def get_movelist(self):
            return self.movelist
        def get_learnlist(self):
            return self.learnlist
        def get_flavour(self, i):
            return self.flavour[i]
        #setters
        def set_passive(self, x, passive):
            if x == 1: #intrinsic is being changed
                self.passive = (self.get_passive()[0], passive)
            else:
                self.passive = (passive, self.get_passive()[1])
        def set_turn_over(self, turn_over):
            self.turn_over = turn_over
        def set_name(self, name):
            self.name = name
        def set_point(self, x, y):
            self.point.set_x(x)
            self.point.set_y(y)
        def set_face(self, face):
            self.face = face
        def set_face_h(self, face_h):
            self.face_h = face_h
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
        def set_energymax(self, energymax):
            self.energymax = energymax
        def set_energy(self, energy):
            self.energy = energy
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
        def set_weapon(self, weapon):
            self.weapon = weapon
        def set_armour(self, armour):
            self.armour = armour
        def set_acc(self, acc):
            self.acc = acc
        def set_stance(self, i, duration):
            self.stance[i] = duration
        def set_focos(self, foc):
            self.foc = foc
        def set_pattern(self, pattern):
            self.pattern = pattern
        def set_flavour(self, i, flavour):
            self.flavour[i] = flavour
        #useful functions
        def get_next_level_exp(self):
            #returns the exp the unit needs to advance to the next level
            nextlvl = 100 + (20*self.get_lvl()) + (5*self.get_lvl()*self.get_lvl())
            return nextlvl
        def end_turn(self):
            self.set_turn_over(1)
            self.get_stance().end_turn(self)
        def gear_passives(self):
            if self.get_weapon() != None:
                self.get_weapon().use_passive()
            if self.get_armour() != None:
                self.get_armour().use_passive()
            if self.get_acc() != None:
                self.get_acc().use_passive()
        def post_battle(self):
            #after a battle in the dungeon crawler portion.
            if self.get_ooa() == 1:
                self.set_ooa(0)
                self.set_hp(1)
            elif self.get_hp() > self.get_hpmax_actual():
                self.set_hp(self.get_hpmax_actual())
            self.set_stamina(self.get_staminamax_actual())
            self.set_able(self.get_ablemax_actual())
            self.set_dodge(self.get_dodgemax_actual())
            self.set_deployable(1)
            self.get_stance().post_battle()
        def check_dead(self, battle, dealer):
            if self.get_hp() == 0:

                for p in self.get_passive(): #unit has been put ooa
                    if p.get_check() == 5:
                        p.exert(self)
                        return

                for p in dealer.get_passive(): #dealer has put unit ooa
                    if p.get_check() == 6:
                        p.exert(dealer)

                self.set_able(0)
                self.set_stamina(0)
                self.set_ooa(1)
                self.get_stance().post_battle()

                if self.get_iff() == 1:
                    battle.get_totalloot().append(self.get_loot())
                    battle.set_totalexp(battle.get_totalexp() + self.get_exp())
                    battle.get_enemymap().remove_unit(self)
                    battle.get_el().remove(self)
                else:
                    self.set_icon("dead_icon")

        def wait(self):
            self.set_stamina(int(min(self.get_stamina()+(0.25 * self.get_staminamax() * self.get_able()), self.get_staminamax())))
            self.set_able(0)
            self.set_turn_over(1)

        def get_aff_mod(self, ele):
            #used in calc damage.
            #ele = affinity of the attacking move
            #compare ele to defender's natural affinity
            #compare ele to defender's armour affinity
            #return the average
            aff_mod = (self.calc_aff(self.get_aff(), ele)) + (self.calc_aff(self.get_armour().get_aff(), ele))

            return aff_mod/2


        def calc_aff(self, aff, ele):
            #pass in defender's affinity (aff)
            #pass in move affinity (ele)
            #find the aff mod of these two, return it

            aff_list = [[ 1, 1, 1, 1, 1, 0.5, 0.5, 1, 0.5 ], #normal
            [ 1.5, 1, 1, 0.5, 1, 0.5, 0.5, 2, 1 ], #beast
            [ 1, 2, 0.5, 0.5, 1, 2, 2, 0.25, 1 ], #ice
            [ 1, 2, 2, 0, 1, 0.5, 0.5, 2, 0.5 ], #fire
            [ 1, 2, 1, 1, 0, 0, 3, 0.25, 1 ], #lightning
            [ 1, 1, 0.5, 1, 1, 1, 0.25, 0.25, 1 ], #earth
            [ 1, 0.5, 1, 0.5, 0.25, 2, 1, 1, 2 ] , #metal
            [ 2, 0.25, 2, 2, 2, 0.25, 0.25, 3, 3 ], #vile
            [ 1, 2, 1, 1, 1, 1, 1, 3, 0 ]] #heroic

            return aff_list[aff][ele] #<-- yes, pretty sure this is the right indexing order.


        def calc_heal(self, target, cmove):
            #self: dealer of the heals
            #target: recipient of the heals
            #cmove: healing move

            astats = self.get_maga_actual() * self.get_stance().get_maga()
            dstats = target.get_magd_actual() * target.get_stance().get_magd()

            spread = renpy.random.randint(230, 255) /255.0
            #spread = 1 #for testing buffs

            for p in self.get_passive():
                if p.get_check() == 2:
                    p.exert(self)


            heal = max((((astats + cmove.get_power()) / dstats) * cmove.get_power() * spread), 0)

            return int(heal)
        def take_heal(self, dealer, heal, showlist, maxes):
            #maxes: if 0, the heal cannot exceed unit's actual max health. if 1: it can.
            #check stances: i.e. reciprocal

            #any stances that do: take 2x heals, 0.5x heals, etc. need to be handled in here.

            for p in self.get_passive():
                if p.get_check() == 4:
                    p.exert(self)

            if maxes == 0:
                if self.get_hp() >= self.get_hpmax_actual():
                    showlist.append((self.get_point().get_x(), self.get_point().get_y(), -1, self.get_iff()))
                    return
                else:
                    self.set_hp(min(self.get_hp()+heal, self.get_hpmax_actual()))

            elif maxes == 1:
                self.set_hp(self.get_hp()+heal)
            else:
                self.set_hp(min(self.get_hp()+heal, self.get_hpmax_actual()))

            showlist.append((self.get_point().get_x(), self.get_point().get_y(), heal, self.get_iff()))

        def take_heal_oob(self, dealer, heal):
            for p in self.get_passive():
                if p.get_check() == 4:
                    p.exert(self)
            self.set_hp(min(self.get_hp()+heal, self.get_hpmax_actual()))

        def calc_damage(self, target, cmove):
            #self: dealer of the damage
            #target: recipient of the damage, unit child obj
            #type: whether move does phys (0) or mag (1) damage
            #element: move's element (affinity). 0 through 8
            #power = move's power. int

            #see if we're dealing with physical or magical damage. returns tuples of (attack, hit) , (defense, dodge)
            damage = 1.0

            for p in self.get_passive():
                if p.get_check() == 1:
                    p.exert(self, target)

            if cmove.get_damage_type() == 0: #physical damage
                atk = self.get_physa_actual() * self.get_stance().get_physa()
                dfs = target.get_physd_actual() * target.get_stance().get_physd()
                if target.get_stance().get_mtn() == 1:
                    damage = 0.5
            else: #magical damage
                atk = self.get_maga_actual() * self.get_stance().get_maga()
                dfs = target.get_magd_actual() * self.get_stance().get_magd()
                if target.get_stance().get_mtn() == 1:
                    target.get_stance().set_mtn(0)

            hit = max((self.get_hit() * self.get_stance().get_hit()) + cmove.get_hit() + 5, 5) #max(5, 5 + attacker's hit + move hit.)
            dodge = target.get_dodge() * target.get_stance().get_dodge()

            #the unit tries to dodge. success: decrease unit's dodge.
            if renpy.random.randint(1, 100) < max(dodge - hit, 0):

                if target.get_dodgemax_actual() > 0:
                    #target.set_dodge(max(target.get_dodge()-abs(self.get_hit()+cmove.get_hit()), 0))
                    target.set_dodge(int(max(target.get_dodge() - hit, 0))) #can only go down to 0


                return -1 #dodge successful. returns -1 damage


            if cmove.get_element == -1:
                aff_mod = target.get_aff_mod(self.get_weapon().get_aff())
            else:
                aff_mod = target.get_aff_mod(cmove.get_element())

            spread = round(renpy.random.uniform(0.9, 1.0), 2)

            #actual damage calculation
            damage = damage * ((atk) * (cmove.get_power() + self.get_lvl()) / (dfs)) * aff_mod * spread

            return int(damage)

        def take_damage(self, dealer, damage, showlist, battle, dot, duration):
            #self: unit taking the damage
            #dealer: unit dealing the damage
            #damage: an int.
            #showlist: for showing damage



            #any stances that do: take 2x damage, 0.5x damage, etc. need to be handled in here.

            #dodge does not regenerate when the unit is hit. (passives notwithstanding.)
            if damage == -1: #dodge
                showlist.append((self.get_point().get_x(), self.get_point().get_y(), "Dodge", self.get_iff()))
                return


            #call passive:
            for p in self.get_passive():
                if p.get_check() == 3:
                    workaround = [damage]
                    p.exert(self, battle, workaround)
                    damage = workaround[0]

            #look through stances: the order is important.
            if self.get_stance().get_exhausted() > 0: #if exhausted, take 1.2x damage
                damage = int(damage * 1.25)

            self.get_stance().move_dot(self, dot, duration)

            #unit takes damage
            showlist.append((self.get_point().get_x(), self.get_point().get_y(), damage, self.get_iff()))
            self.set_hp(max(self.get_hp()-damage, 0))
            self.check_dead(battle, dealer)

        def use_move(self, cmove, battle):
            #legend:
            # cmove = the chosen move. e.g. hit. it's an object.
            # battle = the battle instance we're fighting in.
            # sq = tuple (row, column) that is going to be clicked

            if cmove.get_iff() == 0:
                sq = renpy.invoke_in_new_context(call_highlight_e, self, cmove, battle) #click on enemy side
            elif cmove.get_iff() == 1:
                sq = renpy.invoke_in_new_context(call_highlight_a, self, cmove, battle) #click on ally side
            elif cmove.get_iff() == 2:
                pass
                #nl = [...] #create the targeted spots yourself. it's a set area on enemy board.
            elif cmove.get_iff() == 3:
                pass
                #nl = [...] #create the targeted spots yourself. it affects a set area on allied board.
            elif cmove.get_iff() == -1:
                #for walk only
                cmove.exert(self, battle)
                renpy.hide_screen("move_browse_b")
                return


            if 'sq' in locals():
                if sq == -1:
                    return
                else:
                    #the move handles the rest
                    cmove.exert(self, sq, battle)
                    renpy.hide_screen("move_browse_b")
                    self.end_turn()
            else:
                cmove.exert(self, battle)
                renpy.hide_screen("move_browse_b")
                self.end_turn()


    #playable units (in order)
    class Unit_yve(Unit):
        def __init__(self):
            self.iff = 0
            self.name = "Yvette"
            self.point = Point(-1, -1, (1,1))
            self.face = "face_yve"
            self.face_h = "face_yve_hover"
            self.icon = "icon_yve"
            self.pose = "yve_pose"
            self.deployable = 1

            self.equip_types = [[3,2,1], [1], [1]]
            self.weapon = Folding_spear()
            self.armour = Folding_armour()
            self.acc = Yve_headband()

            self.energymax = 15
            self.energy = self.get_energymax_actual()
            self.restam = 10
            self.lvl = 0
            self.exp = 0
            self.evo = 0

            self.turn_over = 0

            self.stance = Stances()
            self.hpmax = 130
            self.ablemax = 1
            self.staminamax = 60
            self.dodgemax = 15
            self.hit = 5

            self.able = self.get_ablemax_actual()
            self.hp = self.get_hpmax_actual()
            self.stamina = self.get_staminamax_actual()
            self.dodge = self.get_dodgemax_actual()

            self.ooa = 0
            self.dead = 0
            self.aff = 2
            self.aff_name = "Ice"
            self.physa = 70
            self.physd = 70
            self.maga = 50
            self.magd = 50

            self.foc = Focus_fighter()
            self.pattern = 1 #4/2/1
            self.move1 = Spear()
            self.move2 = Pierce()
            self.move3 = Defend()
            self.move4 = Walk()
            self.move5 = Adrenaline()
            self.move6 = None
            self.move7 = None

            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]
            self.movelist = []
            self.passive = (Adrenaline_Rush_1(), Passive())
            self.passivelist = [Adrenaline_Rush_1()]

    class Unit_friday(Unit):
        def __init__(self):
            self.iff = 0
            self.name = "Friday"
            self.point = Point(-1, -1, (1,1))
            self.face = "face_friday"
            self.face_h = "face_friday_hover"
            self.icon = "icon_friday"
            self.pose = "pose_friday"
            self.deployable = 1

            self.equip_types = self.equip_types = [[2,1], [4], [3]]
            self.weapon = N1_carmina()
            self.armour = Folding_armour()
            self.acc = Plain_headband()

            self.energymax = 10
            self.energy = self.get_energymax_actual()
            self.restam = 10
            self.lvl = 0
            self.exp = 0
            self.evo = 0

            self.turn_over = 0

            self.stance = Stances()
            self.hpmax = 90
            self.ablemax = 1
            self.staminamax = 50
            self.dodgemax = 5
            self.hit = 0

            self.able = self.get_ablemax_actual()
            self.hp = self.get_hpmax_actual()
            self.stamina = self.get_staminamax_actual()
            self.dodge = self.get_dodgemax_actual()

            self.ooa = 0
            self.dead = 0
            self.aff = 0
            self.aff_name = "Normal"
            self.physa = 50
            self.physd = 60
            self.maga = 50
            self.magd = 60

            self.foc = Focus_assistant()
            self.pattern = 2 #2/4/1
            self.move1 = Gun()
            self.move2 = Beat_up()
            self.move3 = Defend()
            self.move4 = First_aid()
            self.move5 = Walk()
            self.move6 = None
            self.move7 = None

            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]
            self.movelist = []
            self.passive = (Flexibility_1(), Passive())
            self.passivelist = [Flexibility_1()]


    #guest units
    class Unit_federal(Unit):
        def __init__(self):
            self.iff = 0
            self.name = "Federal"
            self.point = Point(-1, -1, (1,1))
            self.face = "face_federal"
            self.face_h = "face_federal_hover"
            self.icon = "icon_federal"
            self.pose = "yve_federal"
            self.deployable = 1

            self.equip_types = [[3,2,1], [3], [0]]
            self.weapon = Regulation_sword()
            self.armour = Regulation_armour()
            self.acc = None_accessory()

            self.energymax = 10
            self.energy = self.get_energymax_actual()
            self.restam = 10
            self.lvl = 0
            self.exp = 0
            self.evo = 0

            self.turn_over = 0

            self.stance = Stances()
            self.hpmax = 110
            self.ablemax = 1
            self.staminamax = 50
            self.dodgemax = 10
            self.hit = 5

            self.able = self.get_ablemax_actual()
            self.hp = self.get_hpmax_actual()
            self.stamina = self.get_staminamax_actual()
            self.dodge = self.get_dodgemax_actual()

            self.ooa = 0
            self.dead = 0
            self.aff = 0
            self.aff_name = "Normal"
            self.physa = 60
            self.physd = 65
            self.maga = 50
            self.magd = 60

            self.foc = Focus_fighter()
            self.pattern = 3 #3/3/1
            self.move1 = Sword()
            self.move2 = Flourish()
            self.move3 = Form6()
            self.move4 = Rally()
            self.move5 = Defend()
            self.move6 = Walk()
            self.move7 = None

            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]
            self.movelist = []
            self.passive = (Stick_Together_1(), Passive())
            self.passivelist = []
    class Unit_aide(Unit):
        def __init__(self):
            self.iff = 0
            self.name = "Aide"
            self.point = Point(-1, -1, (1,1))
            self.face = "face_federal"
            self.face_h = "face_federal_hover"
            self.icon = "icon_federal_aide"
            self.pose = "yve_federal"
            self.deployable = 1

            self.equip_types = [[3,2,1], [3], [0]]
            self.weapon = Regulation_sword()
            self.armour = Regulation_armour()
            self.acc = None_accessory()

            self.energymax = 10
            self.energy = self.get_energymax_actual()
            self.restam = 10
            self.lvl = 0
            self.exp = 0
            self.evo = 0

            self.turn_over = 0

            self.stance = Stances()
            self.hpmax = 100
            self.ablemax = 1
            self.staminamax = 50
            self.dodgemax = 10
            self.hit = 5

            self.able = self.get_ablemax_actual()
            self.hp = self.get_hpmax_actual()
            self.stamina = self.get_staminamax_actual()
            self.dodge = self.get_dodgemax_actual()

            self.ooa = 0
            self.dead = 0
            self.aff = 0
            self.aff_name = "Normal"
            self.physa = 55
            self.physd = 60
            self.maga = 55
            self.magd = 50

            self.foc = Focus_fighter()
            self.pattern = 3 #3/3/1
            self.move1 = Form6()
            self.move2 = Walk()
            self.move3 = Defend()
            self.move4 = Gun()
            self.move5 = Suppress()
            self.move6 = First_aid()
            self.move7 = None

            self.moves = [self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,self.move7]
            self.movelist = []
            self.passive = (Stick_Together_1(), Passive())
            self.passivelist = []





























#eof

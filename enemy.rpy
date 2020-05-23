
init python:
    #--- Enemies
    class enemy_unit(unit):
        #they need some things the player units don't need
        #and don't need some things the player units do need

        def __init__(self, lvl, name, x, y):
            self.iff = 1 #all enemy units have iff of 1.
            self.name = name
            self.point = point(x, y) #instance of point class. coordinates for unit's position.
            self.icon = "icon_grunt" #picture
            self.ablemax = 1
            self.able = 1 #lets the unit act each round
            self.staminamax = 50
            self.stamina = 50 #basically mana. some recovers each round.
            self.restam = 5
            self.lvl = lvl
            self.evo = 0 #whether the unit is in evo mode

            self.stance = stances() #unit's status effects
            self.hpmax = 80
            self.hp = 80 #current hp
            self.dodgemax = 0
            self.dodge = 0 #percent chance to dodge attacks.
            self.hitmax = 0
            self.hit = 0 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.

            self.aff = 0 # affinity. for super effective and stuff.
            self.physa = 80 #physical attack
            self.physd = 80 #physical defense
            self.maga = 80 #magical attack
            self.magd = 80 #magical defense

            #gear
            self.weapon = None
            self.armour = None
            self.acc = None

            #moves:
            #self.pattern = 3 #3/3 enemies don't need pattern
            moves = []

            #thinking:
            self.pridef = 0 #default of innate initiative value. normal is 2 or 3 or so.
            self.pri = 0 #innate initiative value. normal is 2 or 3 or so. inc/dec each time the unit acts.
            self.pri_type = 0 #0: decreases pri after acting, 1: increases pri after acting. 2: doesn't change
            self.pri_change = 0 #0: dec pri after acting, 1: inc pri after acting.
            self.concern = 0 #when hp/hpmax < concern, unit priority is inc/dec
            self.concern_change = 0 #when concern affects pri, this is by how much. + or -
            self.healer = 0 #0: not healer, 1: is healer
            self.healer_change = 0 #when there are hurt units, increase pri by this much
            self.buffer = 0 #0: not buffer, 1: is buffer
            self.buffer_change = 0 #when there are unbuffed units, increase pri by this much
            self.is_buffed = 0 #0: in not buffed. 1: is buffed.
            self.discipline = (0,0) #range that affects unit's priority. the smaller the range, the less random. left side should be negative, right side should be positive. should be symmetric.

        #getters
        def get_pridef(self):
            return self.pridef
        def get_pri(self):
            return self.pri
        def get_pri_type(self):
            return self.pri_type
        def get_pri_change(self):
            return self.pri_change
        def get_concern(self):
            return self.concern
        def get_concern_change(self):
            return self.concern_change
        def get_healer(self):
            return self.healer
        def get_healer_change(self):
            return self.healer_change
        def get_buffer(self):
            return self.buffer
        def get_buffer_change(self):
            return self.buffer_change
        def get_is_buffed(self):
            return self.is_buffed
        def get_discipline(self):
            return self.discipline

        #setters
        def set_pri(self, pri):
            self.pri = pri
        #useful functions
        def is_concerned(self):
            if float(self.get_hp()) / float(self.get_hpmax()) < self.get_concern():
                return 1
            return 0
        def fatigue(self):
            return float(self.get_stamina()) / float(self.get_staminamax())
        def calc_priority(self, el):
            #unit's innate pri value
            pri = self.get_pri()

            #modify unit's pri value based on when they act
            if self.get_pri_type() == 0:
                if self.get_pri() <= -5 or self.get_pri() >= 15:
                    self.set_pri(self.get_pridef())
                else:
                    self.set_pri(self.get_pri() - self.get_pri_change())
            elif self.get_pri_type() == 1:
                self.set_pri(self.get_pri() + self.get_pri_change())

            #healer logic
            if self.get_healer() == 1:
                for unit in el:
                    if unit == self:
                        pass
                    elif unit.get_hp()/self.get_hpmax() < unit.get_concern():
                        pri += self.get_healer_change()
            #buffer logic
            if self.get_buffer() == 1:
                for unit in el:
                    if unit == self:
                        pass
                    elif unit.get_is_buffed == 0:
                        pri += self.get_buffer_change()

            #is the unit concerned?
            if self.is_concerned() == 1:
                pri += self.get_concern_change()

            #random priority calculated based on discipline
            pri += random.randint(self.get_discipline()[0], self.get_discipline()[1])

            return pri
        def take_turn(self, el, pl, battle):
            #decide what to do from the moves the unit knows.
            #renpy.say(None, "{}, reporting in".format(self.get_name()))
            renpy.pause(2.0)

            #buff (if unit in el is not buffed)
            #TODO worry about it later

            if self.fatigue() > 0.7:
                chosen = self.select_move(3, battle) #heavy
            elif self.fatigue() > 0.4:
                chosen = self.select_move(2, battle) #medium
            elif self.fatigue() > 0.2:
                chosen = self.select_move(1, battle) #light
            else:
                if self.get_able() == self.get_ablemax():
                    self.defend()
                else:
                    self.wait()
                return

            #if the unit tried to use a move, but was blocked. clearance was not obtained.
            #-translate the unit towards the chosen position
            if chosen == -1:
                if self.get_able() == self.get_ablemax():
                    self.defend()
                else:
                    self.wait()
            elif chosen in range(0, 5):
                if chosen > self.get_point().get_x():
                    self.shift(battle, 1)
                else:
                    self.shift(battle, -1)

            else:
                chosen.exert(self, pl, el, battle)

        def shift(self, battle, direction):
            #direction: move one to the right (1), or to the left (-1)
            battle.get_enemymap().remove_unit(self)

            #move unit
            self.set_point(self.get_point().get_x() + direction, self.get_point().get_y())

            #place unit  in map
            battle.get_enemymap().place_unit(self)
            self.set_able(self.get_able()-1)


        def select_move(self, effort, battle):
            #we've decided to use a heavy move. Now we need to determine which one.
            #effort: heavy(1), medium(2), light(3)
            x = random.randint(1, 99)
            #chosen = None

            if self.get_point().get_y() > 1: #we're in front
                for move in self.get_moves():
                    if move.get_rank() == 2 and move.get_weight() > x and move.get_effort() <= effort:
                        if move.e_check_clearance((self.get_point().get_x(), self.get_point().get_y()), battle) == 1:
                            chosen = move
                        else: #if we're blocked, we go for a walk.
                            spotlist = []
                            for i in range(self.get_point().get_x()+1, 5): #every spot to the right. if a spot is blocked, break.
                                if battle.get_enemymap().search_map((i, self.get_point().get_y())) != None:
                                    break
                                elif move.e_check_clearance((i, self.get_point().get_y()), battle) == 1:
                                        spotlist.append(i)

                            for i in range(0, self.get_point().get_x()): #every spot to the left. if a spot is blocked, break.
                                if battle.get_enemymap().search_map((self.get_point().get_x()-(i+1), self.get_point().get_y())) != None:
                                    break
                                elif move.e_check_clearance((self.get_point().get_x()-(i+1), self.get_point().get_y()), battle) == 1:
                                        spotlist.append(i)

                            #now we have each possible good spot. find the one closest to our unit's x
                            min = 4
                            if not spotlist:
                                chosen = -1

                            else:
                                for spot in spotlist:
                                    dif = self.get_point().get_x() - spot
                                    if abs(dif) <= min:
                                        dif = min
                                        chosen = spot


            else: #we're in the back
                for move in self.get_moves():
                    if move.get_rank() == 1 and move.get_weight() > x and move.get_effort() <= effort:
                        if move.e_check_clearance((self.get_point().get_x(), self.get_point().get_y()), battle) == 1:
                            chosen = move
                        else: #if we're blocked, we go for a walk.
                            spotlist = []
                            for i in range(self.get_point().get_x()+1, 5): #every spot to the right. if a spot is blocked, break.
                                if battle.get_enemymap().search_map((i, self.get_point().get_y())) != None:
                                    break
                                elif move.e_check_clearance((i, self.get_point().get_y()), battle) == 1:
                                        spotlist.append(i)

                            for i in range(0, self.get_point().get_x()): #every spot to the right. if a spot is blocked, break.
                                if battle.get_enemymap().search_map((self.get_point().get_x()-(i+1), self.get_point().get_y())) != None:
                                    break
                                elif move.e_check_clearance((self.get_point().get_x()-(i+1), self.get_point().get_y()), battle) == 1:
                                        spotlist.append(i)

                            #now we have each possible good spot. find the one closest to our unit's x
                            min = 4
                            if not spotlist:
                                chosen = -1

                            else:
                                for spot in spotlist:
                                    dif = self.get_point().get_x() - spot
                                    if abs(dif) <= min:
                                        dif = min
                                        chosen = spot


            return chosen


    #enemy units (in order of appearance)
    class unit_grunt(enemy_unit):
        def __init__(self, lvl, name, x, y):
            self.iff = 1
            self.name = name
            self.point = point(x, y) #instance of point class. coordinates for unit's position.
            self.icon = "icon_grunt" #picture
            self.ablemax = 1
            self.able = 1 #lets the unit act each round
            self.staminamax = 60
            self.stamina = 60 #basically mana. some recovers each round.
            self.restam = 5
            self.lvl = lvl
            self.evo = 0 #whether the unit is in evo mode

            self.stance = stances() #unit's status effects
            self.hpmax = 80
            self.hp = 80 #current hp
            self.dodgemax = 0
            self.dodge = 0 #percent chance to dodge attacks.
            self.hitmax = 0
            self.hit = 0 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.

            self.aff = 0 # affinity. for super effective and stuff.
            self.physa = 80 #physical attack
            self.physd = 80 #physical defense
            self.maga = 70 #magical attack
            self.magd = 70 #magical defense

            #gear
            self.weapon = None
            self.armour = None
            self.acc = None

            #moves:
            self.moves = [e_claw()]

            #thinking:
            self.pridef = 1 #default of innate initiative value. normal is 2 or 3 or so.
            self.pri = 1 #innate initiative value. normal is 2 or 3 or so. inc/dec each time the unit acts.
            self.pri_type = 0 #0: decreases pri after acting, 1: increases pri after acting
            self.pri_change = 1 #amount pri is inc/dec after acting
            self.concern = 0.5 #when hp/hpmax < concern, unit priority is inc/dec
            self.concern_change = -2 #when concern affects pri, this is by how much. + or -
            self.healer = 0 #0: not healer, 1: is healer
            self.healer_change = 0 #when there are hurt units, increase pri by this much
            self.buffer = 0 #0: not buffer, 1: is buffer
            self.buffer_change = 0 #when there are unbuffed units, increase pri by this much
            self.is_buffed = 0 #0: in not buffed. 1: is buffed.
            self.discipline = (-2,2) #range that affects unit's priority. the smaller the range, the less random.

    class unit_jowler(enemy_unit):
        def __init__(self, lvl, name, x, y):
            self.iff = 1
            self.name = name
            self.point = point(x, y) #instance of point class. coordinates for unit's position.
            self.icon = "icon_jowler" #picture
            self.ablemax = 1
            self.able = 1 #lets the unit act each round
            self.staminamax = 60
            self.stamina = 60 #basically mana. some recovers each round.
            self.restam = 5
            self.lvl = lvl
            self.evo = 0 #whether the unit is in evo mode

            self.stance = stances() #unit's status effects
            self.hpmax = 60
            self.hp = 60 #current hp
            self.dodgemax = 0
            self.dodge = 0 #percent chance to dodge attacks.
            self.hitmax = 0
            self.hit = 0 #subtract from enemy's dodge
            self.ooa = 0 #out of action. defeated.

            self.aff = 0 # affinity. for super effective and stuff.
            self.physa = 60 #physical attack
            self.physd = 55 #physical defense
            self.maga = 40 #magical attack
            self.magd = 50 #magical defense

            #gear
            self.weapon = beast_claw()
            self.armour = beast_skin()
            self.acc = None

            #moves:
            self.moves = [e_claw(), e_jaws(), e_rush(), e_howl()]

            #thinking:
            self.pridef = 3 #default of innate initiative value. normal is 2 or 3 or so.
            self.pri = 3 #innate initiative value. normal is 2 or 3 or so. inc/dec each time the unit acts.
            self.pri_type = 1 #0: decreases pri after acting, 1: increases pri after acting
            self.pri_change = 2 #amount pri is inc/dec after acting
            self.concern = 0.6 #when hp/hpmax < concern, unit priority is inc/dec
            self.concern_change = 3 #when concern affects pri, this is by how much. + or -
            self.healer = 0 #0: not healer, 1: is healer
            self.healer_change = 0 #when there are hurt units, increase pri by this much
            self.buffer = 0 #0: not buffer, 1: is buffer
            self.buffer_change = 0 #when there are unbuffed units, increase pri by this much
            self.is_buffed = 0 #0: in not buffed. 1: is buffed.
            self.discipline = (-5,5) #range that affects unit's priority. the smaller the range, the less random.





#eof

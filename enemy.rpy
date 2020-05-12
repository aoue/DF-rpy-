
init python:
    #--- Enemies
    class enemy_unit(unit):
        #they need some things the player units don't need
        #and don't need some things the player units do need

        def __init__(self, lvl, name, x, y):
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

            #moves:
            self.pattern = 3 #3/3

            #thinking:
            self.pridef = 0 #default of innate initiative value. normal is 2 or 3 or so.
            self.pri = 0 #innate initiative value. normal is 2 or 3 or so. inc/dec each time the unit acts.
            self.pri_type = 0 #0: decreases pri after acting, 1: increases pri after acting
            self.pri_change = 0 #0: dec pri after acting, 1: inc pri after acting.
            self.concern = 0 #when hp/hpmax < concern, unit priority is inc/dec
            self.concern_change = 0 #when concern affects pri, this is by how much. + or -
            self.healer = 0 #0: not healer, 1: is healer
            self.buffer = 0 #0: not buffer, 1: is buffer
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
        def get_buffer(self):
            return self.buffer
        def get_discipline(self):
            return self.discipline

        #setters
        def set_pri(self, pri):
            self.pri = pri

        #useful functions
        def calc_priority(self, el):
            #unit's innate pri value
            pri = self.get_pri()

            #modify unit's pri value.
            #decrease
            if self.get_pri_type() == 0:
                if self.get_pri() <= -5 or self.get_pri() >= 15:
                    self.set_pri(self.get_pridef())
                else:
                    self.set_pri(self.get_pri() - self.get_pri_change())
            #increase
            else:
                self.set_pri(self.get_pri() + self.get_pri_change())

            #is healer and injured allies: +++
            #is healer and uninjured allies: ---
            if self.get_healer() == 1:
                pass

            #is buffer and unbuffed allies: ++
            #is buffer and buffed allies: --

            #is hurt enough to be concerned (hp/hpmax <= concern)
            if self.get_hp()/self.get_hpmax() < self.get_concern():
                pri += self.get_concern_change()


            #random priority calculated based on discipline
            pri += random.randint(self.get_discipline()[0], self.get_discipline()[1])


            return pri

        def take_turn(self, el, pl):
            #decide what to do from the moves the unit knows.

            #heal (if friends are hurt)
            #buff (if friends are debuffed)
            #light attack (if stam is low)
            #med attack (if stam is high)
            #heavy attack (if enemy is weak)
            #aoe (if nice target)
            #defend (else)

            self.set_able(0)



    #enemy units (in order of appearance)
    class unit_grunt(enemy_unit):
        def __init__(self, lvl, name, x, y):
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

            #moves:
            self.pattern = 3 #3/3

            #thinking:
            self.pridef = 0 #default of innate initiative value. normal is 2 or 3 or so.
            self.pri = 0 #innate initiative value. normal is 2 or 3 or so. inc/dec each time the unit acts.
            self.pri_type = 0 #0: decreases pri after acting, 1: increases pri after acting
            self.pri_change = 0 #0: dec pri after acting, 1: inc pri after acting.
            self.concern = 0 #when hp/hpmax < concern, unit priority is inc/dec
            self.concern_change = 0 #when concern affects pri, this is by how much. + or -
            self.healer = 0 #0: not healer, 1: is healer
            self.buffer = 0 #0: not buffer, 1: is buffer
            self.discipline = (-2, 2) #range that affects unit's priority. the smaller the range, the less random. left side should be negative, right side should be positive. should be symmetric.


        def move1():
            pass





#eof

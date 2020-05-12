


init -2 python:

    #--- STANCES ---
    class stances():
        def __init__(self):
            #keeps track of what stances are applied to the unit.
            #the value of the stance is equal to its duration. decrement by 1 at the end of round
            #refer to spreadsheet for precise effects

            #format
            #self.stance = (duration, multiplier)

            #special
            self.ad = (0, 1) #adrenaline
            self.bl = (0, 1) #bloodhungry
            self.sh = (0, 1) #shatter point
            self.ki = (0, 1) #kindara
            self.ex = (0, 1) #exhausted
            self.mr = (0, 1) #martyr

            #special helpers
            self.ad_loss = 0 #hp that the unit gained when going into adrenaline.

            #stat changes
            self.hp_re = (0, 1) #hp regen
            self.st_re = (0, 1) #stamina regen
            self.do = (0, 1) #dodge
            self.hi = (0, 1) #hit
            self.pa = (0, 1) #phys a
            self.pd = (0, 1) #phys d
            self.ma = (0, 1) #mag a
            self.md = (0, 1) #mag d

            #DOTs
            self.be = (0, 1) #bleeding

        #getters
        def get_adrenaline(self):
            return self.ad
        def get_bloodhungry(self):
            return self.bl
        def get_shatter(self):
            return self.sh
        def get_kindara(self):
            return self.ki
        def get_exhausted(self):
            return self.ex
        def get_martyr(self):
            return self.mr
        def get_ad_loss(self):
            self.ad_loss
        def get_hp_regen(self):
            return self.hp_re
        def get_st_regen(self):
            return self.st_re
        def get_dodge(self):
            return self.do
        def get_hit(self):
            return self.hi
        def get_physa(self):
            return self.pa
        def get_physd(self):
            return self.pd
        def get_maga(self):
            return self.ma
        def get_magd(self):
            return self.md
        def get_bleeding(self):
            return self.be

        #setters
        def set_adrenaline(self, x, y):
            self.ad = (x, y)
        def set_bloodhungry(self, x, y):
            self.bl = (x, y)
        def set_shatter(self, x, y):
            self.sh = (x, y)
        def set_kindara(self, x, y):
            self.ki = (x, y)
        def set_exhausted(self, x, y):
            self.ex = (x, y)
        def set_martyr(self, x, y):
            self.mr = (x, y)
        def set_ad_loss(self, x):
            self.ad_loss = x
        def set_hp_regen(self, x, y):
            self.hp_re = (x, y)
        def set_st_regen(self, x, y):
            self.st_re = (x, y)
        def set_dodge(self, x, y):
            self.do = (x, y)
        def set_hit(self, x, y):
            self.hi = (x, y)
        def set_physa(self, x, y):
            self.pa = (x, y)
        def set_physd(self, x, y):
            self.pd = (x, y)
        def set_maga(self, x, y):
            self.ma = (x, y)
        def set_magd(self, x, y):
            self.md = (x, y)
        def set_bleeding(self, x, y):
            self.be = (x, y)

        #useful functions
        def enter_adrenaline(self, unit):
            #call this to enter the unit into adrenaline state.

            #-set ad_loss equal to the hp gain
            self.set_ad_loss(int(unit.get_hp() + (unit.get_hpmax()*0.5) + (5*unit.get_lvl())))

            #-increase current hp by (1.5*max hp + 5*lvl)
            unit.set_hp(self.get_ad_loss())

            #-increase hit by 1.25 or something
            self.set_hit(5, self.get_hit()[1] + 0.25)

            #-increase physa by 1.25 or something
            self.set_physa(5, self.get_physa()[1] + 0.15)


        def get_attacking_stances(self, attack, hit, type):
            #attack = unit's attack
            #hit = unit's hit
            #type = move's type of damage (phys/mag)

            if type == 0:
                #phys damage
                if self.get_physa()[0] > 0:
                    attack = attack * self.get_physa()[1]
            else:
                #mag damage
                if self.get_maga()[0] > 0:
                    attack = attack * self.get_maga()[1]

            if self.get_hit()[0] > 0:
                hit = hit * self.get_hit()[1]

            return attack, hit

        def get_defending_stances(self, defense, dodge, type):
            #defense = target's defense
            #dodge = target's dodge
            #type = move's type of damage (phys/mag)

            if type == 0:
                #phys damage
                if self.get_physd()[0] > 0:
                    defense = defense * self.get_physd()[1]
            else:
                #mag damage
                if self.get_magd()[0] > 0:
                    defense = defense * self.get_magd()[1]

            if self.get_dodge()[0] > 0:
                dodge = dodge * self.get_dodge()[1]

            return defense, dodge

        def new_round(self, unit):
            #check:
            #hp regen/dots.

            if self.get_hp_regen()[0] > 0:
                unit.set_hp(int(min(unit.get_hp() + (unit.get_hpmax()*self.get_hp_regen[1]), unit.get_hpmax())))

            if self.get_bleeding()[0] > 0:
                unit.set_hp(int(min(unit.get_hp() - (unit.get_hpmax()*self.get_bleeding[1]), unit.get_hpmax())))


            #apply hp regen

            #stamina regen. first, calc it:
            st_regen = unit.get_restam()

            if self.get_st_regen()[0] > 0:

                st_regen = st_regen * self.get_st_regen()[1]

            if self.get_exhausted()[0] == 1:

                st_regen = st_regen * self.get_exhausted()[1]

            #apply stamina regen
            unit.set_stamina(int(min(unit.get_stamina() + st_regen, unit.get_staminamax())))


            #-check if still exhausted. unit will no longer be exhausted if their stamina reaches a quarter of their max? that's what we're going with for now, anyway.
            if self.get_exhausted()[0] == 1:
                if unit.get_stamina() > (unit.get_staminamax() / 4):
                    self.set_exhausted(0, 0)

            #-check if still under adrenaline. unit will no longer be under adrenaline if enough time has passed.
            if self.get_adrenaline()[0] == 0 and unit.get_hp() > unit.get_hpmax():
                unit.set_hp(max(unit.get_hpmax(), unit.get_hpmax() - self.get_ad_loss()))

            self.dec_stances()

        def dec_stances(self):
            #decrease some stances by one. call this at the end of the round
            self.set_adrenaline(max(self.get_adrenaline()[0] - 1, 0), self.get_adrenaline()[1])
            self.set_bloodhungry(max(self.get_bloodhungry()[0] - 1, 0), self.get_bloodhungry()[1])
            self.set_martyr(max(self.get_martyr()[0] - 1, 0), self.get_martyr()[1])
            self.set_hp_regen(max(self.get_hp_regen()[0] - 1, 0), self.get_hp_regen()[1])
            self.set_st_regen(max(self.get_st_regen()[0] - 1, 0), self.get_st_regen()[1])
            self.set_dodge(max(self.get_dodge()[0] - 1, 0), self.get_dodge()[1])
            self.set_hit(max(self.get_hit()[0] - 1, 0), self.get_hit()[1])
            self.set_physa(max(self.get_physa()[0] - 1, 0), self.get_physa()[1])
            self.set_physd(max(self.get_physd()[0] - 1, 0), self.get_physd()[1])
            self.set_maga(max(self.get_maga()[0] - 1, 0), self.get_maga()[1])
            self.set_magd(max(self.get_magd()[0] - 1, 0), self.get_magd()[1])





















#eof

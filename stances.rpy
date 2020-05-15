


init -2 python:

    #--- STANCES ---
    class stances():
        def __init__(self):
            #keeps track of what stances are applied to the unit.
            #the value of the stance is equal to its duration. decrement by 1 at the end of round
            #refer to spreadsheet for precise effects

            #format
            #self.stance = (duration, multiplier)

            #special - these are trackers. int=duration
            self.ad = -1 #adrenaline
            self.rally = -1 #rally
            self.defend = -1 #defend
            self.ex = 0 #exhausted
            self.ki = 0 #kindara
            self.sh = 0 #shatter point

            #self.re = 0 #reciprocal. if a foe attacks you, they heal equal to the damage. if an ally heals you, they take damage equal to the heal.

            #DOTs
            self.be = -1 #bleeding

            #self.bl = 0 #bloodhungry
            #self.mr = 0 #martyr

            #special helpers
            self.ad_loss = 0 #hp that the unit gained when going into adrenaline.

            #stat changes - these are modifiers. float=multiplier
            self.hp_re = 1.0 #hp regen
            self.st_re = 1.0 #stamina regen
            self.do = 1.0 #dodge
            self.hi = 1.0 #hit
            self.pa = 1.0 #phys a
            self.pd = 1.0 #phys d
            self.ma = 1.0 #mag a
            self.md = 1.0 #mag d

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
            return self.ad_loss
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
        def get_rally(self):
            return self.rally
        def get_defend(self):
            return self.defend

        #setters
        def set_adrenaline(self, x):
            self.ad = x
        def set_bloodhungry(self, x):
            self.bl = x
        def set_shatter(self, x):
            self.sh = x
        def set_kindara(self, x):
            self.ki = x
        def set_exhausted(self, x):
            self.ex = x
        def set_martyr(self, x):
            self.mr = x
        def set_ad_loss(self, x):
            self.ad_loss = x
        def set_hp_regen(self, x):
            self.hp_re = x
        def set_st_regen(self, x):
            self.st_re = x
        def set_dodge(self, x):
            self.do = x
        def set_hit(self, x):
            self.hi = x
        def set_physa(self, x):
            self.pa = x
        def set_physd(self, x):
            self.pd = x
        def set_maga(self, x):
            self.ma = x
        def set_magd(self, x):
            self.md = x
        def set_bleeding(self, x):
            self.be = x
        def set_rally(self, x):
            self.rally = x
        def set_defend(self, x):
            self.defend = x

        #useful functions
        def get_attacking_stances(self, attack, hit, type):
            #attack = unit's attack
            #hit = unit's hit
            #type = move's type of damage (phys/mag)

            if type == 0:
                #phys damage
                attack = attack * self.get_physa()
            else:
                #mag damage
                attack = attack * self.get_maga()

            hit = hit * self.get_hit()

            return attack, hit

        def get_defending_stances(self, defense, dodge, type):
            #defense = target's defense
            #dodge = target's dodge
            #type = move's type of damage (phys/mag)

            if type == 0:
                #phys damage
                defense = defense * self.get_physd()
            else:
                #mag damage
                defense = defense * self.get_magd()


            dodge = dodge * self.get_dodge()

            return defense, dodge

        def new_round(self, unit):
            #check:
            #hp regen/dots.

            ##-- for this: check if a 'hp regen' tracker is on. if it is, then check self.get_hp_regen() for the modifier
            #if self.get_hp_regen()[0] > 0:
            #    unit.set_hp(int(min(unit.get_hp() + (unit.get_hpmax()*self.get_hp_regen[1]), unit.get_hpmax())))

            #if self.get_bleeding()[0] > 0:
            #    unit.set_hp(int(min(unit.get_hp() - (unit.get_hpmax()*self.get_bleeding[1]), unit.get_hpmax())))


            #stamina regen. first, calc it:
            st_regen = unit.get_restam()

            #for this: check if a 'stamina regen' tracker is on. if it is, then check self.get_st_regen() for the modifier
            #if self.get_st_regen()[0] > 0:
            #    st_regen = st_regen * self.get_st_regen()[1]

            #if self.get_exhausted()[0] == 1:
            #    st_regen = st_regen * self.get_exhausted()[1]

            #apply stamina regen
            unit.set_stamina(int(min(unit.get_stamina() + st_regen, unit.get_staminamax())))

            #-check if still exhausted. unit will no longer be exhausted if their stamina reaches a quarter of their max? that's what we're going with for now, anyway.
            if self.get_exhausted() == 1:
                if unit.get_stamina() > (unit.get_staminamax() / 4):
                    self.set_exhausted(0)

            #check if still under the effect of various stances. if the unit is not, then exit stance.
            if self.get_adrenaline() == 0:
                self.exit_adrenaline(unit)

            if self.get_rally() == 0:
                self.exit_rally()

            if self.get_defend() == 0:
                self.exit_defend()

            self.dec_stances()

        def dec_stances(self):
            #decrease (some) tracking stances by one. call this at the end of /start of new round
            self.set_adrenaline(max(self.get_adrenaline() - 1, -1))
            self.set_rally(max(self.get_rally() - 1, -1))
            self.set_bleeding(max(self.get_bleeding() - 1, -1))
            self.set_defend(max(self.get_defend() - 1, -1))

        #enter/exit stance pairs
        def enter_adrenaline(self, unit):
            #call this to enter the unit into adrenaline state.

            #-set ad_loss equal to the hp gain
            self.set_ad_loss(int(unit.get_hp() + (unit.get_hpmax()*0.5) + (10*unit.get_lvl())))

            #-increase current hp by (1.5*max hp + 5*lvl)
            unit.set_hp(self.get_ad_loss())

            #-increase hit mod by .25
            self.set_hit(self.get_hit() + 0.25)

            #-increase physa mod by .15
            self.set_physa(self.get_physa() + 0.15)
            
        def exit_adrenaline(self, unit):
            #call this to exit the unit from adrenaline state

            #if above max health thanks to adrenaline hp buff, remove hp buff.
            if unit.get_hp() > unit.get_hpmax():
                unit.set_hp(max(unit.get_hpmax(), unit.get_hp() - self.get_ad_loss()))

            #-decrease hit mod by .25 or something
            self.set_hit(self.get_hit() - 0.25)

            #-decrease physa mod by .15 or something
            self.set_physa(self.get_physa() - 0.15)

        def enter_rally(self):
            #call to enter unit into rally state

            #hit mod up by .25
            self.set_hit(self.get_hit() + 0.25)

            #physa mod up by .1
            self.set_physa(self.get_physa() + 0.1)
        def exit_rally(self):
            #call to exit unit from rally state

            #hit mod down by .25
            self.set_hit(self.get_hit() - 0.25)

            #physa mod down by .1
            self.set_physa(self.get_physa() - 0.1)

        def enter_bleeding(self):
            pass
        def exit_bleeding(self):
            self.set_bleeding(-1)

        def enter_defend(self):
            self.set_defend(0)

            self.set_physd(self.get_physd() + 0.2)
            self.set_magd(self.get_magd() + 0.2)
        def exit_defend(self):
            self.set_physd(self.get_physd() - 0.2)
            self.set_magd(self.get_magd() - 0.2)























#eof

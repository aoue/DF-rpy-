


init python:

    #--- STANCES ---
    class stances():
        def __init__(self):
            #keeps track of what stances are applied to the unit.
            #the value of the stance is equal to its duration. decrement by 1 at the end of round
            #refer to spreadsheet for precise effects

            #special
            self.ad = 0 #adrenaline
            self.bl = 0 #bloodhungry
            self.sh = 0 #shatter point
            self.ki = 0 #kindara
            self.ex = 0 #exhausted
            self.mr = 0 #martyr

            #stat changes
            self.hp_re = 0 #hp regen
            self.st_re = 0 #stamina regen
            self.do = 0 #dodge
            self.hi = 0 #hit
            self.pa = 0 #phys a
            self.pd = 0 #phys d
            self.ma = 0 #mag a
            self.md = 0 #mag d

            #DOTs
            self.be = 0 #bleeding

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
        def get_hp_regen(self):
            return self.hp_re
        def get_st_regen(self):
            return self.st_re
        def get_dodge(self):
            return self
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
        def set_hp_regen(self, x):
            self.hp_re = x
        def set_st_regen(self, x):
            self.st_re = x
        def set_dodge(self, x):
            self = x
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

        #useful functions
        def get_attacking_stances(self, attack, hit, type):
            #attack = unit's attack
            #hit = unit's hit
            #type = move's type of damage (phys/mag)

            if type == 0:
                #phys damage
                if self.get_physa() > 0:
                    attack = attack * 1.5
            else:
                #mag damage
                if self.get_maga() > 0:
                    attack = attack * 1.5

            if self.get_hit() > 0:
                hit = hit * 1.5

            return attack, hit

        def get_defending_stances(self, defense, dodge, type):
            #call before the unit is attacked. call on the target's behalf.

            if type == 0:
                #phys damage
                if self.get_physd() > 0:
                    defense = defense * 1.5
            else:
                #mag damage
                if self.get_magd() > 0:
                    defense = defense * 1.5

            if self.get_dodge() > 0:
                dodge = dodge * 1.5

            return defense, dodge

        def new_round(self, unit):
            #check:


            #hp regen/dots. first calc it.
            hp_regen = 0

            if self.get_hp_regen() > 0:
                hp_regen += 0.1

            if self.get_bleeding() > 0:
                hp_regen -= 0.1

            #apply hp regen
            unit.set_hp(int(min(unit.get_hp() + (unit.get_hpmax()*hp_regen), unit.get_hpmax())))

            #stamina regen. first, calc it:
            st_regen = unit.get_restam()

            if self.get_st_regen() > 0: #if stam regen up applied, then regen *= 1.5
                st_regen = int(st_regen * 1.5)

            if self.get_exhausted() == 1: #if exhausted applied, then regen *= 0.5
                st_regen = int(st_regen * 0.5)

            #apply stamina regen
            unit.set_stamina(int(min(unit.get_stamina() + (unit.get_restam()*st_regen), unit.get_staminamax())))


            #-check if still exhausted. unit will no longer be exhausted if their stamina reaches a quarter of their max?
            if self.get_exhausted() == 1:
                if unit.get_stamina() > (unit.get_staminamax() / 4):
                    self.set_exhausted(0)


            #decrease some stances by one.
            self.set_adrenaline(max(self.get_adrenaline() - 1), 0)
            self.set_bloodhungry(max(self.get_bloodhungry() - 1), 0)
            self.set_martyr(max(self.get_martyr() - 1), 0)
            self.set_hp_regen(max(self.get_hp_regen() - 1), 0)
            self.set_st_regen(max(self.get_st_regen() - 1), 0)
            self.set_dodge(max(self.get_dodge() - 1), 0)
            self.set_hit(max(self.get_hit() - 1), 0)
            self.set_physa(max(self.get_physa() - 1), 0)
            self.set_physd(max(self.get_physd() - 1), 0)
            self.set_maga(max(self.get_maga() - 1), 0)
            self.set_magd(max(self.get_magd() - 1), 0)





















#eof



#this is assigned to a unit's passive variable.

#passive abilities. they are checked at different times during a round.
#    -at round start. check every unit's passive.
#    -when an attack takes place, check the passive of the attacker and of the defender(s)
#    -same, but for heals.
#    -at round end.
#a unit can have only one passive equipped. (add to party screen). they can choose their passive from any passives their own move set and their gear.
#when doing a passive check, each do_passive function has a check. also, you call do_passive on the unit. the do_passive function calls a function that is a variable, which must be assigned before battle.
#the check:
#    -the tick marker has to be equal to the passive's tick marker. this makes sure the passive only goes into action at the right time.
#tick markers (when the passive is exerted):
# round start (0)           --> battle.round_start
# unit attacks (1)          --> unit.calc_damage
# unit heals (2)            --> unit.calc_heal
# unit is attacked (3)      --> unit.take_damage
# unit is healed (4)        --> unit.take_heal/unit.take_heal_oob
# unit is put ooa (5)       --> unit.check_dead
# unit kills (6)            --> unit.check_dead (dealer)

#example
init python:

    class Passive():
        def __init__(self):
            self.check = -1 # 0 through 7. determines when the passive should be called.
            self.flavour = "No passive equipped" #so the player knows what the passive does when equipping it.
            self.title = "None" #so the player can identify the passive by its name.
            self.charges = 0 #how many times the passive can trigger. only relevant for some.

        #getters
        def get_charges(self):
            return self.charges
        def get_check(self):
            return self.check
        def get_flavour(self):
            return self.flavour
        def get_title(self):
            return self.title
        #setters
        def set_charges(self, x):
            self.charges = x

    #--- Adrenaline Rush ---#
    #type = 6
    #I: extend by 1 turn
    #II: extend by 2 turns
    #III: reset to full duration
    class Adrenaline_Rush_1(Passive):
        #when the unit attacks and kills, extend the length of the adrenaline status by 1 turn.
        def __init__(self):
            self.check = 6
            self.flavour = "When putting an enemy out of action, if {i}adrenaline{/i} status is active, extend its duration by 1 round."
            self.title = "Adrenaline Rush I"

        def exert(self, unit):
            #called in check dead
            if unit.get_stance().get_adrenaline() > 0:
                unit.get_stance().set_adrenaline(unit.get_stance().get_adrenaline()+1)


    #bloodhungry or something. on kill, regain some able. some stam? it's another passive for Payton.

    #--- Flexibility ---#
    #type = 3
    #I: regain 1/10 of max dodge
    #II: regain 1/5 of max dodge
    #III: regain 1/2 of lost dodge
    class Flexibility_1(Passive):
        #when hit, regain 10% of max dodge.
        def __init__(self):
            self.check = 3
            self.flavour = "When hit, regain 1/10 of max dodge."
            self.title = "Flexibility I"

        def exert(self, unit, battle, damage):
            #called in take_damage. when unit is hit.
            unit.set_dodge(int(min(unit.get_dodge() + unit.get_dodgemax_actual() / 10, unit.get_dodgemax_actual())))


    #--- Stick Together ---#
    #type = 3
    #I: take 0.90x dmg
    #II: take 0.85x dmg
    #III: take 0.80x dmg
    #IV: take 0.75x dmg
    #V: take 0.5x dmg
    class Stick_Together_1(Passive):
        #when the unit is attacked, if an ally is adjacent, take 0.9 times damage.
        def __init__(self):
            self.check = 3
            self.flavour = "If an ally is adjacent when attacked, take 0.9 times damage."
            self.title = "Stick Together I"

        def exert(self, unit, battle, damage):
            #called in the take_damage function

            #check adjacent tiles.
            if unit.get_iff() == 0:
                map = battle.get_allymap()
            else:
                map = battle.get_enemymap()

            if isinstance(map.search_map((max(unit.get_point().get_x()-1, 0), unit.get_point().get_y())), Unit):
                if map.search_map((max(unit.get_point().get_x()-1, 0), unit.get_point().get_y())).get_ooa() == 0:
                    damage[0] = int(damage[0] * 0.9)

            elif isinstance(map.search_map((min(unit.get_point().get_x()+1, 4), unit.get_point().get_y())), Unit):
                if map.search_map((min(unit.get_point().get_x()+1, 4), unit.get_point().get_y())).get_ooa() == 0:
                    damage[0] = int(damage[0] * 0.9)

            elif isinstance(map.search_map((unit.get_point().get_x(), max(unit.get_point().get_y()-1, 0))), Unit):
                if map.search_map((unit.get_point().get_x(), max(unit.get_point().get_y()-1, 0))).get_ooa() == 0:
                    damage[0] = int(damage[0] * 0.9)

            elif isinstance(map.search_map((unit.get_point().get_x(), min(unit.get_point().get_y()+1, 4))), Unit):
                if map.search_map((unit.get_point().get_x(), min(unit.get_point().get_y()+1, 4))).get_ooa() == 0:
                    damage[0] = int(damage[0] * 0.9)

    #--- Revival ---#
    #type 5
    #I: revive with 1 hp
    #II: revive with 10% hp
    #III: revive with 25% hp
    #IV: revive with 50% hp
    #V: revive with 100% hp
    class Revival_1(Passive):
        def __init__(self):
            self.check = 5
            self.flavour = "The first time the unit is put out of action, the unit returns immediately with 1 HP."
            self.title = "Revival I"
            self.charges = 1

        def exert(self, unit):
            self.set_charges(0)
            unit.set_hp(1)

    #--- Stamina Drain ---#
    #type = 1
    #drain 2/5/7/10/15 stamina on an attack
    class Stamina_Drain_1(Passive):
        #when the unit is attacked, if an ally is adjacent, take 0.9 times damage.
        def __init__(self):
            self.check = 1
            self.flavour = "Drain 2 stamina on attack."
            self.title = "Stamina Drain I"

        def exert(self, unit, target):
            target.set_stamina(max(target.get_stamina()-2, 0))
            if target.get_stamina() == 0:
                target.get_stance().set_exhausted(1)

            self.set_stamina(min(self.get_stamina()+2), self.get_staminamax_actual())











#eof

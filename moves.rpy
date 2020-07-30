#self.element = 0
# -1: use weapon element.
# 0: normal
# 1: beast
# 2: ice
# 3: fire
# 4: lightning
# 5: earth
# 6: metal
# 7: vile
# 8: heroic

#self.dot = 0
# 0: no dot
# 1: poison
#--------------------------------
#---TO ADD ---
#how do we feel about 'slayer' moves. i.e. bonus against a certain type of units: beast slayer, man slayer, etc. i don't like them.


#tori:
#time warp: makes buffs run their course. set time remaining on target's buffs to half their current duration, or to 0 if current duration == 1. ??. or expire all buffs/dots on selected units? cool.
#energy transfer. transfers stamina, energy to target.

#yve:
#flourish.
#fast hit. more damage the more able units there are on the field.
#double hit. hits the same target twice.
#thrust. a longer version of pierce.
#flow. increases dodge, hit stances. enter the flow stance. (lose dodge slower, regain it faster)
#shock. heal hp based on how much hp yve is down. enter exhaustion state.

#nai:
#misdirect. target self or ally. lower priority so the enemy doesn't target you as often.
#enemy:
#pull/push units. get the player units out of position.

init -3 python:
    #--- GUIDELINES ---
    #any move that sets a stance first checks if the stance is already applied. If it is, the move only resets its duration.

    #--- MOVES ---
    class Move():
        def __init__(self):
            self.status_only = 0 #1: the move does no damage, affects only status. ex: adrenaline.
            self.flavour = "{i}flavour text/move description{/i}"
            self.title = "move"
            self.rank = 0 # can be 0 (anywhere), 1 (front), or 2 (back).
            self.type = 1 # for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 # for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #t he movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 0 # 0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 0 # the amount of stamina the unit loses using this move
            self.energy_drain = 0 # the amount of enerygy the unit loses using this move
            self.able_drain = 0 # the amount of able the unit loses using this move
            self.power = 0 # affects damage
            self.hit = 0 # affects dodging
            self.damage_type = 0 # 0: deals physical damage, 1: deals magical damage
            self.element = -1 # damage element. -1 through 8. see spreadsheet or top of this docs
            self.element_name = "" #shown in management, etc
            self.dot = 0 # int. tells the do_damage function to apply a certain stance to hit units.
            self.dot_duration = 0 # int. how long the applied dot will last.
            self.oob = 0 #0: cannot be used out of battle. #1: can be used out of battle.
        #getters
        def get_oob(self):
            return self.oob
        def get_element_name(self):
            return self.element_name
        def get_dot(self):
            return self.dot
        def get_dot_duration(self):
            return self.dot_duration
        def get_status_only(self):
            return self.status_only
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
        def get_energy_drain(self):
            return self.energy_drain
        def get_able_drain(self):
            return self.able_drain
        def get_power(self):
            return self.power
        def get_hit(self):
            return self.hit
        def get_damage_type(self):
            return self.damage_type
        def get_element(self):
            return self.element
        #useful functions
        def check_clearance(self, unit, battle):

            #make sure the board has enough room to accomodate the unit
            dtuple = (unit.get_point().get_x(), unit.get_point().get_y())

            if self.get_clearance_type() == 2:
                return 1

            if unit.get_point().get_x() + self.get_clearance()[0] in range(0, 5) and unit.get_point().get_y() + self.get_clearance()[1] in range(0, 5):

                if self.get_clearance_type() == 1: #needs only position clear

                    if battle.get_allymap().search_map((dtuple[0] + self.get_clearance()[0], dtuple[1] + self.get_clearance()[1])) == None:
                        return 1

                else: #needs all spots between self and destination clear

                    if self.get_clearance()[0] == 0: #vertical move
                        for i in range(unit.get_point().get_y() + self.get_clearance()[1], unit.get_point().get_y()):

                            if battle.get_allymap().search_map((unit.get_point().get_x(), i)) != None:
                                return 0

                    else: #horizontal move
                        for i in range(unit.get_point().get_x() + self.get_clearance()[0], unit.get_point().get_x()):

                            if battle.get_allymap().search_map((i, unit.get_point().get_y())) == None:
                                return 0
                    return 1
            return 0
        def translate(self, unit, battle):
            #we do not have to worry about borders, because the player cannot click on the move if its out of bounds.

            #if unit is in the map, disassociate the spot with the unit.
            if unit.get_iff() == 0: #allied unit
                battle.get_allymap().remove_unit(unit)

                #move unit
                unit.set_point(unit.get_point().get_x() + self.get_clearance()[0], unit.get_point().get_y() + self.get_clearance()[1])

                #place unit in map
                battle.get_allymap().place_unit(unit)
            else:
                battle.get_enemymap().remove_unit(unit)

                #move unit
                unit.set_point(unit.get_point().get_x() + self.get_clearance()[0], unit.get_point().get_y() + self.get_clearance()[1])

                #place unit  in map
                battle.get_enemymap().place_unit(unit)
        def drain(self, unit):
            unit.set_energy(unit.get_energy() - self.get_energy_drain())
            unit.set_stamina(max(unit.get_stamina()-self.get_stamina_drain(), 0))
            dif = unit.get_able() - self.get_able_drain()

            if dif < 0: #if the drain is greater than the unit's able
                dif = abs(dif) #take abs of dif
                for i in range(0, dif): #for each able drain greater than unit's able, drain 5 extra stam
                    unit.set_stamina(max(unit.get_stamina()-5, 0))
                    dif -= 1

            if unit.get_stamina() == 0: #if the unit is at 0 stamina, set them as exhausted
                unit.get_stance().set_exhausted(1)
            unit.set_able(dif)
        def do_damage(self, unit, targetlist, battle, dot, duration):
            showlist = []

            targetlist = list(set(targetlist)) #uncommment this line to turn off multihit.

            for target in targetlist:
                if isinstance(target, tuple):
                    showlist.append(target)
                elif target != None:
                    if target.get_ooa() == 0:
                        target.take_damage(unit, int(unit.calc_damage(target, self)), showlist, battle, dot, duration)

            if len(showlist) > 0:
                renpy.show_screen("show_damage", showlist, self.get_title(), unit)
        def do_heal(self, unit, targetlist):
            showlist = []

            targetlist = list(set(targetlist))

            for target in targetlist:
                if isinstance(target, tuple):
                    showlist.append(target)
                elif target != None:
                    if target.get_ooa() == 0:
                        target.take_heal(unit, unit.calc_heal(target, self), showlist, 0) #appends to showlist inside here

            if len(showlist) > 0:
                renpy.show_screen("show_heal", showlist, self.get_title(), unit)

        #oob
        def drain_oob(self, unit):
            #drains a unit for the out of battle skill menu
            unit.set_energy(unit.get_energy()-self.get_energy_drain())
            if unit.get_energy() == 0:
                renpy.hide_screen("oob_target_select")

        def do_heal_oob(self, unit, targetlist):
            #doing heals outside of battle
            for target in targetlist:
                if target.get_ooa() == 0:
                    target.take_heal_oob(unit, unit.calc_heal(target, self)) #appends to showlist inside here


    #--- Shared ---
    class Defend(Move):
        def __init__(self):
            self.status_only = 1
            self.flavour = "{i}Ready for an attack, raising physical defense.{/i}"
            self.title = "Defend"
            self.rank = 0
            self.type = 0
            self.iff = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 0
            self.energy_drain = 0
            self.able_drain = 0
            self.power = 0
            self.hit = 0
            self.damage_type = 0
            self.element = 0
            self.element_name = "-"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0
        def exert(self, unit, sq, battle):
            unit.set_stamina(int(min(unit.get_stamina()+(0.25 * unit.get_staminamax_actual()), unit.get_staminamax_actual())))
            unit.get_stance().enter_defend()
            unit.set_able(0)
    class Walk(Move):
        def __init__(self):
            self.status_only = 1
            self.flavour = "{i}Walk to adjust position.{/i}"
            self.title = "Walk"
            self.rank = 0
            self.type = 0
            self.iff = -1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 0
            self.energy_drain = 0
            self.able_drain = 0
            self.power = 0
            self.hit = 0
            self.damage_type = 0
            self.element = 0
            self.element_name = "-"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0
        def exert(self, unit, battle):
            #move to an open, adjacent square. ends the unit's turn.
            sq = renpy.invoke_in_new_context(call_highlight_walk, unit, battle) #tuple

            if sq == -1:
                return

            battle.get_allymap().remove_unit(unit)
            unit.get_point().set_x(sq[0])
            unit.get_point().set_y(sq[1])
            battle.get_allymap().place_unit(unit)
            unit.set_able(unit.get_able()-1)
            unit.end_turn()

    #--- Yve ---
    class Spear(Move):
        #single target,
        #low damage
        #low stam, low able
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}The oldest weapon.{/i}"
            self.title = "Spear"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 15
            self.energy_drain = 0
            self.able_drain = 1
            self.power = 25
            self.hit = 0
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            targetlist = []
            targetlist.append(battle.get_enemymap().search_map(sq))

            #calc damage and deal it to the target
            #damage =
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
    class Pierce(Move):
        #three squares in a row
        #low damage
        #med stam, med able
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}Strike through.{/i}"
            self.title = "Pierce"
            self.rank = 1
            self.type = 3
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 0
            self.stamina_drain = 30
            self.energy_drain = 1
            self.able_drain = 2
            self.power = 35
            self.hit = -5
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            #sq: the clicked square
            self.drain(unit)
            self.translate(unit, battle)

            r = sq[0]
            c = min(sq[1], 2)

            targetlist = []
            for i in range(0, 3):
                targetlist.append(battle.get_enemymap().search_map((r, c+i)))

            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
    class Adrenaline(Move):
        #self
        #heal some hp, can go over max. dodge up, hit up. fades after 4? turns
        #low stam, med able
        def __init__(self):
            self.status_only = 1
            self.flavour = "{i}Adrenaline is the best painkiller.{/i}"
            self.title = "Adrenaline"
            self.rank = 2
            self.type = 0
            self.iff = 1
            self.clearance = (0,-1)
            self.clearance_type = 1
            self.stamina_drain = 15
            self.energy_drain = 1
            self.able_drain = 1
            self.power = 0
            self.hit = 0
            self.damage_type = 0
            self.element = 0
            self.element_name = "-"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):

            #sq: the clicked square
            self.drain(unit)
            self.translate(unit, battle)

            #apply adrenaline stance
            if unit.get_stance().get_adrenaline() <= 0:
                unit.get_stance().enter_adrenaline(unit)
            else:
                unit.get_stance().set_adrenaline(5)
    class Whirl(Move):
        #3x3 cross minus the center square
        #med damage
        #med stam, low able
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}spin spin{/i}"
            self.title = "Ice Whirl"
            self.rank = 1
            self.type = 27
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 40
            self.energy_drain = 1
            self.able_drain = 1
            self.power = 50
            self.hit = 0
            self.damage_type = 0
            self.element = 2
            self.element_name = "Ice"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            self.drain(unit)
            self.translate(unit, battle)

            targetlist = []
            targetlist.append(battle.get_enemymap().search_map((sq[0], sq[1]-1)))
            targetlist.append(battle.get_enemymap().search_map((sq[0], sq[1]+1)))
            targetlist.append(battle.get_enemymap().search_map((sq[0]-1, sq[1])))
            targetlist.append(battle.get_enemymap().search_map((sq[0]+1, sq[1])))

            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())

    #--- Friday ---
    class Gun(Move):
        #shoot. single target. back rank. light damage. light cost.
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}Shoot.{/i}"
            self.title = "Gun"
            self.rank = 2
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 10
            self.energy_drain = 0
            self.able_drain = 1
            self.power = 20
            self.hit = 0
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            target = battle.get_enemymap().search_map(sq)
            targetlist = [target]
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
    class Beat_up(Move):
        #hits 2-4 times
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}hit someone a lot of times.{/i}"
            self.title = "Beat up"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 30
            self.energy_drain = 0
            self.able_drain = 1
            self.power = 5
            self.hit = 10
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def set_power(self, x):
            self.power = x
        def exert(self, unit, sq, battle):
            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            target = battle.get_enemymap().search_map(sq)
            targetlist = [target]

            i = renpy.random.randint(1, 10)
            self.set_power(self.get_power() * i)
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
            self.set_power(20)
    class First_aid(Move):
        #first aid. very light heal, stops bleeding. light cost.
        def __init__(self):
            self.status_only = 1
            self.flavour = "{i}Basic care, even by the talentless, is better than nothing.{/i}"
            self.title = "First Aid"
            self.rank = 2
            self.type = 1
            self.iff = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 20
            self.energy_drain = 1
            self.able_drain = 1
            self.power = 20 #heals
            self.hit = 0
            self.damage_type = 1
            self.element = 0
            self.element_name = "-"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 1

        def exert(self, unit, sq, battle):
            self.drain(unit)
            self.translate(unit, battle)

            target = battle.get_allymap().search_map(sq)
            targetlist = [target]

            if target != None:
                #heal a little. based on ma.
                if target.get_stance().get_bleeding() == 1:
                    target.set_stance().set_bleeding(0)

            self.do_heal(unit, targetlist)

        def exert_oob(self, unit, target):
            if target.get_hp() != target.get_hpmax():
                self.drain_oob(unit)

                targetlist = [target]

                self.do_heal_oob(unit, targetlist)
    class Suppress(Move):
        #suppress. 2x2. terrible hit. back rank.
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}Spread and inaccurate firing.{/i}"
            self.title = "Suppress"
            self.rank = 2
            self.type = 7
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 30
            self.energy_drain = 0
            self.able_drain = 1
            self.power = 20
            self.hit = -40
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            self.drain(unit)
            self.translate(unit, battle)

            r = min(sq[0], 3)
            c = min(sq[1], 3)

            target0 = battle.get_enemymap().search_map((r,c))
            target1 = battle.get_enemymap().search_map((r+1,c))
            target2 = battle.get_enemymap().search_map((r,c+1))
            target3 = battle.get_enemymap().search_map((r+1,c+1))
            targetlist = [target0, target1, target2, target3]
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
    class Form6(Move):
        #Twelve Forms - VI. 1x1. front rank. retreats 1.
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}Twelve Forms - Form VI.{/i}"
            self.title = "Form VI"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,1)
            self.clearance_type = 1
            self.stamina_drain = 10
            self.energy_drain = 0
            self.able_drain = 1
            self.power = 15
            self.hit = 0
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"

            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            targetlist = []
            targetlist.append(battle.get_enemymap().search_map(sq))

            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
    #class Iron_arm(Move):
        #single target, med dmg, metal attr.
        #increases friday's defense.
    #class Mark(Move):
        #single target. no damage.
        #lowers enemy's def, magic def. gives enemy back half their stamina.

    #--- Federal ---
    class Sword(Move):
        #sword. single target. front rank. light damage. light cost.
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}Strike with the sword.{/i}"
            self.title = "Sword"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 15
            self.energy_drain = 0
            self.able_drain = 1
            self.power = 20
            self.hit = 0
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            self.drain(unit)
            self.translate(unit, battle)

            targetlist = []
            targetlist.append(battle.get_enemymap().search_map(sq))

            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
    class Flourish(Move):
        #flourish. single target. front rank. heavy damage. heavy stamina cost. no able cost.
        def __init__(self):
            self.status_only = 0
            self.flavour = "{i}A fast and powerful blow.{/i}"
            self.title = "Flourish"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 30
            self.energy_drain = 1
            self.able_drain = 0
            self.power = 45
            self.hit = 5
            self.damage_type = 0
            self.element = -1
            self.element_name = "Weapon"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            self.drain(unit)
            self.translate(unit, battle)

            targetlist = []
            targetlist.append(battle.get_enemymap().search_map(sq))

            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())
    class Rally(Move):
        #rally. 3x3 (allies). hit up, physa up. back rank. light cost.
        def __init__(self):
            self.status_only = 1
            self.flavour = "{i}The unit rallies their teammates, increasing hit and attack.{/i}"
            self.title = "Rally"
            self.rank = 2
            self.type = 13
            self.iff = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 20
            self.energy_drain = 1
            self.able_drain = 1
            self.power = 0
            self.hit = 0
            self.damage_type = 0
            self.element = 0
            self.element_name = "-"
            self.dot = 0
            self.dot_duration = 0
            self.oob = 0

        def exert(self, unit, sq, battle):
            self.drain(unit)
            self.translate(unit, battle)

            r = min(sq[0], 2)
            c = min(sq[1], 2)

            targetlist = []
            for i in range(-1, 2):
                for x in range(-1, 2):
                    targetlist.append(battle.get_allymap().search_map((r+i,c+x)))

            for target in targetlist:
                if target != None:
                    if target.get_stance().get_rally() < 0 and target.get_ooa() == 0:
                        target.get_stance().enter_rally()
                    elif target.get_ooa() == 0:
                        target.get_stance().set_rally(5) #set/refresh duration

    #--- Federal Aide ---













#eof

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

init -3 python:
    #--- GUIDELINES ---

    #any move that sets a stance first checks if the stance is already applied. If it is, the move only resets its duration.

    #--- MOVES ---
    class move():
        def __init__(self):
            self.flavour = "{i}flavour text/move description{/i}"
            self.title = "move"
            self.rank = 0 #can be 0 (anywhere), 1 (front), or 2 (back).
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 0 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 0 #the amount of stamina the unit loses using this move
            self.able_drain = 0 #the amount of able the unit loses using this move
            self.power = 0 #affects damage
            self.hit = 0 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs
        #getters
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

                #place unit  in map
                battle.get_allymap().place_unit(unit)
            else:
                battle.get_enemymap().remove_unit(unit)

                #move unit
                unit.set_point(unit.get_point().get_x() + self.get_clearance()[0], unit.get_point().get_y() + self.get_clearance()[1])

                #place unit  in map
                battle.get_enemymap().place_unit(unit)
        def drain(self, unit):
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
        def do_damage(self, unit, nl, battle):
            showlist = [] #list of tuples: (unit, damage)

            for target in nl:
                if target != None:
                    if target.get_ooa() == 0:
                        target.take_damage(unit, unit.calc_damage(target, self), showlist, battle)

            if len(showlist) > 0:
                renpy.show_screen("show_damage", showlist)
        def do_heal(self, unit, nl):
            showlist = [] #list of tuples: (unit, damage)

            for target in nl:
                if target != None:
                    if target.get_ooa() == 0:
                        target.take_heal(unit, unit.calc_heal(target, self), showlist)

            if len(showlist) > 0:
                renpy.show_screen("show_heal", showlist)




    #--- Yve ---
    class spear(move):
        #single target,
        #low damage
        #low stam, low able
        def __init__(self):
            self.flavour = "{i}Hit with the point.{/i}"
            self.title = "Spear"
            self.rank = 1 #can be 1, or 2. determines where the move can be used
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 2 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 15 #the amount of stamina the unit loses using this move
            self.able_drain = 1 #the amount of able the unit loses using this move
            self.power = 20 #affects damage
            self.hit = 0 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            target = battle.get_enemymap().search_map(sq)
            targetlist = [target]

            #calc damage and deal it to the target
            #damage =
            self.do_damage(unit, targetlist, battle)

    class pierce(move):
        #three squares in a row
        #low damage
        #med stam, med able
        def __init__(self):
            self.flavour = "{i}Pierce through.{/i}"
            self.title = "Pierce"
            self.rank = 1 #can be 1, or 2. determines where the move can be used
            self.type = 3 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 0 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 30 #the amount of stamina the unit loses using this move
            self.able_drain = 2 #the amount of able the unit loses using this move
            self.power = 35 #affects damage
            self.hit = -5 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            self.drain(unit)
            self.translate(unit, battle)

            r = sq[0]
            c = min(sq[1], 2)

            target = battle.get_enemymap().search_map((r,c))
            target2 = battle.get_enemymap().search_map((r,c+1))
            target3 = battle.get_enemymap().search_map((r,c+2))
            targetlist = [target, target2, target3]

            self.do_damage(unit, targetlist, battle)

    class adrenaline(move):
        #self
        #heal some hp, can go over max. dodge up, hit up. fades after 4? turns
        #low stam, med able
        def __init__(self):
            self.flavour = "{i}Quicken the senses.{/i}"
            self.title = "Adrenaline"
            self.rank = 2 #can be 1, or 2. determines where the move can be used
            self.type = 0 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 1 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,-1) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 1 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 15 #the amount of stamina the unit loses using this move
            self.able_drain = 1 #the amount of able the unit loses using this move
            self.power = 0 #affects damage
            self.hit = 0 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            self.drain(unit)
            self.translate(unit, battle)

            #apply adrenaline stance
            if unit.get_stance().get_adrenaline() <= 0:
                unit.get_stance().enter_adrenaline(unit)
            else:
                unit.get_stance().set_adrenaline(5)

    class whirl(move):
        #3x3 cross minus the center square
        #med damage
        #med stam, low able
        def __init__(self):
            self.flavour = "{i}I am a storm.{/i}"
            self.title = "Ice Whirl"
            self.rank = 1 #can be 1, or 2. determines where the move can be used
            self.type = 27 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 2 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 40 #the amount of stamina the unit loses using this move
            self.able_drain = 2 #the amount of able the unit loses using this move
            self.power = 50 #affects damage
            self.hit = 0 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 4 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            target2 = battle.get_enemymap().search_map((sq[0],sq[1]-1))
            target3 = battle.get_enemymap().search_map((sq[0],sq[1]+1))
            target4 = battle.get_enemymap().search_map((sq[0]-1,sq[1]))
            target5 = battle.get_enemymap().search_map((sq[0]+1,sq[1]))
            targetlist = [target2, target3, target4, target5]

            self.do_damage(unit, targetlist, battle)

    #--- Federal ---
    class sword(move):
        #sword. single target. front rank. light damage. light cost.
        def __init__(self):
            self.flavour = "{i}Strike with the sword.{/i}"
            self.title = "Sword"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 15
            self.able_drain = 1
            self.power = 20
            self.hit = 0
            self.damage_type = 0
            self.element = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            target = battle.get_enemymap().search_map(sq)
            targetlist = [target]

            #calc damage and deal it to the target
            #damage =
            self.do_damage(unit, targetlist, battle)

    class flourish(move):
        #flourish. single target. front rank. heavy damage. heavy stamina cost. no able cost.
        def __init__(self):
            self.flavour = "{i}A fast, accurate blow.{/i}"
            self.title = "Flourish"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 35
            self.able_drain = 0
            self.power = 50
            self.hit = 5
            self.damage_type = 0
            self.element = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            target = battle.get_enemymap().search_map(sq)
            targetlist = [target]

            #calc damage and deal it to the target
            #damage =
            self.do_damage(unit, targetlist, battle)

    class form6(move):
        #Twelve Forms - VI. 1x1. front rank. retreats 2.
        def __init__(self):
            self.flavour = "{i}Twelve Forms - Form VI.{/i}"
            self.title = "Form VI"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,1)
            self.clearance_type = 0
            self.stamina_drain = 20
            self.able_drain = 1
            self.power = 10
            self.hit = 0
            self.damage_type = 0
            self.element = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            target = battle.get_enemymap().search_map(sq)
            targetlist = [target]
            self.do_damage(unit, targetlist, battle)


    class rally(move):
        #rally. 3x3 (allies). hit up, physa up. back rank. light cost.
        def __init__(self):
            self.flavour = "{i}Rally together.{/i}"
            self.title = "Rally"
            self.rank = 2
            self.type = 13
            self.iff = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 20
            self.able_drain = 1
            self.power = 0
            self.hit = 0
            self.damage_type = 0
            self.element = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            r = min(sq[0], 2)
            c = min(sq[1], 2)

            target0 = battle.get_allymap().search_map((r-1,c-1))
            target1 = battle.get_allymap().search_map((r, c-1))
            target2 = battle.get_allymap().search_map((r+1,c-1))
            target3 = battle.get_allymap().search_map((r-1,c))
            target4 = battle.get_allymap().search_map((r,c))
            target5 = battle.get_allymap().search_map((r+1,c))
            target6 = battle.get_allymap().search_map((r-1,c+1))
            target7 = battle.get_allymap().search_map((r,c+1))
            target8 = battle.get_allymap().search_map((r+1,c+1))
            targetlist = [target0, target1, target2, target3, target4, target5, target6, target7, target8]

            #apply buffs to any targets
            #-physa up
            #-hit up

            for target in targetlist:
                if target != None:
                    if target.get_stance().get_rally() <= 0: #if rally is not active on this unit, make it so.
                        target.get_stance().enter_rally()
                    target.get_stance().set_rally(5) #set/refresh duration

    class shoot(move):
        #shoot. single target. back rank. light damage. light cost.
        def __init__(self):
            self.flavour = "{i}Shoot carefully.{/i}"
            self.title = "Shoot"
            self.rank = 2
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 15
            self.able_drain = 1
            self.power = 15
            self.hit = 0
            self.damage_type = 0
            self.element = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #this move hits only the selected square.
            target = battle.get_enemymap().search_map(sq)
            targetlist = [target]
            self.do_damage(unit, targetlist, battle)

    #--- Federal Aide ---
    class suppress(move):
        #suppress. 2x2. terrible hit. back rank.
        def __init__(self):
            self.flavour = "{i}A swift, innacurate burst.{/i}"
            self.title = "Suppress"
            self.rank = 2
            self.type = 7
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 30
            self.able_drain = 1
            self.power = 15
            self.hit = -40
            self.damage_type = 0
            self.element = 0

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            r = min(sq[0], 3)
            c = min(sq[1], 3)

            target0 = battle.get_enemymap().search_map((r,c))
            target1 = battle.get_enemymap().search_map((r+1,c))
            target2 = battle.get_enemymap().search_map((r,c+1))
            target3 = battle.get_enemymap().search_map((r+1,c+1))
            targetlist = [target0, target1, target2, target3]
            self.do_damage(unit, targetlist, battle)

    class first_aid(move):
        #first aid. very light heal, stops bleeding. light cost.
        def __init__(self):
            self.flavour = "{i}Basic magical care.{/i}"
            self.title = "First Aid"
            self.rank = 2 #can be 1, or 2. determines where the move can be used
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 1 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 2 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 20 #the amount of stamina the unit loses using this move
            self.able_drain = 1 #the amount of able the unit loses using this move
            self.power = 15 #affects damage/heals
            self.hit = 0 #affects dodging
            self.damage_type = 1 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            self.drain(unit)
            self.translate(unit, battle)


            #do stuff
            target = battle.get_allymap().search_map(sq)
            targetlist = [target]

            #the game thinks the selected spot is none

            if target != None:
                #heal a little. based on ma.
                if target.get_stance().get_bleeding() == 1:
                    target.set_stance().set_bleeding(0)

            self.do_heal(unit, targetlist)













#---TO ADD ---
#tori:
#time warp: makes buffs run their course. set time remaining on target's buffs to half their current duration, or to 0 if current duration == 1.

#boy:
#screw: power = 3 or something. stam cost = 5 or something. purpose is to use up enemies kindara/shatter point/defensive stances, yeah.

#yve:
#flourish. heavy stam drain, but no able.
#battlefield trance. increase able and stamina regen at the start of each round.

#nai:
#misdirect. target self or ally. lower priority so the enemy doesn't target you as often.

#enemy:
#pull/push units. get the player units out of position.






#eof

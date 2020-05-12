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

init -2 python:
    #--- GUIDELINES ---

    #any move that sets a stance first checks if the stance is already applied. If it is, the move only resets its duration




    #--- MOVES ---
    class move():
        def __init__(self):
            self.flavour = "{i}flavour text/move description{/i}"
            self.title = "move"
            self.rank = 0 #can be 0, 1, or 2. determines where the move can be used
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
            battle.get_allymap().remove_unit(unit)

            #move unit
            unit.set_point(unit.get_point().get_x() + self.get_clearance()[0], unit.get_point().get_y() + self.get_clearance()[1])

            #place unit  in map
            battle.get_allymap().place_unit(unit)
        def drain(self, unit):
            unit.set_stamina(max(unit.get_stamina()-self.get_stamina_drain(), 0))


            dif = unit.get_able() - self.get_able_drain()

            if dif < 0: #if the drain is greater than the unit's able
                dif = abs(dif) #take abs of dif
                for i in range(0, dif): #for each able drain greater than unit's able, drain 5 extra stam
                    unit.set_stamina(max(unit.get_stamina()-5, 0))
                    dif -= 1

            if unit.get_stamina() == 0: #if the unit is at 0 stamina, set them as exhausted
                unit.get_stance().set_exhausted(1,0)
            unit.set_able(dif)

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

            #calc damage and deal it to the target
            #damage =
            if target != None:
                target.take_damage(unit, unit.calc_damage(target, self))

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
            self.stamina_drain = 20 #the amount of stamina the unit loses using this move
            self.able_drain = 2 #the amount of able the unit loses using this move
            self.power = 25 #affects damage
            self.hit = -5 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            self.drain(unit)
            self.translate(unit, battle)

            target = battle.get_enemymap().search_map(sq)
            target2 = battle.get_enemymap().search_map((sq[0],abs(sq[1]-1)))
            if sq[1] == 1:
                target3 = battle.get_enemymap().search_map((sq[0],2))
            else:
                target3 = battle.get_enemymap().search_map((sq[0],abs(sq[1]-2)))

            if target != None:
                target.take_damage(unit, unit.calc_damage(target, self))
            if target2 != None:
                target2.take_damage(unit, unit.calc_damage(target2, self))
            if target3 != None:
                target3.take_damage(unit, unit.calc_damage(target3, self))

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
            if unit.get_stance().get_adrenaline()[0] > 0:
                unit.get_stance().set_adrenaline(5, 0)
            else:
                unit.get_stance().enter_adrenaline(unit)

    class whirl(move):
        #3x3 cross minus the center square
        #med damage
        #med stam, low able
        def __init__(self):
            self.flavour = "{i}I am a vortex.{/i}"
            self.title = "Whirl"
            self.rank = 1 #can be 1, or 2. determines where the move can be used
            self.type = 27 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 2 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 30 #the amount of stamina the unit loses using this move
            self.able_drain = 2 #the amount of able the unit loses using this move
            self.power = 40 #affects damage
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

            if target2 != None:
                target2.take_damage(unit, unit.calc_damage(target2, self))
            if target3 != None:
                target3.take_damage(unit, unit.calc_damage(target3, self))
            if target4 != None:
                target4.take_damage(unit, unit.calc_damage(target4, self))
            if target5 != None:
                target5.take_damage(unit, unit.calc_damage(target5, self))


    #--- Federal ---
    #sword. single target. front rank. light damage. light cost.
    #flourish. single target. front rank. heavy damage. heavy stamina cost. no able cost.
    #rally. 3x3 (allies). hit up, physa up. back rank. light cost.
    #quickshot. horizontal pair. back rank. medium cost.

    #--- Federal Aide ---
    #shoot. single target. back rank. light damage. light cost.
    #suppress. 2x2. terrible hit. back rank.
    #Twelve Forms - VI. 1x1. front rank. retreats 2.



    #--- TEST MOVES ---

    class skate(move):
        def __init__(self):
            self.flavour = "{i}Skates can cut{/i}"
            self.title = "Skate"
            self.rank = 2
            self.type = 15
            self.iff = 0
            self.clearance = (0,-4)
            self.clearance_type = 0 #needs whole row clear
            self.stamina_drain = 30
            self.able_drain = 2
            self.power = 50
            self.hit = 0
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8.

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            target = battle.get_enemymap().search_map(sq)
            if target != None:
                target.take_damage(unit.calc_damage(target, self))

            if sq[1] != 0:
                target0 = battle.get_enemymap().search_map((sq[0],0))
                if target0 != None:
                    target0.take_damage(unit.calc_damage(target0, self))
            if sq[1] != 1:
                target1 = battle.get_enemymap().search_map((sq[0],1))
                if target1 != None:
                    target1.take_damage(unit.calc_damage(target1, self))
            if sq[1] != 2:
                target2 = battle.get_enemymap().search_map((sq[0],2))
                if target2 != None:
                    target2.take_damage(unit.calc_damage(target2, self))
            if sq[1] != 3:
                target3 = battle.get_enemymap().search_map((sq[0],3))
                if target3 != None:
                    target3.take_damage(unit.calc_damage(target3, self))
            if sq[1] != 4:
                target4 = battle.get_enemymap().search_map((sq[0],4))
                if target4 != None:
                    target4.take_damage(unit.calc_damage(target4, self))

    class evo_storm(move):
        def __init__(self):
            self.flavour = "{i}Storm on the horizon.{/i}"
            self.title = "Storm"
            self.rank = 0
            self.type = 1
            self.iff = 2
            self.clearance = (0,0)
            self.clearance_type = 0
            self.stamina_drain = 0
            self.able_drain = 0
            self.power = 0
            self.hit = 0
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            pass




#---TO ADD ---
#tori:
#time warp: makes buffs run their course. set time remaining on target's buffs to half their current duration, or to 0 if current duration == 1.

#boy:
#screw: does 1 damage. purpose is to use up enemies kindara/shatter point.

#yve:
#flourish. heavy stam drain, but no able.
#battlefield trance. increase able and stamina regen at the start of each round.

#nai:
#misdirect. target self or ally. lower priority so the enemy doesn't target you as often.



#enemy:
#pull/push units. get the player units out of position.






#eof

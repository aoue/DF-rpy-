
init -2 python:
    #--- ENEMY MOVES ---
    class enemy_move(move):
        def __init__(self):
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

            #additional variables
            self.weight = 0 #more powerful moves have higher. max 100. min 1. a unit must have at least one (weight 1) move.
            self.effort = 0 #1(heavy), 2(medium), 3(light). To help the enemy think.
            self.aoe = 0 #0: not aoe, 1: is aoe
            self.heal = 0 #0: not a healing move, 1: is a healing move
            self.targeting = 0 #what is the move's preferred target.

        #--- ENEMY TARGETING LEGEND ---
        #0: hit random target
        #1: hit enemy closest to the front
        #2: hit enemy closest to the back
        #3: hit enemy with lowest hp
        #4: hit enemy with lowest defense of the type the move attacks.
        #?: hit enemy weak to move's element
        #etc

        #getters
        def get_weight(self):
            return self.weight
        def get_effort(self):
            return self.effort
        def get_aoe(self):
            return self.aoe
        def get_heal(self):
            return self.heal
        def get_targeting(self):
            return self.targeting
        def pick_target(self, pl, el, battle):
            if self.get_aoe() == 0 and self.get_heal() == 0: #single target

                if self.get_targeting() == 0: #random target:
                    while True:
                        i = random.randint(0, len(pl)-1)
                        if pl[i].get_ooa() == 0:
                            return pl[i]
                elif self.get_targeting() == 1: #closest to front. in ties, randomly pick.
                    targetlist = []
                    for column in range(0, 5):
                        for row in range(0, 5):
                            if battle.get_allymap().search_map((row, column)) != None and battle.get_allymap().search_map((row, column)).get_ooa() == 0:
                                targetlist.append(battle.get_allymap().search_map((row, column)))

                        if targetlist: #if list is not empty
                            i = random.randint(0, len(targetlist)-1)
                            return targetlist[i]
                elif self.get_targeting() == 2: #closest to back. in ties, randomly pick.
                    targetlist = []
                    for column in reversed(range(0, 5)):
                        for row in range(0, 5):
                            if battle.get_allymap().search_map((row, column)) != None and battle.get_allymap().search_map((row, column)).get_ooa() == 0:
                                targetlist.append(battle.get_allymap().search_map((row, column)))

                        if targetlist: #if list is not empty
                            i = random.randint(0, len(targetlist)-1)
                            return targetlist[i]
                elif self.get_targeting() == 3: #lowest hp.
                    x = 999999
                    for unit in pl:
                        if unit.get_hp() < x and unit.get_ooa() == 0:
                            x = unit.get_hp()
                            target = unit
                    return target
                elif self.get_targeting() == 4: #lowest defense of type the move hits.
                    x = 999999

                    if self.get_damage_type() == 0: #physical damage
                        for unit in pl:
                            if unit.get_physd() < x and unit.get_ooa() == 0:
                                x = unit.get_physd()
                                target = unit
                    else:
                        for unit in pl:
                            if unit.get_magd() < x and unit.get_ooa() == 0:
                                x = unit.get_physd()
                                target = unit
                    return target




            elif self.get_aoe() == 0 and self.get_heal() == 1: #single target heal
                if self.get_healer() == 1 and self.get_stamina/self.get_staminamax() > 0.5:
                    min = 999999
                    for unit in el:
                        if unit.get_ooa() == 0 and unit.get_hp()/unit.get_hpmax() <= 0.6:
                            if unit.get_hp() < min:
                                min = unit.get_hp()
                                target = unit


            elif self.get_aoe() == 1 and self.get_heal() == 0: #aoe
                pass

                ##choosing aoe target area:
                #for each square in every (row max - aoe length) in every (column max - target area height):
                    #tally all the units in the square taking the current square as top left.
                        #keep a running max
                #use on the best area (9/10) or random area (1/10 accompanied by line: 'ugh - my hand slipped!' maybe?


            else: #aoe heal
                pass


    class e_claw(enemy_move):
        def __init__(self):
            self.rank = 1 #can be 0 (anywhere), 1 (front), or 2 (back).
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 2 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 0 #the amount of stamina the unit loses using this move
            self.able_drain = 1 #the amount of able the unit loses using this move
            self.power = 20 #affects damage
            self.hit = 2 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

            #additional variables
            self.weight = 100 #more powerful moves have higher. max 100. min 1. a unit must have at least one (weight 1) move.
            self.effort = 1 #1(heavy), 2(medium), 3(light). To help the enemy think.
            self.aoe = 0 #0: not aoe, 1: is aoe
            self.heal = 0 #0: not a healing move, 1: is a healing move
            self.targeting = 1 #what is the move's preferred target.

        def exert(self, unit, pl, el, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #targeting.
            #for this test, just target the first unit in pl
            target = self.pick_target(pl, el, battle)
            targetlist = [target]

            #calc damage and deal it to the target
            self.do_damage(unit, targetlist, battle)























##eof

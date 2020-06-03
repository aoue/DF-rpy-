
#be wary - enemy board is flipped compared to player's board.
#-ranks are reversed
#-translations are reversed


#--- ENEMY TARGETING LEGEND ---
#0: hit random target
#1: hit enemy closest to the front
#2: hit enemy closest to the back
#3: hit enemy with lowest hp
#4: hit enemy with lowest defense of the type the move attacks.
#?: hit enemy weak to move's element
#etc


init -2 python:
    #--- ENEMY MOVES ---
    class Enemy_move(Move):
        def __init__(self):
            self.flavour = "{i}str{/i}"
            self.title = "str"
            self.rank = 0 #can be 0 (anywhere), 1 (back), or 2 (front).
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 0 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 0 #the amount of stamina the unit loses using this move
            self.able_drain = 0 #the amount of able the unit loses using this move
            self.power = 0 #affects damage
            self.hit = 0 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.dot = 0 #int. tells the do_damage function to apply a certain stance to hit units.
            self.dot_duration = 0 #int. how long the applied dot will last.

            #additional variables
            self.weight = 0 #more powerful moves have higher. max 100. min 1. a unit must have at least one (weight 1) move.
            self.effort = 0 #1(heavy), 2(medium), 3(light). To help the enemy think.
            self.aoe = 0 #0: not aoe, 1: is aoe
            self.aoe_area = (0,0) #dimensions of aoe area
            self.heal = 0 #0: not a healing move, 1: is a healing move
            self.targeting = 0 #what is the move's preferred target.

        #getters
        def get_aoe_area(self):
            return self.aoe_area
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
        #useful functions
        def e_drain(self, unit):
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
        def e_check_clearance(self, stuple, battle):

            #make sure the board has enough room to accomodate the unit
            #dtuple = (unit.get_point().get_x(), unit.get_point().get_y())
            dtuple = (min(max(stuple[0], 0), 4), min(max(stuple[1], 0), 4))

            if self.get_clearance_type() == 2:
                return 1

            if stuple[0] + self.get_clearance()[0] in range(0, 5) and stuple[1] + self.get_clearance()[1] in range(0, 5):

                if self.get_clearance_type() == 1: #needs only position clear

                    if battle.get_enemymap().search_map((dtuple[0] + self.get_clearance()[0], dtuple[1] + self.get_clearance()[1])) == None:
                        return 1

                else: #needs all spots between self and destination clear

                    if self.get_clearance()[1] > 0: #vertical move to the front
                        for i in range(stuple[1] - self.get_clearance()[1], stuple[1]):
                            if battle.get_enemymap().search_map((stuple[0], i)) != None:
                                return 0
                    elif self.get_clearance()[1] < 0: #vertical move to the back
                        for i in range(stuple[1], stuple[1] + self.get_clearance()[1]):
                            if battle.get_enemymap().search_map((stuple[0], i)) != None:
                                return 0

                    elif self.get_clearance()[0] > 0: #horizontal move to the right
                        for i in range(stuple[0], stuple[0] + self.get_clearance()[0]):
                            if battle.get_enemymap().search_map((i, stuple[1])) == None:
                                return 0

                    else: #horizontal move to the left
                        for i in range(stuple[0] - self.get_clearance()[0], stuple[0]):
                            if battle.get_enemymap().search_map((i, stuple[1])) == None:
                                return 0


                    return 1
            return 0
        def manage_target(self, iff, x, y, map, targetlist):
            #searches map for position of (x,y)
            #if none, then append to showlist:
            #map: battle.get_enemymap() or battle.get_allymap()

            if map.search_map((x, y)) == None:
                if iff == 0:
                    targetlist.append((x, y, -1, 1))
                else:
                    targetlist.append((x, y, -1, 0))

            else:
                targetlist.append(map.search_map((x,y)))
        def non_tuple_items(self, nl):
            #returns number of non-tuple items in a list
            count = 0
            for item in nl:
                if isinstance(item, tuple) == False:
                    count += 1
            return count

        def pick_target(self, pl, battle):

            if pl[0].get_iff() == 0:
                map = battle.get_allymap()
                iff = 1
            else:
                map = battle.get_enemymap()
                iff = 0

            if self.get_aoe() == 0 and self.get_heal() == 0: #single target
                if self.get_targeting() == 0: #random target:
                    while True:
                        i = renpy.random.randint(0, len(pl)-1)
                        if pl[i].get_ooa() == 0:
                            return pl[i]
                elif self.get_targeting() == 1: #closest to front. in ties, randomly pick.
                    targetlist = []
                    for column in range(0, 5):
                        for row in range(0, 5):
                            if map.search_map((row, column)) != None and map.search_map((row, column)).get_ooa() == 0:
                                targetlist.append(map.search_map((row, column)))

                        if targetlist: #if list is not empty
                            i = renpy.random.randint(0, len(targetlist)-1)
                            return targetlist[i]
                elif self.get_targeting() == 2: #closest to back. in ties, randomly pick.
                    targetlist = []
                    for column in reversed(range(0, 5)):
                        for row in range(0, 5):
                            if map.search_map((row, column)) != None and map.search_map((row, column)).get_ooa() == 0:
                                targetlist.append(map.search_map((row, column)))

                        if targetlist: #if list is not empty
                            i = renpy.random.randint(0, len(targetlist)-1)
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
                            if unit.get_physd_actual() < x and unit.get_ooa() == 0:
                                x = unit.get_physd_actual()
                                target = unit
                    else:
                        for unit in pl:
                            if unit.get_magd_actual() < x and unit.get_ooa() == 0:
                                x = unit.get_magd_actual()
                                target = unit
                    return target

            elif self.get_aoe() == 0 and self.get_heal() == 1: #single target heal
                pass
                #if self.get_healer() == 1 and self.get_stamina/self.get_staminamax() > 0.5:
                #    min = 999999
                #    for unit in el:
                #        if unit.get_ooa() == 0 and unit.get_hp()/unit.get_hpmax() <= 0.6:
                #            if unit.get_hp() < min:
                #                min = unit.get_hp()
                #                target = unit

            elif self.get_aoe() == 1 and self.get_heal() == 0: #aoe attack
                ##choosing aoe target area:
                #for each square in every (row max - aoe length) in every (column max - target area height):
                    #tally all the units in the square taking the current square as top left.
                        #keep a running max
                targetmaxlist = [] #list of max

                #for each square:
                for column in range(0, 5 - self.get_aoe_area()[1]):
                    for row in range(0, 5 - self.get_aoe_area()[0]):
                        targetlist = [] #which units are targeted

                        #generate an aoe for each area
                        for i in range(column, column + self.get_aoe_area()[1]):
                            for x in range(row, row + self.get_aoe_area()[0]):
                                self.manage_target(iff, x, i, map, targetlist)

                                #now, we want to compare number of non-none items in targetlist to targetmaxlist
                        if self.non_tuple_items(targetlist) > self.non_tuple_items(targetmaxlist):
                            targetmaxlist = targetlist
                        elif targetlist != targetmaxlist and self.non_tuple_items(targetlist) == self.non_tuple_items(targetmaxlist):
                            #50% chance to take new list, 50% to keep old:
                            i = renpy.random.randint(0, 1)
                            if i == 1:
                                targetmaxlist = targetlist
                return targetmaxlist

                #old:
                #                if map.search_map((x, i)) != None:
                #                        targetlist.append(map.search_map((x, i)))
                #        if len(targetlist) > len(targetmaxlist):
                #            targetmaxlist = targetlist
                #        elif targetlist != targetmaxlist and len(targetlist) == len(targetmaxlist):
                #            #50% chance to take new list, 50% to keep old:
                #            i = renpy.random.randint(0, 1)
                #            if i == 1:
                #                targetmaxlist = targetlist
                #
                #return targetmaxlist


            else: #aoe heal
                pass



    ## -- Beast Moves -- ##
    class E_claw(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Filthy clawing.{/i}"
            self.title = "Claw"
            self.rank = 2
            self.type = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 15
            self.able_drain = 1
            self.power = 15
            self.hit = 0
            self.damage_type = 0
            self.element = -1
            self.dot = 0
            self.dot_duration = 0
            self.weight = 100
            self.effort = 1
            self.aoe = 0
            self.heal = 0
            self.targeting = 1

        def exert(self, unit, pl, el, battle):
            self.e_drain(unit)
            self.translate(unit, battle)

            target = self.pick_target(pl, battle)
            targetlist = [target]
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())

    class E_jaws(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Terrible jaws.{/i}"
            self.title = "Jaws"
            self.rank = 2
            self.type = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 30
            self.able_drain = 1
            self.power = 23
            self.hit = -5
            self.damage_type = 0
            self.element = -1
            self.dot = 0
            self.dot_duration = 0
            self.weight = 60
            self.effort = 3
            self.aoe = 0
            self.heal = 0
            self.targeting = 0

        def exert(self, unit, pl, el, battle):
            self.e_drain(unit)
            self.translate(unit, battle)

            target = self.pick_target(pl, battle)
            targetlist = [target]
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())

    class E_rush(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Terrible Leap.{/i}"
            self.title = "Rush"
            self.rank = 1
            self.type = 1
            self.clearance = (0,3)
            self.clearance_type = 0
            self.stamina_drain = 20
            self.able_drain = 1
            self.power = 20
            self.hit = -20
            self.damage_type = 0
            self.element = -1
            self.dot = 0
            self.dot_duration = 0
            self.weight = 100
            self.effort = 1
            self.aoe = 0
            self.heal = 0
            self.targeting = 2

        def exert(self, unit, pl, el, battle):
            self.e_drain(unit)
            self.translate(unit, battle)

            target = self.pick_target(pl, battle)
            targetlist = [target]
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())

    class E_howl(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Terrible Howling.{/i}"
            self.title = "Howl"
            self.rank = 1
            self.type = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 20
            self.able_drain = 1
            self.power = 0
            self.hit = 0
            self.damage_type = 0
            self.element = 0
            self.dot = 0
            self.dot_duration = 0
            self.weight = 20
            self.effort = 1
            self.aoe = 0
            self.heal = 0
            self.targeting = 1

        def exert(self, unit, pl, el, battle):
            self.e_drain(unit)
            self.translate(unit, battle)

            if unit.get_stance().get_howl() <= 0:
                unit.get_stance().enter_howl()
            else:
                unit.get_stance().set_howl(2)

    class E_clobber(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Clobbering.{/i}"
            self.title = "Clobber"
            self.rank = 1
            self.type = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 25
            self.able_drain = 1
            self.power = 35
            self.hit = 0
            self.damage_type = 0
            self.element = 1
            self.dot = 0
            self.dot_duration = 0
            self.weight = 80
            self.effort = 2
            self.aoe = 0
            self.heal = 0
            self.targeting = 1

        def exert(self, unit, pl, el, battle):
            self.e_drain(unit)
            self.translate(unit, battle)

            target = self.pick_target(pl, battle)
            targetlist = [target]
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())

    class E_spew(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Spew poison.{/i}"
            self.title = "Spew"
            self.rank = 1
            self.type = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 40
            self.able_drain = 1
            self.power = 25
            self.hit = 0
            self.damage_type = 0
            self.element = 7
            self.dot = 1
            self.dot_duration = 3
            self.weight = 100
            self.effort = 3
            self.aoe = 1
            self.aoe_area = (3,3)
            self.heal = 0
            self.targeting = 1

        def exert(self, unit, pl, el, battle):
            self.e_drain(unit)
            self.translate(unit, battle)

            targetlist = self.pick_target(pl, battle)
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())

    class E_call_jowlers(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Calls 3 jowlers to join the fight.{/i}"
            self.title = "Call Jowlers"
            self.rank = 1
            self.type = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 0
            self.able_drain = 0
            self.power = 0
            self.hit = 0
            self.damage_type = 0
            self.element = 1
            self.dot = 0
            self.dot_duration = 0
            self.weight = 100
            self.effort = 1
            self.aoe = 0
            self.heal = 0
            self.targeting = 3

        def exert(self, unit, pl, el, battle):

            self.e_drain(unit)
            self.translate(unit, battle)

            if len(el) == 1:
                newbaddie = Unit_jowler(0, "jowler", battle.get_enemymap().random_empty(), 0)
                el.append(newbaddie)
                battle.get_enemymap().place_unit(newbaddie)

                newbaddie2 = Unit_jowler(0, "jowler 2", battle.get_enemymap().random_empty(), 0)
                el.append(newbaddie2)
                battle.get_enemymap().place_unit(newbaddie2)

                newbaddie3 = Unit_jowler(0, "jowler 3", battle.get_enemymap().random_empty(), 0)
                el.append(newbaddie3)
                battle.get_enemymap().place_unit(newbaddie3)

                return


    class E_gobble(Enemy_move):
        def __init__(self):
            self.flavour = "{i}Eats whatever's nearby.{/i}"
            self.title = "Gobble"
            self.rank = 1
            self.type = 1
            self.clearance = (0,0)
            self.clearance_type = 2
            self.stamina_drain = 0
            self.able_drain = 1
            self.power = 20
            self.hit = 0
            self.damage_type = 0
            self.element = 1
            self.dot = 0
            self.dot_duration = 0
            self.weight = 100
            self.effort = 1
            self.aoe = 0
            self.heal = 0
            self.targeting = 3

        def exert(self, unit, pl, el, battle):
            self.e_drain(unit)
            self.translate(unit, battle)

            if len(el) == 1:
                move_alt = E_call_jowlers()
                move_alt.exert(unit, pl, el, battle)
                unit.set_stamina(min(unit.get_stamina()+20, unit.get_staminamax()))
                return

            #search own side for unit with lowest hp
            target0 = self.pick_target(el, battle)

            #search player side for unit with lowest hp
            target = self.pick_target(pl, battle)

            #compare the two targets, go with the one that has lower hp:
            if target0.get_hp() < target.get_hp() and target0 != unit:
                target = target0
            else:
                target = target
            targetlist = [target]

            #calc damage and deal it to the target
            self.do_damage(unit, targetlist, battle, self.get_dot(), self.get_dot_duration())


            #if the target is killed:
            if target.get_ooa() == 1:
                unit.set_hp(min(unit.get_hp()+100,unit.get_hpmax()))
                unit.set_stamina(min(unit.get_stamina()+75, unit.get_staminamax()))
            else:
                unit.set_stamina(min(unit.get_stamina()+30, unit.get_staminamax()))






















##eof

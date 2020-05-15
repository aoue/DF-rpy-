
init -2 python:
    #--- ENEMY MOVES ---
    class enemy_move(move):
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

            #additional variables
            self.weight = 0 #more powerful moves have higher. max 100. min 1. a unit must have at least one (weight 1) move.
            self.effort = 0 #1(heavy), 2(medium), 3(light). To help the enemy think.
            self.targeting = 0 #what is the move's preferred target.
            self.aoe = 0 #0: not aoe, 1: is aoe

        #getters
        def get_weight(self):
            return self.weight
        def get_effort(self):
            return self.effort
        def get_aoe(self):
            return self.aoe
        def pick_target(self, pl, el, battle):
            if self.get_aoe() == 0: #single target
                pass
                #for unit in pl

            else: #aoe
                pass
                ##choosing aoe target area:
                #for each square in every (row max - aoe length) in every (column max - target area height):
                    #tally all the units in the square taking the current square as top left.
                        #keep a running max
                #use on the best area (9/10) or random area (1/10 accompanied by line: 'ugh - my hand slipped!' maybe?
            return target


    class e_claw(enemy_move):
        def __init__(self):
            self.rank = 1 #can be 0 (anywhere), 1 (front), or 2 (back).
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 2 #0 for needs total clear path. 1 for needs only clear destination. 2 doesn't move.
            self.stamina_drain = 0 #the amount of stamina the unit loses using this move
            self.able_drain = 1 #the amount of able the unit loses using this move
            self.power = 25 #affects damage
            self.hit = 2 #affects dodging
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

            #additional variables
            self.weight = 100 #more powerful moves have higher. max 100. min 1. the higher the weight, the more likely the move is to be used.
            self.effort = 1 #1(heavy), 2(medium), 3(light). To help the enemy think.

        def exert(self, unit, battle):
            #unit: the unit doing the attack
            #sq: the clicked square. tuple
            #battle: the battle class

            #moves cost stamina and able
            self.drain(unit)
            self.translate(unit, battle)

            #targeting.
            #for this test, just target the first unit in pl
            target = battle.get_pl()[0]
            targetlist = [target]

            #calc damage and deal it to the target
            self.do_damage(unit, targetlist)























##eof

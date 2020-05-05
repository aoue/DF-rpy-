
init python:
    #--- MOVES ---
    class move():
        def __init__(self):
            self.flavour = "{i}flavour text/move description{/i}"
            self.title = "move"
            self.rank = 0 #can be 0, 1, or 2. determines where the move can be used
            self.type = 1 #for targeting. each one means a different shape. legend on 'combat screens.rpy'
            self.iff = 0 #for which board. 0: enemy board, 1: allied board. 2: enemy board, set location. 3: allied board, set location.
            self.clearance = (0,0) #the movement in the column and row direction that the unit will make. also, need to check that the move is possible for the unit to click on it.
            self.clearance_type = 0 #0 for needs total clear path. 1 for needs only clear destination.
            self.stamina_drain = 0 #the amount of stamina the unit loses using this move
            self.able_drain = 0 #the amount of able the unit loses using this move
            self.power = 0 #affects damage
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
        def get_damage_type(self):
            return self.damage_type
        def get_element(self):
            return self.element
        #useful functions
        def translate(self, unit, battle):
            #we do not have to worry about borders, because the player cannot click on the move if its out of bounds.
            unit.set_point(unit.get_point().get_x() + self.get_clearance()[0], unit.get_point().get_y() + self.get_clearance()[1])

            #update unit position in map
            battle.get_allymap().place_unit(unit)
        def drain(self, unit):
            unit.set_stamina(max(unit.get_stamina()-self.get_stamina_drain(), 0))

            dif = unit.get_able() - self.get_able_drain()

            if dif < 0: #if the drain is greater than the unit's able
                dif = abs(dif) #take abs of dif
                for i in range(0, dif): #for each able drain greater than unit's able, remove 5 stam
                    unit.set_stamina(max(unit.get_stamina()-5, 0))
                    dif -= 1

            unit.set_able(dif)

    class hit(move):
        def __init__(self):
            self.flavour = "{i}A hit, hard and fast.{/i}"
            self.title = "Hit"
            self.rank = 1
            self.type = 1
            self.iff = 0
            self.clearance = (0,0)
            self.clearance_type = 0
            self.stamina_drain = 15
            self.able_drain = 1
            self.power = 20
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
                target.take_damage(unit.calc_damage(target, self.get_type(), self.get_element(), self.get_power()))

    class jumpkick(move):
        def __init__(self):
            self.flavour = "{i}Fly in from the back.{/i}"
            self.title = "Jump Kick"
            self.rank = 2
            self.type = 2
            self.iff = 0
            self.clearance = (0,-2)
            self.clearance_type = 1
            self.stamina_drain = 20
            self.able_drain = 3
            self.power = 25
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            self.drain(unit)
            self.translate(unit, battle)

            #for some reason only Yve doesn't do damage? check her stats, ok?
            #mc and yve JUST BOTH DID THE SAME JUMP KICK ON SAME SQUARE AND YVE DID NO DAMAGE WHILE MC DID 17
            #F
            target = battle.get_enemymap().search_map(sq)
            target2 = battle.get_enemymap().search_map((sq[0],sq[1]-1))

            if target != None:
                target.take_damage(unit.calc_damage(target, self.get_type(), self.get_element(), self.get_power()))
            if target2 != None:
                target2.take_damage(unit.calc_damage(target2, self.get_type(), self.get_element(), self.get_power()))

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
            self.damage_type = 0 #0: deals physical damage, 1: deals magical damage
            self.element = 0 #damage element. 0 through 8. see spreadsheet or top of this docs

        def exert(self, unit, sq, battle):
            #unit: the unit doing the attack
            #sq: the clicked square
            pass

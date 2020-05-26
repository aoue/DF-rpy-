


## accessories. gotta look pretty.

init python:
    ## -- Accessories -- ##
    class accessory():
        def __init__(self):
            self.title = "" #weapon name
            self.flavour = "" #flavour text
            self.flag = 0 #1,2,3,4. corresponds to type of item.
            self.type = 0 #int. who can equip it.
            self.phys = 0 #affects phys damage dealt. min 0.
            self.mag = 0 #affects mag damage dealt. min 0.
            self.hit = 0 #affects hit %
            self.aff = 0 #affects damage affinity
            self.passive = 0 #0: no passive. 1: yes passive.

        #getters
        def get_title(self):
            return self.title
        def get_flag(self):
            return self.flag
        def get_flavour(self):
            return self.flavour
        def get_type(self):
            return self.type
        def get_phys(self):
            return self.phys
        def get_mag(self):
            return self.mag
        def get_hit(self):
            return self.hit
        def get_aff(self):
            return self.aff
        def get_passive(self):
            return self.passive

    class regen_band(accessory):
        def __init__(self):
            self.title = "" #weapon name
            self.flavour = "" #flavour text
            self.flag = 0 #1,2,3,4. corresponds to type of item.
            self.type = 0 #int. who can equip it.
            self.phys = 0 #affects phys damage dealt. min 0.
            self.mag = 0 #affects mag damage dealt. min 0.
            self.hit = 0 #affects hit %
            self.aff = 0 #affects damage affinity.
            self.passive = 1 #when the passive triggers. 0: never. 1:start of round. 2:when unit attacks. 3:when unit is attacked.

        #useful functions
        def use_passive(self, unit):
            #heal 4% of health every time the unit acts
            unit.set_hp(min(unit.get_hp() + (1.04*unit.get_hpmax()), unit.get_hpmax()))























##eof

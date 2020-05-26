#TODO
 #-move types: affected by weapon affinity, or move unique affinity.
 #-call weapon/armor passives at the right time.
 #-how armour affinity affects our unit taking damage: the unit's base affinity accounts for 70% of damage, while armour affinity accounts for 30% of damage. like ebf

## --- Legend --- ##
#weapon type:
    #0: enemy
    #1: spear (yve)
    #2: tools (boy)



#affinity follows the same legend as the rest.


init python:
    ## -- Weapons -- ##
    class weapon():
        def __init__(self):
            self.img = "" #normal image
            self.img_h = "" #hovered image
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
        def get_image(self):
            return self.img
        def get_image_h(self):
            return self.img_h
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

        #useful functions
        def use_passive(self):
            pass #do a thing.

    ## -- Spears -- ##
    class folding_spear(weapon):
        def __init__(self):
            self.img = "folding_spear"
            self.img_h = "folding_spear_h"
            self.title = "Folding Spear"
            self.flavour = "Simple spear that folds to a fraction of its size."
            self.flag = 2
            self.type = 1
            self.phys = 30
            self.mag = 10
            self.hit = 5
            self.aff = 0
            self.passive = 0

    ## -- Tools -- ##
    class screwbox(weapon):
        def __init__(self):
            self.title = "Screwbox"
            self.flavour = "Squareheads."
            self.flag = 2
            self.type = 2
            self.phys = 5
            self.mag = 5
            self.hit = 0
            self.aff = 0
            self.passive = 0

    ## -- Enemy Weapons --##
    class beast_claw(weapon):
        def __init__(self):
            #self.img = "folding_spear"
            #self.img_h = "folding_spear_h"
            self.title = "Beast Claw"
            self.flavour = "Claws, attached to the foot of a beast."
            self.flag = 2
            self.type = 0
            self.phys = 20
            self.mag = 0
            self.hit = 0
            self.aff = 0
            self.passive = 0

    class horrible_claw(weapon):
        def __init__(self):
            #self.img = "folding_spear"
            #self.img_h = "folding_spear_h"
            self.title = "Horrible Claw"
            self.flavour = "Horrible claws, stuck with blood and vomit."
            self.flag = 2
            self.type = 0
            self.phys = 20
            self.mag = 0
            self.hit = 0
            self.aff = 0
            self.passive = 0

















##eof

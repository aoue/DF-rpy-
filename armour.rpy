
init python:
    #armour type:
        #1: dess (light)
        #2: palk (medium)
        #3: flex (heavy)


    ## -- Armour -- ##
    class armour():
        def __init__(self):
            self.img = "" #normal image
            self.img_h = "" #hovered image
            self.title = "" #armour name
            self.flavour = "" #flavour text
            self.flag = 1
            self.type = 0 #int. who can equip it.
            self.phys = 0 #affects phys damage taken.
            self.mag = 0 #affects mag damage taken.
            self.dodge = 0 #affects dodge %
            self.aff = 0 #affects unit's affinity
            self.passive = 0 #0: no passive. 1: yes passive.

        #getters
        def get_image(self):
            return self.img
        def get_image_h(self):
            return self.img_h
        def get_title(self):
            return self.title
        def get_flavour(self):
            return self.flavour
        def get_flag(self):
            return self.flag
        def get_type(self):
            return self.type
        def get_phys(self):
            return self.phys
        def get_mag(self):
            return self.mag
        def get_dodge(self):
            return self.dodge
        def get_aff(self):
            return self.aff
        def get_passive(self):
            return self.passive

        #useful functions
        def use_passive(self):
            if self.get_passive() == 1:
                pass #do a thing.

    # -- Flex Armour -- ##
    class folding_armour(armour):
        def __init__(self):
            self.img = "folding_armour"
            self.img_h = "folding_armour_h"
            self.title = "Folding Armour"
            self.flavour = "Simple armour that folds to a fraction of its size."
            self.flag = 1
            self.type = 3
            self.phys = 10
            self.mag = 10
            self.dodge = 20
            self.aff = 0
            self.passive = 0

        def use_passive(self):
            if self.get_passive() == 1:
                pass
    class bascule_armour(armour):
        def __init__(self):
            self.img = "bascule_armour"
            self.img_h = "bascule_armour_h"
            self.title = "Bascule Armour"
            self.flavour = "Thick armour worn underneath the clothes."
            self.flag = 1
            self.type = 3
            self.phys = 30
            self.mag = 20
            self.dodge = -5
            self.aff = 0
            self.passive = 0

        def use_passive(self):
            if self.get_passive() == 1:
                pass


    ## -- Light Armour -- ##
    class smock_armour(armour):
        def __init__(self):
            self.title = "Smock"
            self.flavour = "Uncomfortable, but protective, smock. Smock."
            self.flag = 1
            self.type = 1
            self.phys = 10
            self.mag = 0
            self.dodge = 5
            self.aff = 0
            self.passive = 0

        def use_passive(self):
            if self.get_passive() == 1:
                pass

    class beast_skin(armour):
        def __init__(self):
            self.title = "Beast Skin"
            self.flavour = "Thick, hardened skin."
            self.flag = 1
            self.type = 1
            self.phys = 15
            self.mag = 5
            self.dodge = 10
            self.aff = 0
            self.passive = 0

        def use_passive(self):
            if self.get_passive() == 1:
                pass













































##eof

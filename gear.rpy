
#gear stuff.


init -2 python:
    ## -- Gear Type -- ##
    #Flag:
    #0: reserved for enemies.
    #1: weapon
    #2: armour
    #3: accessory
    #Weapon types: can only equip unit's type.
    #0: reserved for enemies.
    #1: spear (yve)
    #2: tools (boy)
    #3: swords (federal)
    #4: guns (aide, dg)
    #Armour type: can only equip unit's type and lower types.
    #1: light
    #2: medium
    #3: heavy
    #Accessory types: can only equip unit's type.
    #0: reserved for enemies.
    #1: headbands (yve)
    #2: belts (boy)


    ## -- Gear -- ##
    class Gear():
        def __init__(self):
            self.title = "" #weapon name
            self.flavour = "" #flavour text
            self.flag = 0 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 0 #int. who can equip the gear within its flag.
            self.aff = 0 #affects damage affinity
            self.aff_name = ""
            self.passive = 0 #0: has no passive. otherwise it will be a class.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 0

        #getters
        def get_energy(self):
            return self.energy
        def get_title(self):
            return self.title
        def get_flavour(self):
            return self.flavour
        def get_flag(self):
            return self.flag
        def get_type(self):
            return self.type
        def get_aff(self):
            return self.aff
        def get_aff_name(self):
            return self.aff_name
        def get_passive(self):
            return self.passive
        def get_hp(self):
            return self.hp
        def get_able(self):
            return self.able
        def get_stamina(self):
            return self.stamina
        def get_restam(self):
            return self.restam
        def get_physa(self):
            return self.physa
        def get_maga(self):
            return self.maga
        def get_physd(self):
            return self.physd
        def get_magd(self):
            return self.magd
        def get_hit(self):
            return self.hit
        def get_dodge(self):
            return self.dodge
        def use_passive(self):
            pass #do a thing. if the weapon has a passive, it is defined in the weapon's class.


    ## -- Weapons -- ##
    class Folding_spear(Gear):
        def __init__(self):
            self.title = "Folding Spear" #weapon name
            self.flavour = "A light, flexible spear that folds to a fraction of its size." #flavour text
            self.flag = 2 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 1 #int. who can equip the gear within its flag.
            self.aff = 0 #affects damage affinity
            self.aff_name = "Normal"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 10
            self.restam = 0
            self.physa = 15
            self.maga = 15
            self.physd = 0
            self.magd = 0
            self.hit = 5
            self.dodge = 5
    class Screwbox(Gear):
        def __init__(self):
            self.title = "Screwbox" #weapon name
            self.flavour = "Half-inch." #flavour text
            self.flag = 2 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 2 #int. who can equip the gear within its flag.
            self.aff = 6 #affects damage affinity
            self.aff_name = "Metal"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 1
            self.maga = 0
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 0
    class Regulation_sword(Gear):
        def __init__(self):
            self.title = "Regulation Sword" #weapon name
            self.flavour = "A mass-produced sword favoured by government agencies." #flavour text
            self.flag = 2 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 3 #int. who can equip the gear within its flag.
            self.aff = 0 #affects damage affinity
            self.aff_name = "Normal"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 20
            self.maga = 5
            self.physd = 0
            self.magd = 0
            self.hit = 5
            self.dodge = 0
    class Regulation_rifle(Gear):
        def __init__(self):
            self.title = "Regulation Rifle" #weapon name
            self.flavour = "A mass-produced rifle favoured by government agencies." #flavour text
            self.flag = 2 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 4 #int. who can equip the gear within its flag.
            self.aff = 0 #affects damage affinity
            self.aff_name = "Normal"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 15
            self.maga = 10
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 0
    class Beast_claw(Gear):
        def __init__(self):
            self.title = "Beast claw" #weapon name
            self.flavour = "Claws sharpened by the forces of nature." #flavour text
            self.flag = 2 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 0 #int. who can equip the gear within its flag.
            self.aff = 1 #affects damage affinity
            self.aff_name = "Beast"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 10
            self.maga = 0
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 5
    class Beast_claw(Gear):
        def __init__(self):
            self.title = "Beast Spit" #weapon name
            self.flavour = "Vile spit. Don't get it in your hair." #flavour text
            self.flag = 2 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 0 #int. who can equip the gear within its flag.
            self.aff = 1 #affects damage affinity
            self.aff_name = "Beast"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 5
            self.maga = 15
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 5

    ## -- Armour -- ##
    class Folding_armour(Gear):
        def __init__(self):
            self.title = "Folding Armour" #weapon name
            self.flavour = "A light, flexible armour that folds to a fraction of its size." #flavour text
            self.flag = 1 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 1 #int. who can equip the gear within its flag.
            self.aff = 0 #affects damage affinity
            self.aff_name = "Normal"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 10
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 15
            self.magd = 15
            self.hit = 0
            self.dodge = 10
    class Regulation_armour(Gear):
        def __init__(self):
            self.title = "Regulation Armour" #weapon name
            self.flavour = "Widespread armour." #flavour text
            self.flag = 1 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 1 #int. who can equip the gear within its flag.
            self.aff = 0 #affects damage affinity
            self.aff_name = "Normal"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 20
            self.magd = 10
            self.hit = 0
            self.dodge = 0
    class Bascule_armour(Gear):
        def __init__(self):
            self.title = "Bascule Armour" #weapon name
            self.flavour = "Strong armour, perfect for getting roughed about in." #flavour text
            self.flag = 1 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 3 #int. who can equip the gear within its flag.
            self.aff = 6 #affects damage affinity
            self.aff_name = "Metal"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 10
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 30
            self.magd = 20
            self.hit = 0
            self.dodge = -5
    class Smock_armour(Gear):
        def __init__(self):
            self.title = "Smock Armour" #weapon name
            self.flavour = "A smock, best suited for off the battlefield." #flavour text
            self.flag = 1 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 1 #int. who can equip the gear within its flag.
            self.passive = 0 #0: has no passive. 1: has a passive.
            self.aff_name = "Normal"
            self.aff = 0 #affects damage affinity

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 5
            self.magd = 0
            self.hit = 0
            self.dodge = 0
    class Beast_skin(Gear):
        def __init__(self):
            self.title = "Beast Skin" #weapon name
            self.flavour = "Skin hardened by the forces of nature." #flavour text
            self.flag = 1 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 0 #int. who can equip the gear within its flag.
            self.aff = 1 #affects damage affinity
            self.aff_name = "Beast"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 10
            self.magd = 10
            self.hit = 0
            self.dodge = 10


    ## -- Accessories -- ##
    class Plain_headband(Gear):
        def __init__(self):
            self.title = "Plain Headband" #weapon name
            self.flavour = "A plain headband Yve brought with her." #flavour text
            self.flag = 3 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 1 #int. who can equip the gear within its flag.
            self.aff_name = "-"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 10
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 5
    class Plain_belt(Gear):
        def __init__(self):
            self.title = "Plain Belt" #weapon name
            self.flavour = "A plain belt." #flavour text
            self.flag = 3 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 2 #int. who can equip the gear within its flag.
            self.aff_name = "-"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 5
            self.magd = 5
            self.hit = 0
            self.dodge = 0



    # -- Special -- ##
    class None_armour(Gear):
        def __init__(self):
            self.title = "Nothing" #weapon names
            self.flavour = "Nothing." #flavour text
            self.flag = 1 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 0 #int. who can equip the gear within its flag.
            self.passive = 0 #0: has no passive. 1: has a passive.
            self.aff_name = "-"

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 0
    class None_weapon(Gear):
        def __init__(self):
            self.title = "Nothing" #weapon names
            self.flavour = "Nothing." #flavour text
            self.flag = 2 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 0 #int. who can equip the gear within its flag.
            self.aff_name = "-"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 0
    class None_accessory(Gear):
        def __init__(self):
            self.title = "Nothing" #weapon names
            self.flavour = "Nothing." #flavour text
            self.flag = 3 #1,2,3. corresponds to 1:armour, 2:weapon, 3:accessory
            self.type = 0 #int. who can equip the gear within its flag.
            self.aff_name = "-"
            self.passive = 0 #0: has no passive. 1: has a passive.

            #how the gear affects stats. adds the integer to the stat value. every piece of gear can affect every stat.
            self.energy = 0
            self.hp = 0
            self.able = 0
            self.stamina = 0
            self.restam = 0
            self.physa = 0
            self.maga = 0
            self.physd = 0
            self.magd = 0
            self.hit = 0
            self.dodge = 0














##eof

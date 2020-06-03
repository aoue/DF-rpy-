

#focuses. they control how the unit levels up.
# -stat growth
# -moves learned.


init -10 python:
    class Focus():
        def __init__(self):
            self.title = "" #name of the focus
            self.flavour = "" #flavour of the focus shown to the player
            self.physa_up = 0 #how the unit's physa will be increased after each level
            self.physd_up = 0 #etc
            self.maga_up = 0
            self.magd_up = 0
            self.hit_up = 0
            self.dodge_up = 0


            self.learnlist = []  #all moves the unit can learn under this focus

        def get_title(self):
            return self.title

    def level_up(self, unit):
        #what to do when the unit levels up. handle it all here.
        pass

    class Focus_fighter(Focus):
        def __init__(self):
            self.title = "Fighter"
            self.flavour = ""
            self.physa_up = 2
            self.physd_up = 2
            self.maga_up = 1
            self.magd_up = 0
            self.hit_up = 0
            self.dodge_up = 0

            self.learnlist = [Whirl()]  #all moves the unit can learn under this focus

    class Focus_assistant(Focus):
        def __init__(self):
            self.title = "Fighter"
            self.flavour = ""
            self.physa_up = 2
            self.physd_up = 2
            self.maga_up = 1
            self.magd_up = 0
            self.hit_up = 0
            self.dodge_up = 0

            self.learnlist = []  #all moves the unit can learn under this focus















##eof

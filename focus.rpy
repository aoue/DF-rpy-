

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
        #getters
        def get_title(self):
            return self.title
        def get_flavour(self):
            return self.flavour
        def get_physa_up(self):
            return self.physa_up
        def get_physd_up(self):
            return self.get_physd_up
        def get_maga_up(self):
            return self.maga_up
        def get_magd_up(self):
            return self.magd_up
        def get_hit_up(self):
            return self.hit_up
        def get_dodge_up(self):
            return self.dodge_up
        def get_learnlist(self):
            return self.learnlist
        #useful functions
        def inc_stats(self, unit):
            #increases the unit's stats on level up.
            pass
        def learn_move(self, unit):
            #checks if the unit learns a new move. if the unit does, then it appends the appropriate move to movelist. WIP. the numbers will definitely need changing later.
            if unit.get_lvl() == 0:
                return -1
            elif unit.get_lvl() % 5 == 0:
                i = (unit.get_lvl()/5) + 1
                return self.get_learnlist()[i]
            elif unit.get_lvl() == 2:
                i = 0
                return self.get_learnlist()[i]
            elif unit.get_lvl() == 8:
                i = 2
                return self.get_learnlist()[i]
            return -1
            #appends the move corresponding to the level up to the unit's movelist.


        def level_up(self, unit, exp, showlist):
            #method:
            # -see if the unit reaches a level up.
            # -if they do, increase stats.
                # -check if unit gets to change focus.
                # -if they do, allow player to pick focus.
                # -check if unit learns a new move.
                # -if they do, append to movelist

            #for showlist
            newmove = -1 #set by default to -1, which means no new move
            lvlup = 0 #set by default to the unit didn't level up
            focusup = 0 #set by default to the unit doesn't get the chance to change focus
            oldexp = unit.get_exp() #the exp the unit had before the battle

            if unit.get_exp() + exp >= unit.get_next_level_exp() and unit.get_lvl() < LEVELCAP:
                unit.set_lvl(unit.get_lvl()+1)
                lvlup = 1
                #the unit levels up
                self.inc_stats(unit) #the unit's stats are increased by the values defined by the focus.
                newmove = self.learn_move(unit) #check if the unit gets a new move.

                if newmove != -1:
                    unit.get_movelist().append(newmove)

                unit.set_exp((unit.get_exp()+exp) - unit.get_next_level_exp())


                #check if the unit has enough exp to level up again:
                if unit.get_exp() >= unit.get_next_level_exp():
                    unit.set_exp(unit.get_next_level_exp()-1) #cannot gain two levels in one go. if you have the exp for it, you get your exp reset to the exp necessary for the next level, subtract one. so... yeah. It really shouldn't happen, to be honest.

                if unit.get_lvl() % 10 == 0:
                    focusup = 1 #gives the unit the option to change focus in the next screen
            else:
                unit.set_exp(min(unit.get_exp()+exp, unit.get_next_level_exp()-1))

            #append a tuple.
            # -[0]: unit. the unit. someone nice, I hope.
            # -[1]: unit's old level. int. just to be shown for cosmetic reasons.
            # -[2]: did unit level up? 1: yes, 0: no
            # -[3]: is it a level where the unit gets to change focus (and the unit leveled up)? 1: yes, 0: no
            showlist.append((unit, newmove, lvlup, focusup, oldexp))


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

            self.learnlist = [-1]  #all moves the unit can learn under this focus















##eof

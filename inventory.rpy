


init python:

    class Inventory():
        #class inventory.
        #four lists:
        #-armour
        #-weapons
        #-accessories
        #-items
        def __init__(self):
            self.view = 0 #0, 1, 2, 3. changes which list will be shown in other screens.
            self.money = 0 #money - for spending. int
            self.armourlist = [] #armour - for equipping. (gear object, quantity)
            self.weaponlist = [] #weapons - for equipping. (gear object, quantity)
            self.acclist = [] #accessories - for equipping. (gear object, quantity)
            self.itemlist = [] #items - for using. (item object, quantity)
            self.matlist = [] #materials - for crafting (material object, quantity)

            self.keylist = [1] #key item list. used for door keys. don't change its size. should be full size at the start of the game.
            self.chestkey = 0 #counts number of chest keys
            self.questlist = [] #quest item list. used for item retrieval for quests or if it will be important whether the player has a certain item.

        #getters
        def get_money(self):
            return self.money
        def get_chestkey(self):
            return self.chestkey
        def get_keylist(self):
            return self.keylist
        def get_quest(self):
            return self.questlist
        def get_view(self):
            return self.view
            
        def get_arm(self):
            return self.armourlist
        def get_wea(self):
            return self.weaponlist
        def get_acc(self):
            return self.acclist
        def get_ite(self):
            return self.itemlist
        def get_mat(self):
            return self.matlist

        #setters
        def add_money(self, x):
            self.money += x
        def set_chestkey(self, x):
            self.chestkey = x

        #add to lists
        def add_key(self, x):
            self.get_keylist()[x] = 1
        def add_gear(self, thing):



            #if thing is in the first element of any of the tuples in the list
            #if any(x == thing for x,y in self.get_arm())
            if thing.get_flag() == 0:
                return
            elif thing.get_flag() == 1:
                nl = self.get_arm()
            elif thing.get_flag() == 2:
                nl = self.get_wea()
            elif thing.get_flag() == 3:
                nl = self.get_acc()
            elif thing.get_flag() == 4:
                nl = self.get_ite()
            else:
                nl = self.get_mat()

            wip = 0
            if not nl: #if list is empty, then add to list
                nl.append((thing, 1))
            else: #if list not empty
                for tup in nl:
                    if type(tup[0]) == type(thing): #if the item is already in the list
                        nl[nl.index(tup)] = (tup[0], tup[1] + 1) #then increase quantity by 1 and break
                        wip = 1
                        break

                if wip == 0:
                    nl.append((thing, 1))


        def remove_gear(self, thing):
            if thing.get_flag() == 0:
                return
            elif thing.get_flag() == 1:
                nl = self.get_arm()
            elif thing.get_flag() == 2:
                nl = self.get_wea()
            elif thing.get_flag() == 3:
                nl = self.get_acc()
            elif thing.get_flag() == 4:
                nl = self.get_ite()
            else:
                nl = self.get_mat()

            for tup in nl:
                if type(tup[0]) == type(thing):
                    if tup[1] - 1 == 0:
                        nl.remove(tup)
                    else:
                        nl[nl.index(tup)] = (tup[0], tup[1] - 1)
































##eof

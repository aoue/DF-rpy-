


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
            self.armourlist = [] #armour - for equipping. gear objects
            self.weaponlist = [] #weapons - for equipping. gear objects
            self.acclist = [] #accessories - for equipping. gear objects
            self.itemlist = [] #items - for using. item object.
            self.matlist = [] #materials - for crafting material object.

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
            if thing.get_flag() == 0:
                return
            if thing.get_flag() == 1:
                self.get_arm().append(thing)
            elif thing.get_flag() == 2:
                self.get_wea().append(thing)
            elif thing.get_flag() == 3:
                self.get_acc().append(thing)
            elif thing.get_flag() == 4:
                self.get_ite().append(thing)
            else:
                self.get_mat().append(thing)
        def remove_gear(self, thing):
            if thing.get_flag() == 0:
                return
            if thing.get_flag() == 1:
                self.get_arm().remove(thing)
            elif thing.get_flag() == 2:
                self.get_wea().remove(thing)
            elif thing.get_flag() == 3:
                self.get_acc().remove(thing)
            elif thing.get_flag() == 4:
                self.get_ite().remove(thing)
            else:
                self.get_mat().remove(thing)


























##eof

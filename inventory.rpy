
init python:

    class inventory():
        #class inventory.
        #four lists:
        #-armour
        #-weapons
        #-accessories
        #-items
        def __init__(self):
            self.view = 0 #0, 1, 2, 3. changes which list will be shown in other screens.
            self.armourlist = []
            self.weaponlist = []
            self.acclist = []
            self.itemlist = []

        #getters
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

        #add to lists
        def add_gear(self, gear):
            if gear.get_flag() == 1:
                self.get_arm().append(gear)
            elif gear.get_flag() == 2:
                self.get_wea().append(gear)
            elif gear.get_flag() == 3:
                self.get_acc().append(gear)
            else:
                self.get_ite().append(gear)





            #bisect.insort(nl, gear)
        def remove_gear(self, gear):
            if gear.get_flag() == 1:
                self.get_arm().remove(gear)
            elif gear.get_flag() == 2:
                self.get_wea().remove(gear)
            elif gear.get_flag() == 3:
                self.get_acc().remove(gear)
            else:
                self.get_ite().remove(gear)


























##eof

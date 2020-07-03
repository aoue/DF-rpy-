
#put all the item class stuff in here.

init python:
    class Item():
        def __init__(self):
            self.title = "" #item name
            self.flavour = "" #flavour text
            self.flag = 4 #always 4. 4 corresponds to items

        #getters
        def get_title(self):
            return self.title
        def get_flavour(self):
            return self.flavour
        def get_flag(self):
            return self.flag

        #useful functions
        def exert(self):
            pass #varies depending on item



































##eof



#put all the stuff for the material class in here

init python:
    class Material():
        def __init__(self):
            self.title = "" #item name
            self.flavour = "" #flavour text
            self.flag = 5 #always 5. 5 corresponds to materials

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

    class Mat_dog_teeth(Material):
        def __init__(self):
            self.title = "Dog Teeth" #item name
            self.flavour = "Canines fallen from the mouth of a dog during the excitement." #flavour text
            self.flag = 5 #always 5. 5 corresponds to materials



    #more materials to add:
    #prologue:
    # -intact dog claw
    # -mangy fur













##eof

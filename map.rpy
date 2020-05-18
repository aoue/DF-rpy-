#method:

#map nav for act I.
#here's how it works:
#-- when the screen is called, it is given arguments. These are:
#-first arg: list of booleans that determine whether a location is unlocked.
#-second arg: list of str label names that should be jumped to. paired one-to-one with first list.
#update the lists with each call.

#-----ACT I index-----#
#a certain item in the list always corresponds to the same physical location. It is as follows:
# [0] = apartment
# [1] = cafe(s)
# [2] = library
# [3] = dorms
# [4] = (azalea) field
# [5] = (no) street (in particular)
# [6] =
# [7] =
# etc

init python:
    #overworld map
    class overworld():
        def __init__(self):
            self.chapter = 0 #str. from 0 (prologue) to 8 (chapter 8). master key to control everything else.

            #--- lists of lists. each list inside corresponds to a chapter ---#
            self.unlocked = [[1]] #whether the location can trigger an event.
            self.jumps = [["fail"]] #str of the label we're jumping to.
            self.descr = [["nice place"]] #str description on hover.
            self.images = [["face_boy"]] #normal image for a location
            self.hovers = [["face_boy_hover"]] #hover image for a location
            self.positions = [[(300, 400)]] #position for a location
            self.bg = [["prologue_bg"]] #the background image.

        #getters.
        def get_chapter(self):
            return self.chapter
        #getters automatically return the chapter's list inside the larger list
        def get_unlocked(self):
            return self.unlocked[self.get_chapter()]
        def get_jumps(self):
            return self.jumps[self.get_chapter()]
        def get_descr(self):
            return self.descr[self.get_chapter()]
        def get_images(self):
            return self.images[self.get_chapter()]
        def get_hovers(self):
            return self.hovers[self.get_chapter()]
        def get_positions(self):
            return self.positions[self.get_chapter()]
        def get_bg(self):
            return self.bg[self.get_chapter()]


        #useful functions
        def show_overworld(self):
            renpy.show(self.get_bg()[self.get_chapter()])
            renpy.call_screen("overworld_map", self.get_unlocked(), self.get_jumps(), self.get_descr(), self.get_images(), self.get_hovers(), self.get_positions())










##eof

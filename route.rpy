
#put events chains/routes in here.

init python:

    #a route is a chain of events
    class Route():
        def __init__(self):
            self.inc = 0 #each time you do an event in the route, the inc increases.
            self.position = (x,y) #the position this route should be displayed at.
            self.jumps = [] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event. list.
            self.lock = 0 #at 0, unlocked. at 1, locked.
            self.descr = "" #description string

        #getters
        def get_inc(self):
            return self.inc
        def get_lock(self):
            return self.lock
        def get_jumps(self):
            return self.jumps
        def get_descr(self):
            return self.descr
        def get_images(self):
            return self.images
        def get_position(self):
            return self.position
        #setters
        def inc_up(self):
            self.inc += 1
        def set_descr(self, x):
            self.descr = x
        def set_view(self, view):
            self.view = view
        def set_lock(self, x):
            self.lock = x
        #useful functions
        def call_event(self):
            renpy.call_in_new_context(self.get_jumps()[self.get_inc()])
            self.inc_up()
            self.set_lock(1)

    #main story routes.
    #one per chapter, just to avoid getting cluttered. delete when chapter is done.
    class Route_ms_0(Route):
        def __init__(self):
            self.inc = 0 #each time you do an event in the route, the inc increases, so next time it calls the next event.
            self.position = (500, 380) #the position this route should be displayed at.
            self.jumps = ["p_ms_1", "p_ms_5"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 0 #at 0, unlocked. at 1, locked.
            self.descr = "main story" #description string


    #character routes
    #both a handler and their operative are contained in the same route. they're named based on which is more important.
    class Route_friday(Route):
        def __init__(self):
            self.inc = 0 #each time you do an event in the route, the inc increases, so next time it calls the next event.
            self.position = (200, 400) #the position this route should be displayed at.
            self.jumps = ["r_friday0", "r_friday1"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 1 #at 0, unlocked. at 1, locked.
            self.descr = "friday" #description string
    class Route_mueler(Route):
        def __init__(self):
            self.inc = 0 #each time you do an event in the route, the inc increases, so next time it calls the next event.
            self.position = (220, 230) #the position this route should be displayed at.
            self.jumps = ["r_mueler0", "r_mueler1"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 0 #at 0, unlocked. at 1, locked.
            self.descr = "mueler" #description string

        ##something for mueler:
        #in some important fight, mc is in combat mode with friday. they take a hit and mc is hurt much worse than friday. he's essentially useless. tori has mc disconnected and has mueler connected in his place. mueler is able to direct friday through the fight successfully. mc starts to hate mueler out of jealously.
    class Route_nai(Route):
        def __init__(self):
            self.inc = 0 #each time you do an event in the route, the inc increases, so next time it calls the next event.
            self.position = (100, 100) #the position this route should be displayed at.
            self.jumps = ["r_nai0", "r_nai1"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 1 #at 0, unlocked. at 1, locked.
            self.descr = "nai" #description string
        #nai's got a robot cat. it's supposed to be more affectionate and easier to take care of. it glitches out and is affectionate to couches and chairs, and it leaks oil everyone. it's a fail.
    class Route_payton(Route):
        def __init__(self):
            self.inc = 0 #each time you do an event in the route, the inc increases, so next time it calls the next event.
            self.position = (200, 400) #the position this route should be displayed at.
            self.jumps = ["r_payton0", "r_payton1"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 1 #at 0, unlocked. at 1, locked.
            self.descr = "payton" #description string
    class Route_tori(Route):
        def __init__(self):
            self.inc = 0 #each time you do an event in the route, the inc increases, so next time it calls the next event.
            self.position = (750, 565) #the position this route should be displayed at.
            self.jumps = ["r_tori0", "r_tori1"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 0 #at 0, unlocked. at 1, locked.
            self.descr = "tori" #description string
    # class Route_newrecruit/mc's junior/name pending()
    #any others
    #end of character routes


    #constant events.
    #these events are repeatable. these type of routes have their own 'call_event' function.
    class Route_crafting(Route):
        #crafting station.
        def __init__(self):
            self.inc = 0 #how many times the player has done this event.
            self.position = (525, 515) #the position this route should be displayed at.
            self.jumps = ["r_crafting0", "r_crafting1"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 0 #at 0, unlocked. at 1, locked.
            self.descr = "?" #description string
        #useful functions
        def call_event(self):
            #renpy.call_in_new_context(self.get_jumps()[self.get_inc()])

            if self.get_inc() == 0:
                renpy.call_in_new_context(self.get_jumps()[0]) #introduction label. can't use the crafting interface yet.
                self.set_descr("Technology")
                self.set_lock(1)


            #if self.get_inc() == a certain milestone.
            # then show some nice event, then show the crafting interface.

            #inc up
    class Route_control(Route):
        #mission control room.
        def __init__(self):
            self.inc = 0 #how many times the player has done this event.
            self.position = (1035, 235) #the position this route should be displayed at.
            self.jumps = ["r_crafting0", "r_crafting1"] #different labels that are jumped to at each stage of the route, as dictated by inc.
            self.images = [] #portraits for all the characters involved at each stage of the event
            self.lock = 0 #at 0, unlocked. at 1, locked.
            self.descr = "?" #description string
        #useful functions
        def call_event(self):
            #renpy.call_in_new_context(self.get_jumps()[self.get_inc()])

            if self.get_inc() == 0:
                renpy.call_in_new_context(self.get_jumps()[0]) #introduction label. can't use the crafting interface yet.
                self.set_descr("Control")
                self.set_lock(1)

            #if self.get_inc() == a certain milestone.
            # then show some nice event, then show the mission control interface. This is how mc can get sidequests.

            #inc up





























##eof

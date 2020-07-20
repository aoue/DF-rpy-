

#routes and events for the prologue only.

#in here we've got:

#available after p_ms_3:

init 1 python:
    class Route_hill(Route):
        def __init__(self):
            self.inc = 0
            self.position = (200, 400)
            self.jumps = ["p_hill"]
            self.images = []
            self.lock = 1
            self.descr = "hill"

    class Route_store(Route):
        def __init__(self):
            self.inc = 0
            self.position = (200, 400)
            self.jumps = ["p_hill"]
            self.images = []
            self.lock = 1
            self.descr = "hill"

    class Route_square(Route):
        def __init__(self):
            self.inc = 0
            self.position = (200, 400)
            self.jumps = ["p_hill"]
            self.images = []
            self.lock = 1
            self.descr = "hill"

    class Route_lab(Route):
        def __init__(self):
            self.inc = 0
            self.position = (200, 400)
            self.jumps = ["p_hill"]
            self.images = []
            self.lock = 1
            self.descr = "hill"

    class Route_radio(Route):
        def __init__(self):
            self.inc = 0
            self.position = (200, 400)
            self.jumps = ["p_hill"]
            self.images = []
            self.lock = 1
            self.descr = "hill"




label p_hill:
    #--hill (talk to friday). optional.

label p_store:
    #--store (pick up the special order of special rope. it's a lot. carry it with you or bring it to the shed?)

label p_square:
    #--square (a few kids are poking at the body of a monster. mc's first time seeing a monster. what's going on here, he asks. friday says yve killed it last night. they left it in the middle of town so it wouldn't attract more, reason being that a corpse smells like food and so do people. payton said moving it outside town would mess up the all the scouting work done so far. option to tell the kids to leave the body alone.)

label p_lab:
    #--lab. (check on the status of the pesticide. the technician says it's going on schedule. mc asks about the pesticide once they leave, but friday doesn't know anything about it.)



# --- #
#available after p_ms_4:


label p_radio:
    #--radio station. maintain contact, check on the reinforcements. they're on schedule. friday hears something, it's the heartbeat of a monster or something. they have to kill it. combat tutorial.)

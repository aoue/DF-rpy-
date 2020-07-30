
##only a temp file. move this all to the main prologue.rpy when done.

#one time events for the prologue only.
# -- Day 1 -- #
init 1 python:
    class Route_square(Route):
        def __init__(self):
            self.inc = 0
            self.position = (200, 400)
            self.jumps = ["p_square"]
            self.images = [] #question mark w/ black background
            self.lock = 1
            self.descr = "Square"

    class Route_lab(Route):
        def __init__(self):
            self.inc = 0
            self.position = (300, 400)
            self.jumps = ["p_lab"]
            self.images = [] #none
            self.lock = 1
            self.descr = "Lab"

    class Route_radio(Route):
        def __init__(self):
            self.inc = 0
            self.position = (400, 400)
            self.jumps = ["p_radio"]
            self.images = [] #question mark w/ black background
            self.lock = 1
            self.descr = "Radio"

    class Route_hill(Route):
        def __init__(self):
            self.inc = 0
            self.position = (0, 400)
            self.jumps = ["p_hill"]
            self.images = [] #friday
            self.lock = 1
            self.descr = "Hill"







#available after p_ms_3:

label p_square:
    #--square (there's the corpse of a beast in the square. They talk about it.)
    #Required event.

    scene cherespoir_square

    "Friday makes her way into the town square. It's not much more than an empty space in the middle of a ring of houses and other businesses. Across the ground is a mismatch of slush and grey, beaten snow. The trails of footprints cross over and into each other like the steps of an elaborate dance."
    "Friday stops in front of something."
    mc "Friday, stop a minute. I saw something back there."
    f "Yes."
    mc "To the left, I think."
    "She turns obligingly. And there it is."

    show cherespoir_corpse

    "It's like a dog. It's reminiscient of the emaciated street dogs of the city, only larger. It's dark fur is matted together by the slush."
    "Laying motionless on the ground, its eyes are unmoving in a calm not found in the feral dog. Beneath it, its legs are stiffened beside holes pawed in the snow."
    "{i}Lupus Eruo.{/i} Not your standard city dog. They're diggers and they can grow to be far larger than the biggest domesticated dog. They're hardly found in cities these days, but there's always one or two people killed by one digging in through the basement if you know how to find the coverage. They would have finished off the rat populations too if the rats weren't, well, rats."
    "But the city isn't the place for them. In the wild they live in large communities, making their dens in naturally-formed cave system while each new generation digs it larger and larger. And with each new generation, they hunt farther and farther away, until they get back to the cities, are hunted, and the cycle continues."
    mc "It's dead then."
    f "Yvette killed her last night."

    python:
        loop = 0
        looptick0 = 0
        looptick1 = 0
    while loop < 2:
        menu:
            "Her?" if looptick0 == 0:
                $loop += 1
                $looptick0 = 1
                mc "Her?"
                f "Yes. We checked. Payton says we must keep track of the population for the estimates."
                mc "It seems like that would be hard to do accurately since they live mostly underground."
                f "Payton says that too."


            "What happened?" if looptick1 == 0:
                $loop += 1
                $looptick1 = 1
                mc "What happened?"
                f "Yvette and I heard her moving through the town last night. Payton said we'd better kill her.{w=1.0} I would have done it, but Payton said I musn't fight alone."
            "[[End]":
                $loop = 2

    "There's a deep stab wound in the beast's flank. There's hints of red in the snow near the injury."
    mc "You just left it... her... in the middle of the street?"
    f "It was more convenient."
    mc "I would imagine the people mind. Don't they care that there's a cadaver right outside their doors?"
    f "Are there people living here?"
    mc "Are you being serious? There must be, right?"
    f "I don't know."
    mc "... We should bury it anyway."
    f "OK."
    "She bends down next to the creature and reaches out towards it."
    mc "No, not with your hands Friday."
    "She stops mid-motion."
    f "There's nothing to use."
    mc "Just... We'll come back if we find something later. Come on, I don't want to make Payton wait for us."
    return

label p_lab:
    #--lab. check on the pesticide. if it's green, that means the container is still sealed and everyone's okay. that's all they're there to check.
    #Required event.

    scene cherespoir_lab
    with longfade

    "This is one of the places on Payton's list. It's dark, and it takes Friday's eyes a short while to become accustomed to it."
    "Contrary to the room's general disrepair, the closest counter, though still coated in dirt and dust and other colourful stains, has trails where someone tried to wipe it down. On the counter is a cylinder a meter high and very thin. It's covered in symbols, most of which I don't recognize, but the familiar skull demarking poison, positioned at the forefront, hints at what's inside."
    mc "Do we need to bring this with us?"
    f "Not today; we only need to check on it. Payton's had me check on it everyday since we got here. If the light's still green, then we're OK."
    mc "And if it's not?"
    f "I don't know. Payton said to pray."
    "Friday walks around to the side of it where a light shines and reflects off the table. It blinks green."
    mc "Well, it's green. So we're done? That's all?"
    "Friday nods."
    f "It's still green, so we're OK."

    return

label p_hill:
    #--hill (talk to friday.
    #look over the town. what are you thinking about friday?
    #what? i dont know.
    #the town looks different today.

    "label: p_hill. loc: prologue_events. status: PL-TODO"

    return



# --- #
#available after p_ms_4:


label p_radio:
    #--radio station. friday tries to get it to work, but cannot.
    #ideally, they wanted to get in contact with the backup team. the switch is that even if they can't, they still have to procede. if they want the mission as a whole to succeed, each part has to act as if each other part is succeeding. Why? inter-branch politics, I think.

    scene cherespoir_square

    "Friday leads us down the street to the last stop. There town's streets are arranged in a cross, and our destination is all the way at the end of one edge. Compared to the rest of the buildings, this one looks much newer. There's even a light on outside."
    "Friday turns it off as she passes."

    scene cherespoir_radio
    with shortfade

    play music radio_static

    mc "..."
    mc "This is another thing Payton showed you how to do?"
    f "Yes. I had to do it yesterday in preparation. Payton said it's vitally important."
    "She adjusts one of the dials on the panel."
    mc "All I hear is static."
    f "Yes. I'm not doing it right. {w=1.0}... It's difficult."
    "She breathes into one of the ends of the headpiece. As she does, her hands turn two dials on the panel. Each time the left instrument is moved, the right one has made a full rotation."

    stop music fadeout 1.0

    "The static cuts for a moment and Friday takes her hands off of the dials. Gradually, a voice makes itself heard amidst the static. It goes on for a few seconds before stopping, then, as continuing as before, it repeats itself from the beginning."

    play music radio_static

    v "Green OK... Route OK... Status OK... All OK..."
    "And it starts again:"
    v "Green OK... Route OK... "

    stop music fadeout 1.0

    "Friday takes the headgear off and the machine's complicated whir stops a moment after."
    f "We have to tell Payton what it said."
    mc "Something bad?"
    f "I don't know. Payton can understand it."

    python:
        ow.get_routes()[2][0].set_lock(0) #unlock the main story --> p_ms_4


    return











##eof

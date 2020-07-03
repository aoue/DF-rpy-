#dimensions are 1280 x 720.

###things that cannot be afforded forgetfulness:
# act 1 may end up not being long enough. two weeks is definitely too long, but maybe a day or two more would be good. these extra days would be filler in the middle focused on building up nice sentiments for the player and the gang, they would have to be before the mountain climbing. (don't worry about it for now, this is a question to readdress later)
# when drawing everyone again for act II, the artstyle should subtly change. more shadows, darker expressions, the works. This fits tone and also avoids the problem of art/story dissonance (a very serious problem.)
# have a mandatory agenda call at the start of each day in act I. (when appropriate)
# show a time stamp or [morning] or whatever at appropriate times during days. could be good.

#TITLE IDEAS
#Dear Friday
#In the Shadow of Mt Pessevaine
#A Town at the Base of Mt Pessevaine
#At the Base of Mt Pessevaine

### ACT PROGRESSION ###
#here are the variables that keep track of what act and what route mc has taken
define persistent.act = 0 #can be (0, 1, 2, 3) for (first launch, act1, act2, act3), respectively.
define persistent.open_on_pickup = False #read new glossary entries on pickup, t/f.

#also:
#character_x_alive = True    #necessary for act II and III, to keep track of whose alive and who's dead

#this specific label name makes it run before the main menu
label before_main_menu:
    #three different title screens and title tracks - one for each act:
    #I: close shot of the 4 main characters on a small hill overlooking the path to the mountain in the background. Add dg once shes been added.
    #II: in a deployment hangar with everyone going to their machines OR a barracks/mess hall with everyone sitting or being. Remove casualty when they die.
    #III: kind of complicated.
        #- background: view from inside mc's cockpit. He's in there, you can see the tubes, wires, etc.
        #- the comm-things of different characters will appear scattered across the screeen, fading in and out, 2 or 3 at a time.
        #- Random chance of each appearing. Each person appears only once per main menu.
        #- each character should have several different dialogue things to bring with them. But if they're already dead, just show static in the textbox and in the icon say 'signal lost'?
        #- call a scene on launch where other characters congratulate mc on his kill. Only one scene per launch and each scene once per game.
    #Epilogue: #$mainmenu = "titlescreen idea.png" <-- like this image, but with different characters. have mc be facing the back so his face is hidden.

    #show logo/etc

    if persistent.act == 0:
        $mainmenu = "mainmenu0.jpg"
        #play music opening1 noloop

    elif persistent.act == 1:
        $mainmenu = "mainmenu1.jpg"
        #play music opening1 noloop

    elif persistent.act == 2:
        $mainmenu = "mainmenu2.jpg"
        #play music opening2 noloop

    else:
        $mainmenu = "mainmenu3.jpg"
        #play music opening3 noloop

    $gui.main_menu_background = mainmenu
    #to change act, just put this in the desired location:
    #$persistent.act = 1

    return

label start:
    stop music fadeout 1.0



    #here we're going to be initializing a bunch of units.
    python:
        #some game settings
        config.rollback_enabled = False

        #some globals
        LEVELCAP = 10 #a unit's level cannot exceed the level cap.

        #character dynamic names

    #jump
    #(for testing a specific label)

    #call display_tests
    #(for testing graphics, effects, etc)

    call tests
    #(for testing programming)

    jump prologue_0

label tests:

    #actions test
    #show screen special_actions_overlay
    #"actions test"
    #"second click"

    #map test
    call map0 from _call_map0

    #combat test
    #call battle0 from _call_battle0  #<--- broken



    #show screen thought("Nai", "laurem ipsum")

    "end of tests"

    return

label display_tests:
    #"testing special chars: \u2603"

    "nothing to see here"



    #y "nai (left), yve (cen), dg (right)"
    #d "lorem ipsum"

    return

label ending1:
    "Somehow you have reached the end of the current build."
    return



##eof

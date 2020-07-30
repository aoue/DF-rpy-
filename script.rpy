#dimensions are 1280 x 720.

#Dear Friday

### ACT PROGRESSION ###
#here are the variables that keep track of what act and what route mc has taken
define persistent.act = 0 #can be (0, 1, 2, 3) for (first launch, act1, act2, act3), respectively.
define persistent.open_on_pickup = False #read new glossary entries on pickup, t/f.


#this specific label name makes it run before the main menu
label before_main_menu:

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


    #call map0 #calls a combat test. 

    default ow = Overworld()

    #if saving is not working. try declaring everything in default! also: the line renpy.retain_after_load() or something seems to be important!

    #here we're going to be initializing a bunch of units.
    python:
        yve = Unit_yve()
        friday = Unit_friday()

        ow.join_party(yve)
        ow.join_party(friday)

        piece1 = Bascule_armour()
        ow.get_inventory().add_gear(piece1)

        config.rollback_enabled = False
        LEVELCAP = 10






    #jump
    #(for testing a specific label)

    #call display_tests
    #(for testing graphics, effects, etc)

    #call tests
    #(for testing programming)

    jump p_ms_0

label tests:

    #actions test
    #show screen special_actions_overlay
    #"actions test"
    #"second click"

    #map test
    #call map0 from _call_map0

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

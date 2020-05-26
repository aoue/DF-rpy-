
###game settings###
define config.has_autosave = True
define config.autosave_slots = 6
define config.autosave_on_quit = True
define config.autosave_on_choice = True
define config.autosave_frequency = 100
define config.has_quicksave = True
define config.rollback_enabled = True #disabling rollback is not user-friendly. HOWEVER, crashing during combat is even less user-friendly. rollback handling is done manually.
define config.quit_action = Quit(confirm=True)
define _game_menu_screen = "preferences"

init python:
    def flashback(image):
        #TODO
        #get current bg
        #renpy.show img
        #reset current bg
        pass

    def copy_list(nl):
        nl_copy = nl[:]
        return nl_copy

    pos_list = [0,1,2,3,4,3,2,1,0]


init -555:
    #------vn display positions------#
    transform maxleft:
        xalign 0.0
        yalign 1.0
    transform farleft:
        xalign 0.1
        yalign 1.0
    transform left:
        xalign 0.2
        yalign 1.0
    transform cen:
        xalign 0.5
        yalign 1.0
    transform right:
        xalign 0.8
        yalign 1.0
    transform farright:
        xalign 0.9
        yalign 1.0
    transform dgright:
        xalign 0.85
        yalign 1.0
    transform maxright:
        xalign 1.0
        yalign 1.0

    #------ deployment ------#
    transform deploypos(x,y):
        pos(x,y)

    #battle fx
    transform e_tile_hover(row, column):
        pos(275 + (125*row), 5 + (65*column))

    transform a_tile_hover(row, column):
        pos(275 + (125*row), 385 + (65*column))


    #px: 320 + 120*(point.get_x()), 135 + 65*(point.get_y())

    #------ally side positions------#

    #px: 275 + 125*(point.get_x()), , 385 + 65*(point.get_y())

    #------enemy side positions------#
    #px: 275 + 125*(point.get_x()), , 5 + 65*(point.get_y())

    ##party screen
    image party_b:
        "overworld/party_button.png"
    image party_h:
        "overworld/party_button_hover.png"
    image party_bg:
        "party/party_bg.jpg"
    image yve_pose:
        "party/yve_pose.png"
    image boy_pose:
        "party/boy_pose.png"
    image party_prev:
        "party/prev.png"
    image party_next:
        "party/next.png"
    image party_prev_h:
        "party/prev_h.png"
    image party_next_h:
        "party/next_h.png"

    ##direction screen
    image direction_b:
        "overworld/direction_button.png"
    image direction_h:
        "overworld/direction_button_hover.png"

    ##hub screen
    image hub_b:
        "overworld/hub_button.png"
    image hub_h:
        "overworld/hub_button_hover.png"

    ##overworld screen
    image prologue_bg:
        "overworld/prologue.jpg"
    image party_icon:
        "dungeon/party_icon.png"

    ##dungeon screen
    image dungeon_bg:
        "dungeon/test_bg.jpg"
    image dungeon_icon:
        "overworld/dungeon_icon.png"
    image dungeon_icon_h:
        "overworld/dungeon_icon_h.png"
    image room:
        "dungeon/room_unexplored.png"
    image room_ex:
        "dungeon/room_explored.png"
    image room_hover:
        "dungeon/room_hover.png"
    image hall_h:
        "dungeon/hallway_horizontal.png"
    image hall_v:
        "dungeon/hallway_vertical.png"

    #face imgs. for deployment screen.
    image face_boy:
        "combat/face/deploy mc.png"
    image face_boy_hover:
        "combat/face/deploy mc hover.png"
    image face_yve:
        "combat/face/deploy yve.png"
    image face_yve_hover:
        "combat/face/deploy yve hover.png"


    #combat background images
    image deployfield0:
        "images/combat/bg/deployfield0.jpg"

    image battlefield0:
        "images/combat/bg/battlefield0.jpg"


    #battle fxs
    image tile_e_hovered:
        "images/combat/fx/tile e hover.png"
    image tile_f_hovered:
        "images/combat/fx/tile f hover.png"


    #unit imgs. dimensions are (82, 60). obv these are trash dimensions.
    image dead_icon:
        "images/combat/units/dead icon.png"

    image icon_grunt:
        "images/combat/units/grunt icon.png"
        0.5
        "images/combat/units/grunt icon 2.png"
        0.5
        repeat

    image icon_jowler:
        "images/combat/units/jowler icon.png"
        0.5
        "images/combat/units/jowler icon 2.png"
        0.5
        repeat
    image icon_groskel:
        "images/combat/units/groskel icon.png"

    image icon_boy:
        "images/combat/units/mc icon.png"
        0.5
        "images/combat/units/mc icon 2.png"
        0.5
        repeat

    image icon_yve:
        "images/combat/units/yve icon.png"
        0.5
        "images/combat/units/yve icon 2.png"
        0.5
        repeat








    #---- combat end ----#

#---- animations and transitions ----#
    define flipfade = ImageDissolve(im.Tile("TransCornerFlip.jpg"), 1.5, 16) #for page turning kind of things
    #template: define fade = Fade(0.5, 0.0, 0.5)    format:(out_time, hold_time, in_time)
    define longfade = Fade(0.5, 0.5, 1.0) #longfade: for more time passing or a locale change
    define shortfade = Fade(0.25, 0, 0.25) #shortfade: for a change of room or whatnot. changing background in the same scene.

    define brightfade = Fade(0.5, 1.0, 0.5, color = "#fff") #fades to white, lingers, proceeds. For when mc is momentarily blinded.
    #^experiment with using an image that looks like bright stuff and use the same method as flipfade. should work fine.

    #thought: for a characters thought to slowly appear.
    define thought = Pixellate(1.0, 2)

    #longthought: for a characters thought to appear only after a long time.
    define longthought = ImageDissolve(im.Tile("thought.png"), 1.5, 16)

    image scarf:
        "animations/scarf1.png"
        0.3
        "animations/scarf2.png"
        0.3
        "animations/scarf3.png"
        0.3
        repeat

    ##rain and lightning##
    image rev_lightning = im.Flip("animations/lightning.png", horizontal=True)
    image rain:
        "animations/rain1.png" #with dissolve
        0.2
        "animations/rain3.png" #with dissolve
        0.2
        "animations/rain2.png" #with dissolve
        0.2
        repeat

        #if we add more images in between it'll look better right.
        #find out whether rain images being shown in random order looks better or worse



    image lightning:
        choice:        #weight of choice is 1
            "animations/lightning.png"
            alpha  0.0
            0.5                 # show nothing for 0.5 seconds

        choice 0.1:   #weight of choice is 0.1
            "animations/lightning.png"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0


        choice 0.1:
            "rev_lightning"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0

        repeat
